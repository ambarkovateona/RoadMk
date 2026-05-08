from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler
from scraper_job import run_scraping

from database import SessionLocal
from models import RoadReport

app = FastAPI(title="AMSM Road Conditions API")

scheduler = BackgroundScheduler()
scheduler.add_job(run_scraping, 'interval', minutes=30)
scheduler.start()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
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
        return {"error": "Report not found"}
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
