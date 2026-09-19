"""
Central configuration for the RoadMk backend.
All values can be overridden with environment variables (see .env.example).
Keeping them in one place makes it obvious what needs to be set for
local dev, Docker and production, instead of hardcoded values scattered
across database.py, main.py, etc.
"""
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://amsm_user:amsm_pass@localhost:5434/amsm_db",
)

# Log every SQL statement. Keep this off by default -- it was hardcoded
# to True before, which drowns real application logs (including the
# scheduler/scraper logs) in SQL noise.
SQL_ECHO = os.getenv("SQL_ECHO", "false").lower() == "true"

SCRAPE_URL = os.getenv(
    "SCRAPE_URL",
    "https://amsm.mk/sostojba-na-patishta/dnevni-informacii/",
)

SCRAPE_INTERVAL_MINUTES = int(os.getenv("SCRAPE_INTERVAL_MINUTES", "30"))

# Run scraping immediately on startup instead of waiting for the first
# interval to elapse. This was the main reason the scheduler "looked"
# like it wasn't working: with only an interval trigger and no
# next_run_time, nothing happens (and nothing is logged) for the first
# 30 minutes after the app starts.
SCRAPE_ON_STARTUP = os.getenv("SCRAPE_ON_STARTUP", "true").lower() == "true"

CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "20"))
REQUEST_MAX_RETRIES = int(os.getenv("REQUEST_MAX_RETRIES", "3"))
REQUEST_RETRY_BACKOFF_SECONDS = float(os.getenv("REQUEST_RETRY_BACKOFF_SECONDS", "2"))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
