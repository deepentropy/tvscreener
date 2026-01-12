"""
Helper functions for MCP tools.

These functions provide a clean interface between MCP tools and the tvscreener library.
"""

from __future__ import annotations

import tvscreener as tvs
from tvscreener import (
    StockField, CryptoField, ForexField, BondField, FuturesField, CoinField,
    FilterOperator
)
import pandas as pd
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


# Mapping from string operators to FilterOperator enum
FILTER_OP_MAP = {
    ">=": FilterOperator.ABOVE_OR_EQUAL,
    ">": FilterOperator.ABOVE,
    "<=": FilterOperator.BELOW_OR_EQUAL,
    "<": FilterOperator.BELOW,
    "==": FilterOperator.EQUAL,
    "!=": FilterOperator.NOT_EQUAL,
    "in_range": FilterOperator.IN_RANGE,
    "not_in_range": FilterOperator.NOT_IN_RANGE,
    "match": FilterOperator.MATCH,
    "crosses": FilterOperator.CROSSES,
    "crosses_up": FilterOperator.CROSSES_UP,
    "crosses_down": FilterOperator.CROSSES_DOWN,
}

# Mapping from asset type to field class and screener class
ASSET_CONFIG = {
    "stock": {"field_class": StockField, "screener_class": tvs.StockScreener},
    "crypto": {"field_class": CryptoField, "screener_class": tvs.CryptoScreener},
    "forex": {"field_class": ForexField, "screener_class": tvs.ForexScreener},
    "bond": {"field_class": BondField, "screener_class": tvs.BondScreener},
    "futures": {"field_class": FuturesField, "screener_class": tvs.FuturesScreener},
    "coin": {"field_class": CoinField, "screener_class": tvs.CoinScreener},
}


def get_field_enum(field_name: str, asset_type: str = "stock"):
    """
    Get the field enum from a field name string.

    Args:
        field_name: Name of the field (e.g., "PRICE", "RSI", "VOLUME")
        asset_type: Asset type ("stock", "crypto", "forex", "bond", "futures", "coin")

    Returns:
        Field enum or None if not found
    """
    field_name = field_name.upper().replace(" ", "_")
    config = ASSET_CONFIG.get(asset_type, ASSET_CONFIG["stock"])
    field_class = config["field_class"]

    # Try direct attribute access first
    if hasattr(field_class, field_name):
        return getattr(field_class, field_name)

    # Fall back to search
    results = field_class.search(field_name)
    if results:
        return results[0]

    return None


def search_fields(
    query: str,
    asset_type: str = "stock",
    limit: int = 20
) -> list[dict[str, Any]]:
    """
    Search for available fields by keyword.

    Args:
        query: Search keyword (e.g., "rsi", "volume", "earnings")
        asset_type: Asset type
        limit: Maximum results to return

    Returns:
        List of matching field info dicts with 'name', 'display_name', 'is_technical'
    """
    config = ASSET_CONFIG.get(asset_type, ASSET_CONFIG["stock"])
    field_class = config["field_class"]

    results = field_class.search(query)[:limit]

    fields = []
    for f in results:
        # Field value tuple: (display_name, api_field, format, is_technical, is_recommendation)
        value = f.value
        fields.append({
            "name": f.name,
            "display_name": value[0] if len(value) > 0 else f.name,
            "is_technical": value[3] if len(value) > 3 else False,
        })

    return fields


def get_field_categories(asset_type: str = "stock") -> dict[str, list[str]]:
    """
    Get field categories with sample fields.

    Args:
        asset_type: Asset type

    Returns:
        Dict mapping category names to lists of field names
    """
    config = ASSET_CONFIG.get(asset_type, ASSET_CONFIG["stock"])
    field_class = config["field_class"]

    category_keywords = [
        "price", "volume", "moving_average", "rsi", "macd",
        "bollinger", "earnings", "dividend", "market_cap",
        "sector", "recommend"
    ]

    categories = {}
    for keyword in category_keywords:
        fields = [f.name for f in field_class.search(keyword)[:5]]
        if fields:
            categories[keyword] = fields

    return categories


def custom_screen(
    asset_type: str = "stock",
    select_fields: list[str] | None = None,
    filters: list[dict[str, Any]] | None = None,
    sort_by: str | None = None,
    ascending: bool = False,
    limit: int = 25
) -> pd.DataFrame:
    """
    Flexible screener with custom fields and filters.

    Args:
        asset_type: Asset type
        select_fields: List of field names to return
        filters: List of filter dicts: {"field": str, "op": str, "value": any}
        sort_by: Field name to sort by
        ascending: Sort direction
        limit: Maximum results

    Returns:
        DataFrame with query results
    """
    config = ASSET_CONFIG.get(asset_type, ASSET_CONFIG["stock"])
    screener = config["screener_class"]()

    # Select fields
    if select_fields:
        fields_to_select = []
        for fname in select_fields:
            field = get_field_enum(fname, asset_type)
            if field:
                fields_to_select.append(field)
        if fields_to_select:
            screener.select(*fields_to_select)

    # Apply filters
    if filters:
        for f in filters:
            field_name = f.get("field")
            op = f.get("op", ">=")
            value = f.get("value")

            field = get_field_enum(field_name, asset_type)
            if not field:
                continue

            filter_op = FILTER_OP_MAP.get(op)
            if not filter_op:
                continue

            screener.where(field, filter_op, value)

    # Apply sorting
    if sort_by:
        sort_field = get_field_enum(sort_by, asset_type)
        if sort_field:
            screener.sort_by(sort_field, ascending=ascending)

    df = screener.get()
    return df.head(limit)


def screen_stocks(
    min_price: float | None = None,
    max_price: float | None = None,
    min_market_cap: float | None = None,
    max_market_cap: float | None = None,
    sectors: list[str] | None = None,
    sort_by: str = "market_cap",
    ascending: bool = False,
    limit: int = 25
) -> pd.DataFrame:
    """
    Screen stocks with common filters.

    Args:
        min_price: Minimum stock price
        max_price: Maximum stock price
        min_market_cap: Minimum market cap
        max_market_cap: Maximum market cap
        sectors: List of sectors to filter
        sort_by: Sort field ('market_cap', 'price', 'volume', 'change')
        ascending: Sort direction
        limit: Maximum results

    Returns:
        DataFrame with matching stocks
    """
    ss = tvs.StockScreener()

    ss.select(
        StockField.NAME,
        StockField.PRICE,
        StockField.CHANGE_PERCENT,
        StockField.VOLUME,
        StockField.MARKET_CAPITALIZATION,
        StockField.PRICE_TO_EARNINGS_RATIO_TTM,
        StockField.SECTOR
    )

    if min_price is not None:
        ss.where(StockField.PRICE, FilterOperator.ABOVE_OR_EQUAL, min_price)
    if max_price is not None:
        ss.where(StockField.PRICE, FilterOperator.BELOW_OR_EQUAL, max_price)
    if min_market_cap is not None:
        ss.where(StockField.MARKET_CAPITALIZATION, FilterOperator.ABOVE_OR_EQUAL, min_market_cap)
    if max_market_cap is not None:
        ss.where(StockField.MARKET_CAPITALIZATION, FilterOperator.BELOW_OR_EQUAL, max_market_cap)
    if sectors:
        for s in sectors:
            ss.where(StockField.SECTOR, FilterOperator.MATCH, s)

    sort_field_map = {
        "market_cap": StockField.MARKET_CAPITALIZATION,
        "price": StockField.PRICE,
        "volume": StockField.VOLUME,
        "change": StockField.CHANGE_PERCENT,
    }
    if sort_by in sort_field_map:
        ss.sort_by(sort_field_map[sort_by], ascending=ascending)

    return ss.get().head(limit)


def screen_crypto(
    min_volume_24h: float | None = None,
    min_market_cap: float | None = None,
    sort_by: str = "market_cap",
    ascending: bool = False,
    limit: int = 25
) -> pd.DataFrame:
    """
    Screen cryptocurrencies with common filters.

    Args:
        min_volume_24h: Minimum 24h trading volume
        min_market_cap: Minimum market cap
        sort_by: Sort field ('market_cap', 'volume', 'change')
        ascending: Sort direction
        limit: Maximum results

    Returns:
        DataFrame with matching cryptocurrencies
    """
    cs = tvs.CryptoScreener()

    cs.select(
        CryptoField.NAME,
        CryptoField.PRICE,
        CryptoField.CHANGE_PERCENT,
        CryptoField.VOLUME_24H_IN_USD,
        CryptoField.MARKET_CAPITALIZATION
    )

    if min_volume_24h is not None:
        cs.where(CryptoField.VOLUME_24H_IN_USD, FilterOperator.ABOVE_OR_EQUAL, min_volume_24h)
    if min_market_cap is not None:
        cs.where(CryptoField.MARKET_CAPITALIZATION, FilterOperator.ABOVE_OR_EQUAL, min_market_cap)

    sort_field_map = {
        "market_cap": CryptoField.MARKET_CAPITALIZATION,
        "volume": CryptoField.VOLUME_24H_IN_USD,
        "change": CryptoField.CHANGE_PERCENT,
    }
    if sort_by in sort_field_map:
        cs.sort_by(sort_field_map[sort_by], ascending=ascending)

    return cs.get().head(limit)


def screen_forex(
    min_volume: float | None = None,
    limit: int = 25
) -> pd.DataFrame:
    """
    Screen forex currency pairs.

    Args:
        min_volume: Minimum trading volume
        limit: Maximum results

    Returns:
        DataFrame with matching forex pairs
    """
    fs = tvs.ForexScreener()

    fs.select(
        ForexField.NAME,
        ForexField.PRICE,
        ForexField.CHANGE_PERCENT,
        ForexField.VOLUME
    )

    if min_volume is not None:
        fs.where(ForexField.VOLUME, FilterOperator.ABOVE_OR_EQUAL, min_volume)

    return fs.get().head(limit)
