from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean
from datetime import datetime, timezone

from database import Base


class RoadReport(Base):
    __tablename__ = "road_reports"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String(40), unique=True, nullable=False, index=True)

    category = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    raw_text = Column(Text, nullable=False)

    status_type = Column(String(100), nullable=False)
    severity = Column(String(20), nullable=False)

    valid_from = Column(Date, nullable=True)
    valid_to = Column(Date, nullable=True)

    is_active = Column(Boolean, nullable=False, default=True)

    scraped_at = Column(DateTime(timezone=True), nullable=False)
    source_url = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)