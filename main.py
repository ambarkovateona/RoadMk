import logging
from contextlib import asynccontextmanager
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from config import CORS_ORIGINS, SCRAPE_INTERVAL_MINUTES, SCRAPE_ON_STARTUP
from database import SessionLocal
from logging_setup import configure_logging
from models import RoadReport
from scraper_job import run_scraping

configure_logging()
logger = logging.getLogger("roadmk.main")

scheduler = BackgroundScheduler()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Wiring the scheduler up inside the FastAPI lifespan (instead of at
    # module import time) means:
    #  - it is guaranteed to start exactly once, when the app actually
    #    starts serving, and to log that fact;
    #  - it shuts down cleanly with the app instead of leaking a
    #    background thread.
    kwargs = {}
    if SCRAPE_ON_STARTUP:
        # Run once immediately, then every SCRAPE_INTERVAL_MINUTES.
        # Without this, the job only fires for the first time after a
        # full interval has elapsed -- with zero output in the meantime,
        # which is what made the scheduler look broken.
        kwargs["next_run_time"] = datetime.now()

    scheduler.add_job(
        run_scraping,
        "interval",
        minutes=SCRAPE_INTERVAL_MINUTES,
        id="amsm_scraping_job",
        replace_existing=True,
        **kwargs,
    )
    scheduler.start()
    logger.info(
        "Scheduler started: running scraping every %d minute(s) (run on startup: %s)",
        SCRAPE_INTERVAL_MINUTES,
        SCRAPE_ON_STARTUP,
    )

    yield

    logger.info("Shutting down scheduler")
    scheduler.shutdown(wait=False)


app = FastAPI(title="AMSM Road Conditions API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    # allow_credentials=True together with allow_origins=["*"] is invalid
    # per the CORS spec (browsers will reject it) and this API doesn't use
    # cookies/auth, so there is nothing that needs credentialed requests.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def report_to_dict(report: RoadReport):
    return {
        "id": report.id,
        "external_id": report.external_id,
        "category": report.category,
        "title": report.title,
        "description": report.description,
        "raw_text": report.raw_text,
        "status_type": report.status_type,
        "severity": report.severity,
        "valid_from": report.valid_from.isoformat() if report.valid_from else None,
        "valid_to": report.valid_to.isoformat() if report.valid_to else None,
        "is_active": report.is_active,
        "scraped_at": report.scraped_at.isoformat() if report.scraped_at else None,
        "source_url": report.source_url,
    }


@app.get("/")
def root():
    return {"message": "AMSM API is running"}


@app.get("/reports")
def get_reports(
    severity: str | None = Query(default=None),
    category: str | None = Query(default=None),
    status_type: str | None = Query(default=None),
    is_active: bool | None = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(RoadReport)
    if severity:
        query = query.filter(RoadReport.severity == severity)
    if category:
        query = query.filter(RoadReport.category == category)
    if status_type:
        query = query.filter(RoadReport.status_type == status_type)
    if is_active is not None:
        query = query.filter(RoadReport.is_active == is_active)

    reports = query.all()
    priority = {"RED": 1, "YELLOW": 2, "GREEN": 3}
    reports = sorted(reports, key=lambda r: (priority.get(r.severity, 99), r.id))
    return [report_to_dict(report) for report in reports]


@app.get("/reports/{report_id}")
def get_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(RoadReport).filter(RoadReport.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report_to_dict(report)


@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    reports = db.query(RoadReport).all()
    total = len(reports)
    red = len([r for r in reports if r.severity == "RED"])
    yellow = len([r for r in reports if r.severity == "YELLOW"])
    green = len([r for r in reports if r.severity == "GREEN"])
    active = len([r for r in reports if r.is_active])
    return {"total": total, "active": active, "red": red, "yellow": yellow, "green": green}


@app.post("/scrape-now")
def scrape_now():
    """
    Manually trigger a scraping run on demand, outside of the schedule.
    Useful to confirm the scraping logic itself works, and to test the
    scheduler wiring by comparing its logs against this endpoint's logs.
    """
    logger.info("Manual scraping run triggered via /scrape-now")
    result = run_scraping()
    return result
