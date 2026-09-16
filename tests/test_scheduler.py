"""
Tests focused on the scheduler -> scraper wiring itself, since that was
the reported bug. These do not hit the network or a real database.
"""
from datetime import datetime
from unittest.mock import patch

from fastapi.testclient import TestClient


def test_scheduler_job_is_wired_to_run_scraping():
    """
    Confirms that the job registered on the scheduler in main.py's
    lifespan is literally the same function object as scraper_job.run_scraping.
    This is what a broken dependency-injection / wrong-callback bug would
    break, even if nothing raised an exception.
    """
    import config
    import main
    from scraper_job import run_scraping

    with patch.object(main.scheduler, "add_job") as mock_add_job, \
         patch.object(main.scheduler, "start"), \
         patch.object(main.scheduler, "shutdown"):
        with TestClient(main.app):
            pass

        assert mock_add_job.called, "scheduler.add_job was never called"
        args, kwargs = mock_add_job.call_args
        assert args[0] is run_scraping
        assert args[1] == "interval"
        assert kwargs.get("minutes") == config.SCRAPE_INTERVAL_MINUTES


def test_scrape_on_startup_schedules_immediate_run():
    """
    With SCRAPE_ON_STARTUP enabled, add_job must be called with a
    next_run_time in the past/now, not left to the default (which only
    fires after a full interval).
    """
    import config
    import main

    assert config.SCRAPE_ON_STARTUP is True

    with patch.object(main.scheduler, "add_job") as mock_add_job, \
         patch.object(main.scheduler, "start"), \
         patch.object(main.scheduler, "shutdown"):
        with TestClient(main.app):
            pass

        _, kwargs = mock_add_job.call_args
        assert "next_run_time" in kwargs
        assert isinstance(kwargs["next_run_time"], datetime)


def test_run_scraping_returns_summary_without_hitting_network():
    """
    run_scraping() should call fetch_html/parse_page and return a summary
    dict describing what happened -- this is what /scrape-now and the
    scheduler both rely on to be observable.
    """
    from scraper_job import run_scraping

    fake_page = {
        "source": "https://example.test",
        "scraped_at": "2026-01-01T00:00:00+00:00",
        "items_count": 0,
        "items": [],
    }

    with patch("scraper_job.fetch_html", return_value="<html></html>") as mock_fetch, \
         patch("scraper_job.parse_page", return_value=fake_page) as mock_parse:
        result = run_scraping()

    mock_fetch.assert_called_once()
    mock_parse.assert_called_once()
    assert result["status"] == "ok"
    assert result["new_count"] == 0
    assert result["parsed_count"] == 0


def test_run_scraping_one_bad_item_does_not_discard_the_others():
    """
    Regression test for the root-cause bug: previously, one item raising
    an exception during processing rolled back the *entire* batch via a
    single shared try/except around the whole loop, so nothing from that
    run was ever saved. Now each item is committed independently.
    """
    from scraper_job import run_scraping

    good_item = {
        "id": "good-1",
        "category": "NOTICE",
        "title": "Good item",
        "description": "desc",
        "raw_text": "raw",
        "status_type": "INFO",
        "severity": "GREEN",
        "valid_from": None,
        "valid_to": None,
        "is_active": True,
        "scraped_at": "2026-01-01T00:00:00+00:00",
        "source_url": "https://example.test",
    }
    # Missing required "scraped_at" key -> raises KeyError while building
    # the RoadReport, simulating a malformed item.
    bad_item = {k: v for k, v in good_item.items() if k != "scraped_at"}
    bad_item["id"] = "bad-1"

    fake_page = {
        "source": "https://example.test",
        "scraped_at": "2026-01-01T00:00:00+00:00",
        "items_count": 2,
        "items": [bad_item, good_item],
    }

    class FakeQuery:
        def filter_by(self, **kwargs):
            return self

        def first(self):
            return None

    class FakeSession:
        def __init__(self):
            self.added = []
            self.committed = []

        def query(self, *args, **kwargs):
            return FakeQuery()

        def add(self, obj):
            self.added.append(obj)

        def commit(self):
            self.committed.append(list(self.added))

        def rollback(self):
            if self.added:
                self.added.pop()

        def close(self):
            pass

    fake_session = FakeSession()

    with patch("scraper_job.fetch_html", return_value="<html></html>"), \
         patch("scraper_job.parse_page", return_value=fake_page), \
         patch("scraper_job.SessionLocal", return_value=fake_session):
        result = run_scraping()

    assert result["new_count"] == 1, "the good item should still be saved"
    assert result["error_count"] == 1, "the bad item should be counted as an error"
