"""Earnings, dividends and IPO calendars, built on the same scanner queries as TradingView's calendar pages."""
import datetime as dt
import json

import pandas as pd
import requests

from tvscreener.field import Market

SCAN_URL = "https://scanner.tradingview.com/global/scan"
REQUEST_TIMEOUT = 60
PAGE_SIZE = 5000

REQUEST_HEADERS = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}

# earnings_release_time codes, checked on companies with known reporting times
RELEASE_TIMES = {-1: "before_open", 1: "after_close", 0: "unspecified"}


def _to_date(value):
    if value is None:
        return dt.datetime.now(dt.timezone.utc).date()
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def _range(start, end):
    """UTC timestamps from the start of ``start`` to the end of ``end`` (inclusive)."""
    start_d, end_d = _to_date(start), _to_date(end)
    if end_d < start_d:
        raise ValueError(f"end ({end_d}) is before start ({start_d})")
    t0 = dt.datetime.combine(start_d, dt.time(), tzinfo=dt.timezone.utc).timestamp()
    t1 = dt.datetime.combine(end_d + dt.timedelta(days=1), dt.time(), tzinfo=dt.timezone.utc).timestamp() - 0.001
    return t0, t1


def _markets(markets):
    if markets is None:
        return [Market.AMERICA.value]
    if isinstance(markets, (str, Market)):
        markets = [markets]
    values = []
    for m in markets:
        if m is Market.ALL or m == "ALL":
            return [x.value for x in Market if x is not Market.ALL]
        values.append(m.value if isinstance(m, Market) else m)
    return values


def _scan(columns, filters, markets, sort=None, preset=None):
    """Run the query and return (symbols, rows), following pages until totalCount."""
    payload = {"columns": columns, "filter": filters, "markets": markets, "options": {"lang": "en"}}
    if sort:
        payload["sort"] = sort
    if preset:
        payload["preset"] = preset
    symbols, rows, start = [], [], 0
    while True:
        payload["range"] = [start, start + PAGE_SIZE]
        response = requests.post(SCAN_URL, data=json.dumps(payload), headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        result = response.json()
        data = result.get("data") or []
        symbols += [d["s"] for d in data]
        rows += [d["d"] for d in data]
        start += PAGE_SIZE
        if not data or start >= result.get("totalCount", 0):
            return symbols, rows


def _utc(series):
    return pd.to_datetime(series, unit="s", utc=True)


def get_earnings_calendar(start=None, end=None, markets=None):
    """
    Companies reporting earnings between two dates.

    Each row is one earnings release in the period: already reported (with actual
    values and surprise) or upcoming (estimates only).

    :param start: First day (date, datetime or ISO string); default today
    :param end: Last day, inclusive; default ``start``
    :param markets: Market, market name or list of them; default Market.AMERICA. Market.ALL for every market.
    :return: DataFrame with columns: symbol, name, description, market, date (UTC), time
        ("before_open", "after_close", "unspecified"), reported, eps_estimate, eps_actual,
        eps_surprise, eps_surprise_pct, revenue_estimate, revenue_actual, revenue_surprise,
        revenue_surprise_pct, market_cap, currency.
        Values are in ``currency`` (USD unless the markets report in another currency).
    """
    t0, t1 = _range(start, end if end is not None else start)
    columns = ["name", "description", "market", "earnings_release_date", "earnings_release_next_date",
               "earnings_release_time", "earnings_release_next_time",
               "earnings_per_share_fq", "earnings_per_share_forecast_fq", "earnings_per_share_forecast_next_fq",
               "eps_surprise_fq", "eps_surprise_percent_fq",
               "revenue_fq", "revenue_forecast_fq", "revenue_forecast_next_fq",
               "revenue_surprise_fq", "revenue_surprise_percent_fq",
               "market_cap_basic", "fundamental_currency_code"]
    filters = [{"left": "earnings_release_date,earnings_release_next_date", "operation": "in_range", "right": [t0, t1]}]
    symbols, rows = _scan(columns, filters, _markets(markets))
    raw = pd.DataFrame(rows, columns=columns)

    # The release in the period is the last one when it falls in range, otherwise the next one
    reported = raw["earnings_release_date"].between(t0, t1)
    pick = lambda last, upcoming: raw[last].where(reported, raw[upcoming])
    actual_only = lambda column: raw[column].where(reported)

    df = pd.DataFrame({
        "symbol": symbols,
        "name": raw["name"],
        "description": raw["description"],
        "market": raw["market"],
        "date": _utc(pick("earnings_release_date", "earnings_release_next_date")),
        "time": pick("earnings_release_time", "earnings_release_next_time").map(RELEASE_TIMES),
        "reported": reported,
        "eps_estimate": pick("earnings_per_share_forecast_fq", "earnings_per_share_forecast_next_fq"),
        "eps_actual": actual_only("earnings_per_share_fq"),
        "eps_surprise": actual_only("eps_surprise_fq"),
        "eps_surprise_pct": actual_only("eps_surprise_percent_fq"),
        "revenue_estimate": pick("revenue_forecast_fq", "revenue_forecast_next_fq"),
        "revenue_actual": actual_only("revenue_fq"),
        "revenue_surprise": actual_only("revenue_surprise_fq"),
        "revenue_surprise_pct": actual_only("revenue_surprise_percent_fq"),
        "market_cap": raw["market_cap_basic"],
        "currency": raw["fundamental_currency_code"],
    })
    return df.sort_values(["date", "market_cap"], ascending=[True, False], ignore_index=True)


def get_dividends_calendar(start=None, end=None, markets=None):
    """
    Dividends with an ex-dividend date between two dates.

    :param start: First day (date, datetime or ISO string); default today
    :param end: Last day, inclusive; default ``start``
    :param markets: Market, market name or list of them; default Market.AMERICA. Market.ALL for every market.
    :return: DataFrame with columns: symbol, name, description, market, ex_date (UTC),
        payment_date (UTC), amount, dividend_yield (%), currency
    """
    t0, t1 = _range(start, end if end is not None else start)
    columns = ["name", "description", "market", "dividend_ex_date_recent", "dividend_ex_date_upcoming",
               "dividend_payment_date_recent", "dividend_payment_date_upcoming",
               "dividend_amount_recent", "dividend_amount_upcoming", "dividends_yield", "fundamental_currency_code"]
    filters = [{"left": "dividend_ex_date_recent,dividend_ex_date_upcoming", "operation": "in_range", "right": [t0, t1]}]
    symbols, rows = _scan(columns, filters, _markets(markets))
    raw = pd.DataFrame(rows, columns=columns)

    recent = raw["dividend_ex_date_recent"].between(t0, t1)
    pick = lambda last, upcoming: raw[last].where(recent, raw[upcoming])
    df = pd.DataFrame({
        "symbol": symbols,
        "name": raw["name"],
        "description": raw["description"],
        "market": raw["market"],
        "ex_date": _utc(pick("dividend_ex_date_recent", "dividend_ex_date_upcoming")),
        "payment_date": _utc(pick("dividend_payment_date_recent", "dividend_payment_date_upcoming")),
        "amount": pick("dividend_amount_recent", "dividend_amount_upcoming"),
        "dividend_yield": raw["dividends_yield"],
        "currency": raw["fundamental_currency_code"],
    })
    return df.sort_values(["ex_date", "symbol"], ignore_index=True)


def get_ipo_calendar(start=None, end=None, markets=None):
    """
    IPOs offered between two dates.

    :param start: First day (date, datetime or ISO string); default today
    :param end: Last day, inclusive; default ``start``
    :param markets: Market, market name or list of them; default Market.AMERICA. Market.ALL for every market.
    :return: DataFrame with columns: symbol, name, description, exchange, market, date (UTC),
        status, offer_price, price_range, offered_shares, deal_amount, market_cap (USD values)
    """
    t0, t1 = _range(start, end if end is not None else start)
    columns = ["name", "description", "exchange", "market", "ipo_offer_time", "ipo_offer_status",
               "ipo_offer_price_usd", "ipo_price_range_usd", "ipo_offered_shares", "ipo_deal_amount_usd",
               "ipo_market_cap_usd"]
    filters = [{"left": "ipo_offer_time", "operation": "in_range", "right": [t0, t1]},
               {"left": "ipo_offer_time", "operation": "nempty"}]
    symbols, rows = _scan(columns, filters, _markets(markets),
                          sort={"sortBy": "ipo_offer_time", "sortOrder": "asc"}, preset="ipo_calendar")
    raw = pd.DataFrame(rows, columns=columns)
    return pd.DataFrame({
        "symbol": symbols,
        "name": raw["name"],
        "description": raw["description"],
        "exchange": raw["exchange"],
        "market": raw["market"],
        "date": _utc(raw["ipo_offer_time"]),
        "status": raw["ipo_offer_status"],
        "offer_price": raw["ipo_offer_price_usd"],
        "price_range": raw["ipo_price_range_usd"],
        "offered_shares": raw["ipo_offered_shares"],
        "deal_amount": raw["ipo_deal_amount_usd"],
        "market_cap": raw["ipo_market_cap_usd"],
    })
