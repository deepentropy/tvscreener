"""Helpers for the TradingView scanner endpoints that are not screener queries."""
import pandas as pd
import requests

SCANNER_URL = "https://scanner.tradingview.com"
REQUEST_TIMEOUT = 30

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
