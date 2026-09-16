"""
One place to configure logging so scheduler / scraper / API logs all
look the same and actually show up in the terminal.
"""
import logging

from config import LOG_LEVEL


def configure_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # SQLAlchemy's own loggers are separate from SQL_ECHO; keep them quiet
    # unless someone explicitly wants DEBUG for everything.
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
