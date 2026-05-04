from database import SessionLocal
from models import RoadReport

db = SessionLocal()

reports = db.query(RoadReport).all()

for report in reports:
    print(report.id, report.title, report.severity)

db.close()