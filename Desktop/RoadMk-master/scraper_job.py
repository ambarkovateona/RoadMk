import logging
from datetime import date, datetime

from database import SessionLocal
from models import RoadReport
from amsm_scraper import URL, fetch_html, parse_page

logger = logging.getLogger("roadmk.scraper_job")


def parse_date(value):
    if not value:
        return None
    return date.fromisoformat(value)


def _build_report(item: dict) -> RoadReport:
    return RoadReport(
        external_id=item["id"],
        category=item["category"],
        title=item["title"],
        description=item["description"],
        raw_text=item["raw_text"],
        status_type=item["status_type"],
        severity=item["severity"],
        valid_from=parse_date(item["valid_from"]),
        valid_to=parse_date(item["valid_to"]),
        is_active=item["is_active"],
        scraped_at=datetime.fromisoformat(item["scraped_at"]),
        source_url=item["source_url"],
    )


def run_scraping() -> dict:
    logger.info("Scraping run started (source=%s)", URL)

    try:
        html = fetch_html(URL)
    except Exception:
        logger.exception("Failed to fetch the AMSM page, aborting this run")
        return {"status": "fetch_failed", "new_count": 0, "error_count": 0}

    try:
        data = parse_page(html, URL)
    except Exception:
        logger.exception("Failed to parse the AMSM page, aborting this run")
        return {"status": "parse_failed", "new_count": 0, "error_count": 0}

    items = data["items"]
    logger.info("Parsed %d item(s) from the page", len(items))

    db = SessionLocal()
    new_count = 0
    skipped_count = 0
    error_count = 0

    try:
        for item in items:
            try:
                existing = (
                    db.query(RoadReport)
                    .filter_by(external_id=item["id"])
                    .first()
                )
                if existing:
                    existing.title = item["title"]
                    existing.description = item["description"]
                    existing.raw_text = item["raw_text"]
                    existing.severity = item["severity"]
                    existing.status_type = item["status_type"]
                    existing.valid_from = parse_date(item["valid_from"])
                    existing.valid_to = parse_date(item["valid_to"])
                    existing.is_active = item["is_active"]
                    existing.scraped_at = datetime.fromisoformat(item["scraped_at"])
                    db.commit()
                    skipped_count += 1
                    continue

                report = _build_report(item)
                db.add(report)
                db.commit()
                new_count += 1
            except Exception:
                db.rollback()
                error_count += 1
                logger.exception(
                    "Failed to save item %r, skipping it and continuing",
                    item.get("id"),
                )
    finally:
        db.close()

    # Brisanje na zapisi koi poveke ne se na AMSM stranacata
    scraped_ids = [item["id"] for item in items]
    db2 = SessionLocal()
    try:
        deleted = db2.query(RoadReport).filter(
            RoadReport.external_id.notin_(scraped_ids)
        ).delete(synchronize_session=False)
        db2.commit()
        logger.info("Deleted %d stale report(s) no longer on the AMSM page", deleted)
    except Exception:
        db2.rollback()
        logger.exception("Failed to delete stale reports")
    finally:
        db2.close()

    logger.info(
        "Scraping run finished: %d new, %d already existed, %d failed (out of %d parsed)",
        new_count,
        skipped_count,
        error_count,
        len(items),
    )

    return {
        "status": "ok",
        "new_count": new_count,
        "skipped_count": skipped_count,
        "error_count": error_count,
        "parsed_count": len(items),
    }