"""
MCP server for tvscreener.

Exposes market screener functionality via the Model Context Protocol.
"""

from __future__ import annotations

import json
from mcp.server.fastmcp import FastMCP

from .tools import (
    search_fields,
    get_field_categories,
    custom_screen,
    screen_stocks,
    screen_crypto,
    screen_forex,
)


mcp = FastMCP(
    "tvscreener",
    instructions=(
        "Query market screener for stocks, crypto, and forex via tvscreener library. "
        "Use discover_fields to find available fields, then use custom_query for flexible filtering."
    )
)


# =============================================================================
# FIELD DISCOVERY TOOLS
# =============================================================================

@mcp.tool()
def discover_fields(
    search_term: str,
    asset_type: str = "stock",
    limit: int = 20
) -> str:
    """
    Search for available fields/indicators by keyword.

    Use this to find field names for custom_query. There are 3500+ fields available.

    Args:
        search_term: Keyword to search (e.g., "rsi", "volume", "earnings", "dividend", "macd", "moving_average")
        asset_type: "stock", "crypto", "forex", "bond", "futures", or "coin"
        limit: Maximum results (default 20)

    Returns:
        List of matching field names and descriptions

    Examples:
        - discover_fields("rsi") -> finds RSI indicator fields
        - discover_fields("earnings") -> finds earnings-related fields
        - discover_fields("dividend") -> finds dividend fields
    """
    fields = search_fields(search_term, asset_type, limit)

    if not fields:
        return f"No fields found matching '{search_term}'"

    result = f"Found {len(fields)} fields matching '{search_term}':\n\n"
    for f in fields:
        tech_marker = " [Technical]" if f.get("is_technical") else ""
        result += f"- **{f['name']}**: {f['display_name']}{tech_marker}\n"

    return result


@mcp.tool()
def list_field_types(asset_type: str = "stock") -> str:
    """
    List available field categories with sample fields.

    Use this to explore what types of data are available before using discover_fields.

    Args:
        asset_type: "stock", "crypto", "forex", "bond", "futures", or "coin"

    Returns:
        Categories and sample field names
    """
    categories = get_field_categories(asset_type)

    result = f"Field categories for {asset_type}:\n\n"
    for category, fields in categories.items():
        result += f"**{category}**:\n"
        for f in fields:
            result += f"  - {f}\n"
        result += "\n"

    result += "\nUse discover_fields('keyword') to find more fields in each category."
    return result


# =============================================================================
# FLEXIBLE QUERY TOOL
# =============================================================================

@mcp.tool()
def custom_query(
    asset_type: str = "stock",
    fields: str | None = None,
    filters: str | None = None,
    sort_by: str | None = None,
    ascending: bool = False,
    limit: int = 25
) -> str:
    """
    Flexible query with any fields and filters.

    Use discover_fields first to find available field names.

    Args:
        asset_type: "stock", "crypto", "forex", "bond", "futures", or "coin"
        fields: Comma-separated field names to return (e.g., "NAME,PRICE,RSI,MACD_LEVEL_12_26")
                If not specified, returns default fields.
        filters: JSON array of filter conditions. Each filter has:
                 - field: Field name (use discover_fields to find names)
                 - op: Operator (">=", ">", "<=", "<", "==", "!=", "match", "in_range")
                 - value: Value to compare (use [min, max] array for in_range)

                 Example: '[{"field": "PRICE", "op": ">=", "value": 100}, {"field": "RSI", "op": "in_range", "value": [30, 70]}]'
        sort_by: Field name to sort by
        ascending: Sort direction (default False = descending)
        limit: Maximum results (default 25, max 100)

    Returns:
        Markdown table with query results

    Examples:
        1. Stocks with RSI between 30-70 and price > $50:
           fields="NAME,PRICE,RSI,VOLUME"
           filters='[{"field": "PRICE", "op": ">", "value": 50}, {"field": "RSI", "op": "in_range", "value": [30, 70]}]'

        2. High dividend stocks:
           fields="NAME,PRICE,DIVIDEND_YIELD_FY"
           filters='[{"field": "DIVIDEND_YIELD_FY", "op": ">=", "value": 3}]'
           sort_by="DIVIDEND_YIELD_FY"
    """
    # Parse fields
    select_fields = None
    if fields:
        select_fields = [f.strip() for f in fields.split(",")]

    # Parse filters
    filter_list = None
    if filters:
        try:
            filter_list = json.loads(filters)
        except json.JSONDecodeError as e:
            return f"Error parsing filters JSON: {e}"

    limit = min(limit, 100)

    try:
        df = custom_screen(
            asset_type=asset_type,
            select_fields=select_fields,
            filters=filter_list,
            sort_by=sort_by,
            ascending=ascending,
            limit=limit
        )

        if df.empty:
            return "No results found matching the criteria."

        return df.to_markdown(index=False)
    except Exception as e:
        return f"Error executing query: {e}"


# =============================================================================
# PRESET QUERY TOOLS
# =============================================================================

@mcp.tool()
def search_stocks(
    min_price: float | None = None,
    max_price: float | None = None,
    min_market_cap_billions: float | None = None,
    max_market_cap_billions: float | None = None,
    sectors: str | None = None,
    sort_by: str = "market_cap",
    limit: int = 25
) -> str:
    """
    Screen stocks with common filters (simplified interface).

    For advanced filtering, use custom_query with discover_fields.

    Args:
        min_price: Minimum stock price in USD
        max_price: Maximum stock price in USD
        min_market_cap_billions: Minimum market cap in billions USD
        max_market_cap_billions: Maximum market cap in billions USD
        sectors: Comma-separated sectors (Technology, Healthcare, Financial, etc.)
        sort_by: Sort by 'market_cap', 'price', 'volume', or 'change'
        limit: Maximum results (default 25, max 100)
    """
    min_cap = min_market_cap_billions * 1e9 if min_market_cap_billions else None
    max_cap = max_market_cap_billions * 1e9 if max_market_cap_billions else None
    sector_list = [s.strip() for s in sectors.split(",")] if sectors else None
    limit = min(limit, 100)

    df = screen_stocks(
        min_price=min_price,
        max_price=max_price,
        min_market_cap=min_cap,
        max_market_cap=max_cap,
        sectors=sector_list,
        sort_by=sort_by,
        limit=limit
    )

    if df.empty:
        return "No stocks found matching the criteria."

    return df.to_markdown(index=False)


@mcp.tool()
def search_crypto(
    min_volume_millions: float | None = None,
    min_market_cap_billions: float | None = None,
    limit: int = 25
) -> str:
    """
    Screen cryptocurrencies (simplified interface).

    For advanced filtering, use custom_query with discover_fields.

    Args:
        min_volume_millions: Minimum 24h trading volume in millions USD
        min_market_cap_billions: Minimum market cap in billions USD
        limit: Maximum results (default 25, max 100)
    """
    min_vol = min_volume_millions * 1e6 if min_volume_millions else None
    min_cap = min_market_cap_billions * 1e9 if min_market_cap_billions else None
    limit = min(limit, 100)

    df = screen_crypto(
        min_volume_24h=min_vol,
        min_market_cap=min_cap,
        limit=limit
    )

    if df.empty:
        return "No cryptocurrencies found matching the criteria."

    return df.to_markdown(index=False)


@mcp.tool()
def search_forex(
    min_volume_millions: float | None = None,
    limit: int = 25
) -> str:
    """
    Screen forex currency pairs.

    Args:
        min_volume_millions: Minimum trading volume in millions
        limit: Maximum results (default 25, max 100)
    """
    min_vol = min_volume_millions * 1e6 if min_volume_millions else None
    limit = min(limit, 100)

    df = screen_forex(min_volume=min_vol, limit=limit)

    if df.empty:
        return "No forex pairs found matching the criteria."

    return df.to_markdown(index=False)


@mcp.tool()
def get_top_movers(
    asset_type: str = "stock",
    direction: str = "gainers",
    limit: int = 10
) -> str:
    """
    Get top gaining or losing assets.

    Args:
        asset_type: "stock" or "crypto"
        direction: "gainers" or "losers"
        limit: Number of results (default 10, max 50)
    """
    limit = min(limit, 50)
    ascending = direction.lower() == "losers"

    if asset_type.lower() == "crypto":
        df = screen_crypto(sort_by="change", ascending=ascending, limit=limit)
    else:
        df = screen_stocks(sort_by="change", ascending=ascending, limit=limit)

    direction_label = "Losers" if ascending else "Gainers"

    if df.empty:
        return f"No {asset_type} data available."

    return f"Top {direction_label}:\n\n" + df.to_markdown(index=False)


@mcp.tool()
def list_sectors() -> str:
    """List available stock sectors for filtering."""
    sectors = [
        "Technology", "Healthcare", "Financial", "Consumer Cyclical",
        "Communication Services", "Industrials", "Consumer Defensive",
        "Energy", "Basic Materials", "Real Estate", "Utilities",
        "Electronic Technology", "Technology Services", "Producer Manufacturing"
    ]
    return "Available sectors:\n" + "\n".join(f"  - {s}" for s in sectors)


@mcp.tool()
def list_filter_operators() -> str:
    """List available filter operators for custom_query."""
    operators = {
        ">=": "Greater than or equal",
        ">": "Greater than",
        "<=": "Less than or equal",
        "<": "Less than",
        "==": "Equal to",
        "!=": "Not equal to",
        "match": "Text contains (for text fields like SECTOR)",
        "in_range": "Value between [min, max] (e.g., RSI between 30-70)",
        "not_in_range": "Value outside [min, max]",
        "crosses": "Value crosses another",
        "crosses_up": "Value crosses above another",
        "crosses_down": "Value crosses below another",
    }

    result = "Available filter operators for custom_query:\n\n"
    for op, desc in operators.items():
        result += f"- **{op}**: {desc}\n"

    result += "\nExample filters JSON:\n"
    result += '```json\n[\n'
    result += '  {"field": "PRICE", "op": ">=", "value": 100},\n'
    result += '  {"field": "RSI", "op": "in_range", "value": [30, 70]},\n'
    result += '  {"field": "SECTOR", "op": "match", "value": "Technology"}\n'
    result += ']\n```'

    return result


def run():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    run()
