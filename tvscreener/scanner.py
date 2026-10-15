"""Helpers for the TradingView scanner endpoints that are not screener queries, and symbol search."""
import json

import pandas as pd
import requests

SCANNER_URL = "https://scanner.tradingview.com"
SYMBOL_SEARCH_URL = "https://symbol-search.tradingview.com/symbol_search/v3/"
REQUEST_TIMEOUT = 30
SEARCH_PAGE_SIZE = 50

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}


def _field_name(field):
    return field.field_name if hasattr(field, 'field_name') else str(field)


def get_symbol(symbol, *fields):
    """
    Get any fields of one symbol.

    :param symbol: Exchange-prefixed symbol (e.g. "NASDAQ:AAPL", "BINANCE:BTCUSDT")
    :param fields: Field enums (with or without interval/history) or API field names
    :return: Dict of API field name to value, or None if the symbol does not exist.
        Unknown field names return None values.
    :raises ValueError: If no field is given

    Example:
        >>> get_symbol("NASDAQ:AAPL", StockField.PRICE, StockField.MARKET_CAPITALIZATION, "earnings_fq_h")
    """
    if not fields:
        raise ValueError("get_symbol() needs at least one field")
    response = requests.get(
        f"{SCANNER_URL}/symbol",
        params={"symbol": symbol, "fields": ",".join(_field_name(f) for f in fields), "no_404": "true"},
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def get_enum_values(*ids, lang="en"):
    """
    Get the valid values of enumerable fields (sector, industry, exchange, country, ETF issuer...).

    :param ids: Field ids, e.g. "sector", "industry", "exchange", "country", "issuer", "asset_class"
    :param lang: Language of the display names
    :return: Dict of field id to {value: display name}, in TradingView's order.
        The value is what filters expect; unknown ids are omitted.
    :raises ValueError: If no id is given

    Example:
        >>> get_enum_values("sector")["sector"]["Electronic Technology"]
        'Electronic technology'
    """
    if not ids:
        raise ValueError("get_enum_values() needs at least one id")
    response = requests.get(
        f"{SCANNER_URL}/enum/ordered",
        params={"id": ",".join(ids), "lang": lang},
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    return {key: {v["id"]: v["name"] for v in values} for key, values in response.json().items()}


def get_metainfo(market):
    """
    Get the field catalogue of a scanner market.

    The catalogue is partly generic: it can list fields that hold no data for this market.

    :param market: Scanner market, e.g. "america", "crypto", "forex", "bond", "futures", "coin",
        "economics2", "cfd", "bonds"
    :return: DataFrame with columns: name, type, values (allowed values, or None)
    """
    response = requests.post(
        f"{SCANNER_URL}/{market}/metainfo",
        data="{}",
        headers={**REQUEST_HEADERS, 'Content-Type': 'application/json'},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    fields = response.json().get("fields", [])
    return pd.DataFrame(
        [{"name": f["n"], "type": f.get("t"), "values": f.get("r")} for f in fields],
        columns=["name", "type", "values"],
    )


def _search_ticker(item):
    """Full ticker of a search result. Futures are returned as their root (e.g. "CME_MINI:ES")."""
    prefix = item.get("prefix") or (item.get("source_id") if item.get("type") == "futures" else None)
    return f"{prefix or item.get('exchange')}:{item.get('symbol')}"


def search_symbols(text, type=None, exchange=None, country=None, limit=50, lang="en"):
    """
    Search TradingView symbols by ticker, name, ISIN or CUSIP, like the website's search box.

    :param text: Search text, e.g. "AAPL", "apple", "US0378331005"
    :param type: Asset type: "stock", "funds", "futures", "forex", "crypto", "index", "bond", "economic";
        default all types
    :param exchange: Exchange to search in, e.g. "NASDAQ", "XETR"
    :param country: ISO country code that ranks the listings of that country first, e.g. "DE"
    :param limit: Maximum number of results (50 per request)
    :param lang: Language of the descriptions
    :return: DataFrame with columns: symbol (exchange-prefixed), ticker, description, type, exchange,
        currency, country, isin, cusip, typespecs, is_primary_listing.
        Futures are returned as their root (e.g. "CME_MINI:ES"), usable with get_forward_curve().
    """
    params = {"text": text, "hl": "0", "lang": lang, "domain": "production"}
    if type:
        params["search_type"] = type
    if exchange:
        params["exchange"] = exchange
    if country:
        params["country"] = country.upper()
    items = []
    while len(items) < limit:
        params["start"] = len(items)
        response = requests.get(SYMBOL_SEARCH_URL, params=params, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        result = response.json()
        page = result.get("symbols") or []
        items += page
        if len(page) < SEARCH_PAGE_SIZE or not result.get("symbols_remaining"):
            break
    columns = ["symbol", "ticker", "description", "type", "exchange", "currency", "country", "isin", "cusip",
               "typespecs", "is_primary_listing"]
    return pd.DataFrame([{
        "symbol": _search_ticker(item),
        "ticker": item.get("symbol"),
        "description": item.get("description"),
        "type": item.get("type"),
        "exchange": item.get("exchange"),
        "currency": item.get("currency_code"),
        "country": item.get("country"),
        "isin": item.get("isin"),
        "cusip": item.get("cusip"),
        "typespecs": item.get("typespecs"),
        "is_primary_listing": item.get("is_primary_listing"),
    } for item in items[:limit]], columns=columns)


def get_peers(symbol, n=10, by="industry"):
    """
    Companies of the same industry (or sector) and market as a stock, largest first.

    TradingView's "related symbols" use the same rule: primary listings of the same
    industry in the same market, ordered by market capitalization.

    :param symbol: Exchange-prefixed stock symbol, e.g. "NASDAQ:AAPL"
    :param n: Number of peers
    :param by: "industry" or "sector"
    :return: DataFrame with columns: symbol, name, description, industry, sector, market_cap, close,
        change (%), currency. The stock itself is excluded.
    :raises ValueError: If ``by`` is invalid, or the symbol is unknown or has no industry
    """
    if by not in ("industry", "sector"):
        raise ValueError(f"by must be 'industry' or 'sector', got {by!r}")
    info = get_symbol(symbol, by, "market")
    if not info or not info.get(by) or not info.get("market"):
        raise ValueError(f"{symbol} is unknown or has no {by}")
    columns = ["name", "description", "industry", "sector", "market_cap_basic", "close", "change", "currency"]
    payload = {
        "columns": columns,
        "filter": [{"left": by, "operation": "equal", "right": info[by]},
                   {"left": "is_primary", "operation": "equal", "right": True},
                   {"left": "market_cap_basic", "operation": "nempty"}],
        "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"},
        "range": [0, n + 1],
    }
    response = requests.post(f"{SCANNER_URL}/{info['market']}/scan", data=json.dumps(payload),
                             headers={**REQUEST_HEADERS, 'Content-Type': 'application/json'}, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    data = [d for d in response.json().get("data") or [] if d["s"] != symbol][:n]
    df = pd.DataFrame([d["d"] for d in data], columns=columns).rename(columns={"market_cap_basic": "market_cap"})
    df.insert(0, "symbol", [d["s"] for d in data])
    return df
