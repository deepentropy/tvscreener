"""Company filings, transcripts and earnings calls listed on TradingView's symbol pages (provider: Quartr)."""
import datetime as dt

import pandas as pd
import requests

from tvscreener.news import _ast_to_text

DOCUMENTS_URL = "https://news-mediator.tradingview.com/public/doc-screener/v1/documents"
VIEW_URL = "https://news-mediator.tradingview.com/public/doc-screener/v1/views/{view_id}"
EVENTS_URL = "https://news-mediator.tradingview.com/public/doc-screener/v1/events"
REQUEST_TIMEOUT = 30
# The events endpoint rejects ranges longer than this
MAX_EVENT_RANGE_DAYS = 365

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}

DOCUMENT_CATEGORIES = ("quarterly_report", "annual_report", "interim_report", "earnings_release",
                       "call_transcript", "event_transcript", "slides")


def _to_date(value, default):
    if value is None:
        return default
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def get_documents(symbol, category=None, start=None, end=None, lang="en"):
    """
    Filings, reports and transcripts of a company: 10-Q, 10-K, earnings releases, call transcripts...

    :param symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
    :param category: Category or list of categories to keep: "quarterly_report", "annual_report",
        "interim_report", "earnings_release", "call_transcript", "event_transcript", "slides"; default all
    :param start: First day (date, datetime or ISO string); default the full history
    :param end: Last day, inclusive; default today
    :param lang: Language of the documents
    :return: DataFrame sorted from the newest, with columns: date (UTC), title, category, event
        ("earning" or "corporate_event"), fiscal_year, fiscal_period, form (e.g. "10-Q"),
        transcript_id, summary_id, pdf_id, provider, id.
        Pass ``transcript_id`` or ``summary_id`` to get_document() for the text.
    :raises ValueError: If a category is unknown
    """
    categories = [category] if isinstance(category, str) else category
    unknown = set(categories or []) - set(DOCUMENT_CATEGORIES)
    if unknown:
        raise ValueError(f"Unknown categories {sorted(unknown)}; valid: {list(DOCUMENT_CATEGORIES)}")

    # The API rejects filters that are not in alphabetical order
    params = [("client", "web"), ("filter", f"lang:{lang}"), ("filter", f"symbol:{symbol}")]
    if start is not None:
        params.append(("start_date", f"{_to_date(start, None).isoformat()}T00:00:00.000Z"))
    if end is not None:
        params.append(("end_date", f"{(_to_date(end, None) + dt.timedelta(days=1)).isoformat()}T00:00:00.000Z"))
    response = requests.get(DOCUMENTS_URL, params=params, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    rows = []
    for item in response.json().get("items") or []:
        views = {v.get("type"): v.get("id") for v in item.get("views") or []}
        rows.append({
            "date": item.get("reported"),
            "title": item.get("title"),
            "category": (item.get("category") or {}).get("id"),
            "event": item.get("event"),
            "fiscal_year": item.get("fiscal_year"),
            "fiscal_period": item.get("fiscal_period"),
            "form": (item.get("form") or {}).get("title"),
            "transcript_id": views.get("transcript"),
            "summary_id": views.get("summary"),
            "pdf_id": views.get("pdf"),
            "provider": (item.get("provider") or {}).get("name"),
            "id": item.get("id"),
        })
    columns = ["date", "title", "category", "event", "fiscal_year", "fiscal_period", "form", "transcript_id",
               "summary_id", "pdf_id", "provider", "id"]
    df = pd.DataFrame(rows, columns=columns)
    if categories:
        df = df[df["category"].isin(categories)]
    df["date"] = pd.to_datetime(df["date"], unit="s", utc=True)
    df["fiscal_year"] = df["fiscal_year"].astype("Int64")
    return df.sort_values("date", ascending=False, ignore_index=True)


def get_document(view_id):
    """
    Text of a transcript or summary listed by get_documents().

    :param view_id: ``transcript_id`` or ``summary_id`` from get_documents()
    :return: Document text, one paragraph per line block (speaker names included in transcripts)
    :raises requests.HTTPError: If the document does not exist or has no text view (PDF reports)
    """
    response = requests.get(VIEW_URL.format(view_id=view_id), headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return _ast_to_text(response.json().get("astDescription"))


def get_earnings_calls(symbol, start=None, end=None):
    """
    Earnings calls of a company, with links to their transcript and audio recording.

    :param symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
    :param start: First day (date, datetime or ISO string); default one year before ``end``
    :param end: Last day, inclusive; default 90 days from today (includes scheduled calls)
    :return: DataFrame sorted by date with columns: date (UTC), title, fiscal_year, fiscal_period,
        state ("scheduled", "live", "completed"...), transcript_url (live transcript, JSON lines),
        audio_url (recording), audio_duration (seconds), id
    """
    end_d = _to_date(end, dt.datetime.now(dt.timezone.utc).date() + dt.timedelta(days=90))
    start_d = _to_date(start, end_d - dt.timedelta(days=MAX_EVENT_RANGE_DAYS))
    if end_d < start_d:
        raise ValueError(f"end ({end_d}) is before start ({start_d})")

    items, window_start = {}, start_d
    while window_start <= end_d:
        window_end = min(window_start + dt.timedelta(days=MAX_EVENT_RANGE_DAYS - 1), end_d)
        params = [("filter", "event_type:earnings_call"), ("filter", f"symbol:{symbol}"),
                  ("start_date", window_start.isoformat()), ("end_date", window_end.isoformat())]
        response = requests.get(EVENTS_URL, params=params, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        for item in response.json().get("items") or []:
            items[item["event"]["id"]] = item
        window_start = window_end + dt.timedelta(days=1)

    rows = []
    for item in items.values():
        event, audio = item["event"], item.get("audio") or {}
        rows.append({
            "date": event.get("date"),
            "title": event.get("title"),
            "fiscal_year": event.get("fiscalYear"),
            "fiscal_period": event.get("fiscalPeriod"),
            "state": event.get("state"),
            "transcript_url": (item.get("liveTranscript") or {}).get("transcript"),
            "audio_url": audio.get("fileUrl") or (item.get("liveAudio") or {}).get("audio"),
            "audio_duration": (audio.get("audioMetadata") or {}).get("duration"),
            "id": event.get("id"),
        })
    columns = ["date", "title", "fiscal_year", "fiscal_period", "state", "transcript_url", "audio_url",
               "audio_duration", "id"]
    df = pd.DataFrame(rows, columns=columns)
    df["date"] = pd.to_datetime(df["date"], utc=True, format="ISO8601")
    df["fiscal_year"] = df["fiscal_year"].astype("Int64")
    return df.sort_values("date", ignore_index=True)
