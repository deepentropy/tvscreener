"""Financial statements, corporate events and seasonals, read from TradingView's data websocket."""
import base64
import collections
import datetime as dt
import functools
import json
import zlib

import pandas as pd
import requests

from tvscreener._websocket import NA, get_quote_fields, run_studies

FUNDAMENTALS_CONFIG_URL = "https://www.tradingview.com/financial/fundamentals_config_v2/"
REQUEST_TIMEOUT = 60
# Fields per quote request
FIELD_BATCH = 1000

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}

STATEMENTS = {
    "income": "Income statements",
    "balance_sheet": "Balance sheet",
    "cash_flow": "Cash flow",
    "statistics": "Statistics",
}
PERIODS = ("FY", "FQ", "FH", "TTM")
# TTM values are reported at each quarter end
_PERIOD_LABELS = {"FY": "fy", "FQ": "fq", "FH": "fh", "TTM": "fq"}

EVENT_STUDIES = {
    "dividends": "Dividends@tv-basicstudies-279",
    "earnings": "Earnings@tv-basicstudies-279",
    "splits": "Splits@tv-basicstudies-279",
}
SEASONALS_STUDY = "Seasonals@tv-basicstudies-279"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


@functools.lru_cache(maxsize=1)
def get_fundamentals_config():
    """
    TradingView's catalogue of fundamental fields (cached).

    :return: DataFrame with columns: id, name, category, period, view_mode, parent, ordinal, type, hidden.
        A field id appears once per ``view_mode`` (statement layout: "industrial", "banking",
        "insurance", "other"...).
    """
    response = requests.get(FUNDAMENTALS_CONFIG_URL, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return pd.DataFrame([{
        "id": item.get("id"),
        "name": item.get("name"),
        "category": item.get("category"),
        "period": item.get("period"),
        "view_mode": item.get("fundViewMode"),
        "parent": item.get("parent"),
        "ordinal": item.get("ordinal"),
        "type": item.get("type"),
        "hidden": bool(item.get("hidden")),
    } for item in response.json()])


def _clean(value):
    return None if value is None or value == NA else value


def get_financials(symbol, statement="income", period="FY", labels=True):
    """
    Financial statement history of a company, as shown on TradingView's financials pages.

    About 20 fiscal years and 32 quarters are available for large companies.

    :param symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
    :param statement: "income", "balance_sheet", "cash_flow" or "statistics" (ratios, per-share values...)
    :param period: "FY" (annual), "FQ" (quarterly), "FH" (semi-annual) or "TTM" (trailing twelve months,
        at each quarter end)
    :param labels: True for readable column names ("Total revenue"), False for field ids ("total_revenue")
    :return: DataFrame with one row per fiscal period, oldest first, indexed by the period label
        ("2025", "2026-Q3"). The first column is ``period_end`` (UTC); the other columns are the
        statement items, in TradingView's order. Items without data are left out.
        ``df.attrs["currency"]`` is the reporting currency.
    :raises ValueError: If ``statement`` or ``period`` is invalid, or the symbol is unknown
    """
    if statement not in STATEMENTS:
        raise ValueError(f"statement must be one of {list(STATEMENTS)}, got {statement!r}")
    period = period.upper()
    if period not in PERIODS:
        raise ValueError(f"period must be one of {list(PERIODS)}, got {period!r}")

    config = get_fundamentals_config()
    items = config[(config["category"] == STATEMENTS[statement]) & (config["period"] == period) & ~config["hidden"]]
    label_suffix = _PERIOD_LABELS[period]
    meta = [f"fiscal_period_{label_suffix}_h", f"fiscal_period_end_{label_suffix}_h", "fundamental_currency_code"]
    fields = sorted({f"{i}_h" for i in items["id"]})

    values = {}
    for start in range(0, len(fields), FIELD_BATCH):
        batch = fields[start:start + FIELD_BATCH] + meta
        result = get_quote_fields([symbol], batch).get(symbol)
        if result is None:
            raise ValueError(f"Unknown symbol {symbol}")
        values.update(result)
    filled = {k[:-2] for k, v in values.items() if k.endswith("_h") and isinstance(v, list) and any(
        _clean(x) is not None for x in v)} - {m[:-2] for m in meta}

    # Each company type (industrial, banking, insurance...) has its own layout: keep the most complete one
    sizes = items.groupby("view_mode")["id"].count()
    found = items[items["id"].isin(filled)].groupby("view_mode")["id"].count()
    if found.empty:
        return pd.DataFrame(columns=["period_end"])
    mode = (found / sizes[found.index]).idxmax()
    layout = _statement_order(items[items["view_mode"] == mode])
    layout = layout[layout["id"].isin(filled)]

    period_labels = list(values.get(meta[0]) or [])
    period_ends = list(values.get(meta[1]) or [])
    n = len(period_labels) or max(len(values[f"{i}_h"]) for i in layout["id"])
    if not period_labels:
        period_labels = [None] * n
    columns = {}
    for field_id, name in zip(layout["id"], layout["name"]):
        series = [_clean(x) for x in values[f"{field_id}_h"][:n]]
        key = name if labels else field_id.rsplit("_", 1)[0]
        if key in columns:
            key = f"{key} ({field_id})"
        columns[key] = series + [None] * (n - len(series))
    df = pd.DataFrame(columns, index=pd.Index([str(p) if p is not None else None for p in period_labels],
                                              name="period"))
    df.insert(0, "period_end", pd.to_datetime((period_ends + [None] * n)[:n], unit="s", utc=True))
    df = df.iloc[::-1]
    df.attrs["currency"] = values.get("fundamental_currency_code")
    return df


def _statement_order(layout):
    """Rows in display order: each item followed by its sub-items, siblings by ordinal."""
    ids = set(layout["id"])
    children = collections.defaultdict(list)
    for row in layout.itertuples():
        children[row.parent if row.parent in ids else None].append(row)
    order = []

    def visit(parent):
        for row in sorted(children[parent], key=lambda r: (r.ordinal is None, r.ordinal)):
            order.append(row.Index)
            visit(row.id)

    visit(None)
    return layout.loc[order]


def _ms(series):
    return pd.to_datetime(series, unit="ms", utc=True)


def _event_frame(rows, columns):
    df = pd.DataFrame([[_clean(x) for x in row[:len(columns)]] for row in rows], columns=columns)
    return df.apply(pd.to_numeric)


def get_corporate_events(symbol, kinds=("dividends", "earnings", "splits")):
    """
    Past and upcoming dividends, earnings releases and stock splits of a company.

    TradingView serves recent history only (logged out): about 20 dividends, the last
    2 years of earnings, and recent splits.

    :param symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
    :param kinds: Event kinds to fetch, among "dividends", "earnings", "splits"
    :return: Dict of kind to DataFrame:

        - dividends: ex_date, payment_date (UTC), amount (gross), net_amount
        - earnings: date (release, UTC), fiscal_period_end, reported (bool), eps_reported (EPS comparable
          to the estimate), eps_estimate, eps_diluted (diluted EPS from the income statement),
          revenue_actual, revenue_estimate
        - splits: date (UTC), numerator, denominator, ratio (numerator / denominator; 10 for a 10-for-1 split)
    :raises ValueError: If a kind is unknown
    :raises TradingViewWebSocketError: If the symbol is unknown
    """
    kinds = [kinds] if isinstance(kinds, str) else list(kinds)
    unknown = set(kinds) - set(EVENT_STUDIES)
    if unknown:
        raise ValueError(f"Unknown kinds {sorted(unknown)}; valid: {list(EVENT_STUDIES)}")
    results = run_studies(symbol, {k: (EVENT_STUDIES[k], {"currenttime": "now"}) for k in kinds}, bars=3000)

    events = {}
    if "dividends" in results:
        raw = _event_frame(results["dividends"]["rows"], ["time", "gross", "ex_date", "net", "payment_date"])
        events["dividends"] = pd.DataFrame({
            "ex_date": _ms(raw["ex_date"]),
            "payment_date": _ms(raw["payment_date"]),
            "amount": raw["gross"],
            "net_amount": raw["net"],
        }).sort_values("ex_date", ignore_index=True)
    if "earnings" in results:
        raw = _event_frame(results["earnings"]["rows"],
                           ["time", "actual", "estimate", "fiscal_date", "release", "reported", "revenue_estimate",
                            "revenue_actual"])
        events["earnings"] = pd.DataFrame({
            "date": _ms(raw["release"]),
            "fiscal_period_end": pd.to_datetime(raw["fiscal_date"], unit="s", utc=True),
            "reported": raw["reported"].notna() | raw["actual"].notna(),
            "eps_reported": raw["reported"],
            "eps_estimate": raw["estimate"],
            "eps_diluted": raw["actual"],
            # Revenues are sent in millions
            "revenue_actual": raw["revenue_actual"] * 1e6,
            "revenue_estimate": raw["revenue_estimate"] * 1e6,
        }).sort_values("date", ignore_index=True)
    if "splits" in results:
        raw = _event_frame(results["splits"]["rows"], ["time", "denominator", "numerator", "date"])
        events["splits"] = pd.DataFrame({
            "date": _ms(raw["date"]),
            "numerator": raw["numerator"],
            "denominator": raw["denominator"],
            "ratio": raw["numerator"] / raw["denominator"],
        }).sort_values("date", ignore_index=True)
    return events


def _decode_graphics(graphics):
    data = json.loads(graphics) if isinstance(graphics, str) else graphics
    if "dataCompressed" in data:
        packed = data["dataCompressed"]
        data = json.loads(zlib.decompress(base64.b64decode(packed + "=" * (-len(packed) % 4))))
    return data.get("data", data)


def get_seasonals(symbol, start_year=None, end_year=None, absolute=False):
    """
    Monthly returns of a symbol, one row per year, as on TradingView's seasonals page.

    :param symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL", "BINANCE:BTCUSDT"
    :param start_year: First year; default 9 years before ``end_year``
    :param end_year: Last year; default the current year
    :param absolute: False for percent changes, True for price changes
    :return: DataFrame indexed by year (oldest first) with columns Jan..Dec. Months not reached yet are NaN.
    :raises TradingViewWebSocketError: If the symbol is unknown
    """
    end_year = end_year or dt.datetime.now(dt.timezone.utc).year
    start_year = start_year or end_year - 9
    if end_year < start_year:
        raise ValueError(f"end_year ({end_year}) is before start_year ({start_year})")
    config = json.dumps({"ticker": symbol, "years": {"start": start_year, "end": end_year}})
    result = run_studies(symbol, {"seasonals": (SEASONALS_STUDY, {"config": config})}, bars=300)["seasonals"]
    performance = _decode_graphics(result["graphics"]).get("performance", {}) if result["graphics"] else {}

    position = 0 if absolute else 1
    rows = {}
    for year, data in performance.items():
        months = [m[position] if m else None for m in data.get("months", [])]
        rows[int(year)] = (months + [None] * 12)[:12]
    df = pd.DataFrame.from_dict(rows, orient="index", columns=MONTHS, dtype=float).sort_index()
    df.index.name = "year"
    return df
