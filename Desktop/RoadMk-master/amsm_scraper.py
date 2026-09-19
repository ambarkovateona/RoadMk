import hashlib
import json
import logging
import re
import time
from datetime import date, datetime, timezone

import requests
from bs4 import BeautifulSoup

from config import (
    REQUEST_MAX_RETRIES,
    REQUEST_RETRY_BACKOFF_SECONDS,
    REQUEST_TIMEOUT_SECONDS,
    SCRAPE_URL,
)

logger = logging.getLogger("roadmk.scraper")

# Kept as an alias so existing imports of `URL` keep working.
URL = SCRAPE_URL


def fetch_html(url: str) -> str:
    """
    Fetch a page with a couple of retries. AMSM occasionally times out or
    briefly returns 5xx -- without a retry, a single bad request used to
    mean the whole scheduled run silently produced nothing until the next
    interval fired.
    """
    headers = {
        "User-Agent": "RoadScraper/1.0 (student project)"
    }

    last_error: Exception | None = None
    for attempt in range(1, REQUEST_MAX_RETRIES + 1):
        try:
            logger.info("Fetching %s (attempt %d/%d)", url, attempt, REQUEST_MAX_RETRIES)
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT_SECONDS)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            last_error = e
            logger.warning("Fetch attempt %d/%d failed: %s", attempt, REQUEST_MAX_RETRIES, e)
            if attempt < REQUEST_MAX_RETRIES:
                time.sleep(REQUEST_RETRY_BACKOFF_SECONDS * attempt)

    assert last_error is not None
    raise last_error


def clean_text(s: str) -> str:
    return " ".join(s.replace("\xa0", " ").split())


def normalize_category(raw_category: str) -> str:
    c = raw_category.strip().upper()

    mapping = {
        "ИЗВЕСТУВАЊЕ": "NOTICE",
        "СОСТОЈБА": "ROAD_STATE",
        "ЗИМСКА ОПРЕМА": "WINTER_EQUIPMENT",
        "ФРЕКВЕНЦИЈА": "TRAFFIC_FREQUENCY",
        "ВНИМАТЕЛНО": "WARNING",
        "СЕЗОНСКИ РЕЖИМ НА СООБРАЌАЈ": "SEASONAL_TRAFFIC_REGIME",
        "СЕЗОНСКИ РЕЖИМ": "SEASONAL_TRAFFIC_REGIME",
        "РАБОТИ НА ПАТ": "ROAD_WORKS",
        "SECTION": "ROAD_SECTION"
    }

    return mapping.get(c, c)


def severity_from_text(text: str) -> str:
    t = text.lower()

    red_keywords = [
        "затвор", "забран", "прекин", "целосно затворање", "не се одвива"
    ]
    yellow_keywords = [
        "отежнат", "девија", "лизгав", "снег", "одрон", "магла",
        "времена измена", "измена на режим", "градежни работи",
        "пренасочен", "внимателно", "намалена видливост"
    ]

    if any(word in t for word in red_keywords):
        return "RED"
    if any(word in t for word in yellow_keywords):
        return "YELLOW"
    return "GREEN"


def status_type_from_text(text: str) -> str:
    t = text.lower()

    if any(word in t for word in ["затвор", "затвора", "целосно затворање"]):
        return "CLOSURE"
    if any(word in t for word in ["забран", "прекин"]):
        return "RESTRICTION"
    if any(word in t for word in ["девија", "пренасоч", "времена измена", "измена на режим"]):
        return "DETOUR"
    if any(word in t for word in ["градежни работи", "работи на пат", "санација", "изведување на градежни активности"]):
        return "ROAD_WORKS"
    if any(word in t for word in ["снег", "магла", "лизгав", "одрон"]):
        return "WEATHER_WARNING"
    if "зимска опрема" in t:
        return "WINTER_EQUIPMENT"
    return "INFO"


def make_item_id(category: str, title: str, raw_text: str) -> str:
    raw = f"{category}|{title}|{raw_text}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def parse_date_string(date_str: str) -> str | None:
    """
    Претвора дд.мм.гггг или дд/мм.гггг во ISO date (YYYY-MM-DD).
    Ако не може да се парсира, враќа None.
    """
    cleaned = date_str.replace("/", ".")
    match = re.match(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", cleaned)
    if not match:
        return None

    day, month, year = map(int, match.groups())

    try:
        parsed = date(year, month, day)
        return parsed.isoformat()
    except ValueError:
        return None


def extract_validity_dates(text: str) -> tuple[str | None, str | None]:
    """
    Бара шаблони:
    - од 21.11.2025 до 31.03.2026
    - од 16.12.2024 год. па се до ...
    - од 15.11.2025 година ... до 15.03.2026 година
    """
    normalized = text.replace("/", ".")
    matches = re.findall(r"(\d{1,2}\.\d{1,2}\.\d{4})", normalized)

    if not matches:
        return None, None

    valid_from = parse_date_string(matches[0])
    valid_to = parse_date_string(matches[1]) if len(matches) > 1 else None

    return valid_from, valid_to


def extract_description(text: str, category_label: str) -> str:
    """
    Ако текстот почнува со 'ИЗВЕСТУВАЊЕ:' или слично,
    го трга префиксот за да имаш почист description.
    """
    prefix = f"{category_label}:"
    if text.startswith(prefix):
        return text[len(prefix):].strip()
    return text.strip()


def is_active_from_dates(valid_from: str | None, valid_to: str | None) -> bool:
    today = date.today()

    if valid_from:
        try:
            if today < date.fromisoformat(valid_from):
                return False
        except ValueError:
            pass

    if valid_to:
        try:
            if today > date.fromisoformat(valid_to):
                return False
        except ValueError:
            pass

    return True


def build_item(
    category_label: str,
    title: str,
    raw_text: str,
    scraped_at: str,
    source_url: str
) -> dict:
    normalized_category = normalize_category(category_label)
    description = extract_description(raw_text, category_label)
    valid_from, valid_to = extract_validity_dates(raw_text)
    status_type = status_type_from_text(raw_text)
    severity = severity_from_text(raw_text)
    is_active = is_active_from_dates(valid_from, valid_to)

    return {
        "id": make_item_id(normalized_category, title, raw_text),
        "category": normalized_category,
        "title": title,
        "description": description,
        "raw_text": raw_text,
        "status_type": status_type,
        "severity": severity,
        "valid_from": valid_from,
        "valid_to": valid_to,
        "is_active": is_active,
        "scraped_at": scraped_at,
        "source_url": source_url
    }


def parse_general_sections(article, scraped_at: str, source_url: str) -> list[dict]:
    items = []

    general_prefixes = [
        "ИЗВЕСТУВАЊЕ:",
        "СОСТОЈБА:",
        "ЗИМСКА ОПРЕМА:",
        "ФРЕКВЕНЦИЈА:",
        "ВНИМАТЕЛНО:",
        "СЕЗОНСКИ РЕЖИМ"
    ]

    for tag in article.find_all(["p", "h3", "h4"]):
        text = clean_text(tag.get_text(" ", strip=True))
        if not text:
            continue

        if any(text.startswith(prefix) for prefix in general_prefixes):
            category_label = text.split(":", 1)[0].strip() if ":" in text else text.strip()
            title = category_label

            items.append(
                build_item(
                    category_label=category_label,
                    title=title,
                    raw_text=text,
                    scraped_at=scraped_at,
                    source_url=source_url
                )
            )

    return items


def parse_road_works(article, scraped_at: str, source_url: str) -> list[dict]:
    items = []

    for tag in article.find_all(["p", "h3", "h4"]):
        t = clean_text(tag.get_text(" ", strip=True))
        if t.startswith("РАБОТИ НА ПАТ"):
            ul = tag.find_next("ul")
            if ul:
                for li in ul.find_all("li", recursive=False):
                    li_text = clean_text(li.get_text(" ", strip=True))
                    if not li_text:
                        continue

                    items.append(
                        build_item(
                            category_label="РАБОТИ НА ПАТ",
                            title="Работи на пат",
                            raw_text=li_text,
                            scraped_at=scraped_at,
                            source_url=source_url
                        )
                    )
            break

    return items


def parse_section_blocks(article, scraped_at: str, source_url: str) -> list[dict]:
    items = []

    for heading in article.find_all(["h4", "h5"]):
        title = clean_text(heading.get_text(" ", strip=True))
        if not title or len(title) < 4:
            continue

        texts = []
        node = heading.find_next_sibling()

        while node and getattr(node, "name", None) not in ["h3", "h4", "h5"]:
            if getattr(node, "name", None) in ["p", "div"]:
                t = clean_text(node.get_text(" ", strip=True))
                if t:
                    texts.append(t)

            node = node.find_next_sibling()

            if len(texts) >= 3:
                break

        if texts:
            full_text = " ".join(texts)

            items.append(
                build_item(
                    category_label="SECTION",
                    title=title,
                    raw_text=full_text,
                    scraped_at=scraped_at,
                    source_url=source_url
                )
            )

    return items


def deduplicate_items(items: list[dict]) -> list[dict]:
    unique = {}
    for item in items:
        unique[item["id"]] = item
    return list(unique.values())


def parse_page(html: str, source_url: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup
    if article is soup:
        logger.warning(
            "No <article> tag found on the page; falling back to parsing the "
            "whole document. This usually means AMSM changed the page layout."
        )
    scraped_at = datetime.now(timezone.utc).isoformat()

    items = []
    for parser_name, parser_fn in (
        ("general_sections", parse_general_sections),
        ("road_works", parse_road_works),
        ("section_blocks", parse_section_blocks),
    ):
        try:
            found = parser_fn(article, scraped_at, source_url)
            logger.info("%s: found %d item(s)", parser_name, len(found))
            items.extend(found)
        except Exception:
            # One parsing strategy failing (e.g. AMSM tweaked markup for
            # just one section) should not take the other two down with it.
            logger.exception("Parser '%s' raised an exception, skipping it", parser_name)

    items = deduplicate_items(items)

    if not items:
        logger.warning(
            "Parsed 0 items from %s. The page structure may have changed, "
            "or there genuinely are no active notices right now.",
            source_url,
        )

    return {
        "source": source_url,
        "scraped_at": scraped_at,
        "items_count": len(items),
        "items": items
    }


def main():
    try:
        html = fetch_html(URL)
        data = parse_page(html, URL)

        with open("amsm_dnevni_informacii.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"Saved {data['items_count']} items to amsm_dnevni_informacii.json")

    except requests.RequestException as e:
        print(f"HTTP error while fetching page: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()