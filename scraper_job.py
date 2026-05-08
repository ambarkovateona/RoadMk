from proba import fetch_html, parse_page, URL
from database import SessionLocal
from models import RoadReport
from datetime import datetime
import json


def parse_date(value):
    if not value:
        return None
    from datetime import date
    return date.fromisoformat(value)


def run_scraping():
    print(f"[{datetime.now()}] Starting scraping...")
    try:
        html = fetch_html(URL)
        data = parse_page(html, URL)

        db = SessionLocal()
        new_count = 0

        try:
            for item in data["items"]:
                existing = db.query(RoadReport).filter_by(external_id=item["id"]).first()
                if existing:
                    continue

                report = RoadReport(
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
                    source_url=item["source_url"]
                )
                db.add(report)
                new_count += 1

            db.commit()
            print(f"[{datetime.now()}] Scraping done. {new_count} new reports added.")

        except Exception as e:
            db.rollback()
            print(f"[{datetime.now()}] DB error: {e}")
        finally:
            db.close()

    except Exception as e:
        print(f"[{datetime.now()}] Scraping error: {e}")
