import json
from datetime import datetime

from database import SessionLocal
from models import RoadReport


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def parse_datetime(value):
    return datetime.fromisoformat(value)


def insert_reports_from_json(json_file: str):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = SessionLocal()

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
                scraped_at=parse_datetime(item["scraped_at"]),
                source_url=item["source_url"]
            )

            db.add(report)

        db.commit()
        print("Reports inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error inserting reports: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    insert_reports_from_json("amsm_dnevni_informacii.json")