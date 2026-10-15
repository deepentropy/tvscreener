"""
MCP server for tvscreener.

Exposes market screener functionality via the Model Context Protocol.
"""

from __future__ import annotations

import json

import pandas as pd

# mcp 2.x renamed FastMCP to MCPServer and removed mcp.server.fastmcp (#60)
try:
    from mcp.server.mcpserver import MCPServer as FastMCP
except ImportError:
    from mcp.server.fastmcp import FastMCP

from ..field import Sector, Market
from ..calendars import get_earnings_calendar, get_dividends_calendar, get_ipo_calendar, get_economic_calendar
from ..core.futures import get_forward_curve
from ..core.government_bond import get_yield_curve, get_yield_matrix
from ..documents import get_documents, get_document, get_earnings_calls
from ..fundamentals import get_financials, get_corporate_events, get_seasonals
from ..news import get_news, get_article
from ..quotes import stream_quotes
from ..scanner import get_symbol, search_symbols, get_peers
from ..volatility import get_volatility_smile
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
        "Query TradingView screeners (stocks, ETFs, crypto, forex, bonds, futures, indices, "
        "economic indicators) via tvscreener. Use discover_fields to find available fields, then "
        "custom_query for flexible filtering. Also: financial statements, live quotes, dividends/earnings/"
        "splits, seasonals, earnings/dividend/IPO/economic calendars, news, filings and call transcripts, "
        "symbol search, peers, yield curves, futures forward curves and option volatility smiles. "
        "Symbols are exchange-prefixed (NASDAQ:AAPL); use find_symbols to find them."
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
        asset_type: "stock", "etf", "crypto", "forex", "bond", "government_bond", "futures", "coin", "index" or "economics"
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
        asset_type: "stock", "etf", "crypto", "forex", "bond", "government_bond", "futures", "coin", "index" or "economics"

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
    filters: str | list | dict | None = None,
    sort_by: str | None = None,
    ascending: bool = False,
    limit: int = 25,
    preset: str | None = None
) -> str:
    """
    Flexible query with any fields and filters.

    Use discover_fields first to find available field names.

    Args:
        asset_type: "stock", "etf", "crypto", "forex", "bond", "government_bond", "futures", "coin", "index" or "economics"
        fields: Comma-separated field names to return (e.g., "NAME,PRICE,RSI,MACD_LEVEL_12_26")
                If not specified, returns default fields.
        filters: JSON array of filter conditions, all combined with AND. Each filter has:
                 - field: Field name (use discover_fields to find names)
                 - op: Operator:
                   ">=", ">", "<=", "<", "==", "!=", "match", "in_range", "not_in_range",
                   "has", "has_none_of" (value: list, e.g. TYPESPECS has ["etf"]),
                   "empty", "not_empty" (no value),
                   "in_day_range" (value: [start, end] day offsets from today, e.g. [0, 7]),
                   "above_pct", "below_pct" (value: [field_or_number, pct]),
                   "within_pct", "not_within_pct" (value: [field_or_number, low_pct, high_pct])
                 - value: Value to compare (use [min, max] array for in_range)
                 A filter can also be an OR / AND group, nestable:
                 {"or": [{"field": "SECTOR", "op": "==", "value": "Finance"}, {"field": "SECTOR", "op": "==", "value": "Utilities"}]}

                 Example: '[{"field": "PRICE", "op": ">=", "value": 100}, {"field": "RSI", "op": "in_range", "value": [30, 70]}]'
        sort_by: Field name to sort by
        ascending: Sort direction (default False = descending)
        limit: Maximum results (default 25, max 100)
        preset: TradingView preset for stock/etf (e.g. "gainers", "losers", "most_volatile",
                "unusual_volume", "all_time_high", "oversold", "high_dividend"). Combined with filters.

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

        3. Large banks or utilities, price more than 5% above SMA 50:
           filters='[{"or": [{"field": "SECTOR", "op": "==", "value": "Finance"}, {"field": "SECTOR", "op": "==", "value": "Utilities"}]},
                     {"field": "MARKET_CAPITALIZATION", "op": ">", "value": 1e10},
                     {"field": "PRICE", "op": "above_pct", "value": ["SIMPLE_MOVING_AVERAGE_50", 5]}]'
    """
    # Parse fields
    select_fields = None
    if fields:
        select_fields = [f.strip() for f in fields.split(",")]

    # Parse filters
    #
    # The tool schema advertises `filters` as a string, but MCP clients that
    # JSON-parse tool arguments (e.g. Claude Code) deserialize a JSON array
    # into a real list before it reaches the server. Accept both encodings and
    # normalize to a list of dicts.
    filter_list = None
    if filters:
        if isinstance(filters, str):
            try:
                filter_list = json.loads(filters)
            except json.JSONDecodeError as e:
                return f"Error parsing filters JSON: {e}"
        else:
            filter_list = filters

        # A double-encoded JSON string decodes to another string.
        if isinstance(filter_list, str):
            try:
                filter_list = json.loads(filter_list)
            except json.JSONDecodeError as e:
                return f"Error parsing filters JSON: {e}"

        # A single filter passed as an object becomes a one-element list.
        if isinstance(filter_list, dict):
            filter_list = [filter_list]

    limit = min(limit, 100)

    try:
        df = custom_screen(
            asset_type=asset_type,
            select_fields=select_fields,
            filters=filter_list,
            sort_by=sort_by,
            ascending=ascending,
            limit=limit,
            preset=preset
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
        sectors: Comma-separated TradingView sectors (Electronic Technology, Health Technology, Finance, etc.).
            Use list_sectors for the full list.
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
    sectors = [s.value for s in Sector if s is not Sector.ANY]
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
        "has": "Set field (e.g. TYPESPECS) contains any of the values (list)",
        "has_none_of": "Set field contains none of the values (list)",
        "empty": "Field has no value (no value needed)",
        "not_empty": "Field has a value (no value needed)",
        "in_day_range": "Date within [start, end] day offsets from today (e.g. [0, 7])",
        "above_pct": "More than pct% above a field or number: [other, pct]",
        "below_pct": "More than pct% below a field or number: [other, pct]",
        "within_pct": "Between low% and high% of a field or number: [other, low_pct, high_pct]",
        "not_within_pct": "Outside low% to high% of a field or number: [other, low_pct, high_pct]",
    }

    result = "Available filter operators for custom_query:\n\n"
    for op, desc in operators.items():
        result += f"- **{op}**: {desc}\n"

    result += "\nExample filters JSON:\n"
    result += '```json\n[\n'
    result += '  {"field": "PRICE", "op": ">=", "value": 100},\n'
    result += '  {"field": "RSI", "op": "in_range", "value": [30, 70]},\n'
    result += '  {"field": "SECTOR", "op": "match", "value": "Technology"}\n'
    result += ']\n```\n'
    result += "\nOR / AND groups (nestable):\n"
    result += '```json\n'
    result += '{"or": [{"field": "SECTOR", "op": "==", "value": "Finance"}, {"field": "SECTOR", "op": "==", "value": "Utilities"}]}\n'
    result += '```'

    return result


# =============================================================================
# CALENDARS, RATES AND SINGLE SYMBOLS
# =============================================================================

def _list_arg(value: str | None):
    """'US, EU' -> ['US', 'EU']; None or '' -> None."""
    if not value:
        return None
    return [v.strip() for v in value.split(",") if v.strip()]


def _markets_arg(markets: str | None):
    if not markets:
        return None
    if markets.strip().upper() == "ALL":
        return Market.ALL
    return [m.strip().lower() for m in markets.split(",")]


@mcp.tool()
def get_calendar(
    kind: str = "earnings",
    start: str | None = None,
    end: str | None = None,
    markets: str | None = None,
    countries: str | None = None,
    importance: str | None = None,
    limit: int = 50
) -> str:
    """
    Earnings, dividend, IPO or economic calendar for a date range.

    Args:
        kind: "earnings", "dividends", "ipo" or "economic" (data releases, central bank decisions, speeches)
        start: First day, YYYY-MM-DD (default today)
        end: Last day, YYYY-MM-DD, inclusive (default start)
        markets: earnings/dividends/ipo only: comma-separated markets (e.g. "america,germany") or "ALL"
            (default america)
        countries: economic only: comma-separated ISO codes, e.g. "US,EU,DE" (default all)
        importance: economic only: minimum importance "low", "medium" or "high"
        limit: Maximum rows (default 50, max 200); earnings are sorted by date then market cap
    """
    functions = {"earnings": get_earnings_calendar, "dividends": get_dividends_calendar, "ipo": get_ipo_calendar}
    if kind not in functions and kind != "economic":
        return f"Unknown kind {kind!r}; use earnings, dividends, ipo or economic"
    try:
        if kind == "economic":
            df = get_economic_calendar(start, end, countries=_list_arg(countries), importance=importance)
            df = df.drop(columns=["category", "source", "reference_date", "id"])
        else:
            df = functions[kind](start, end, markets=_markets_arg(markets))
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No {kind} events in this period."
    return f"{len(df)} {kind} events:\n\n" + df.head(min(limit, 200)).to_markdown(index=False)


@mcp.tool()
def yield_curve(country: str = "US", tenors: str | None = None) -> str:
    """
    Government bond yields in percent by tenor: one country's curve, or several countries side by side.

    Args:
        country: ISO country code ("US", "DE", "JP"...), several comma-separated ("US,DE,JP"),
            or "ALL" for every country. Several countries return a matrix (rows: countries, columns: tenors).
        tenors: Comma-separated tenors to keep, e.g. "3M,2Y,10Y,30Y" (returns the matrix layout)
    """
    countries = _list_arg(country) or ["US"]
    every = countries[0].upper() == "ALL"
    try:
        if len(countries) == 1 and not every and not tenors:
            df = get_yield_curve(countries[0])
            if df.empty:
                return f"No benchmark yields for {country}."
            return df.to_markdown(index=False)
        df = get_yield_matrix(None if every else countries, _list_arg(tenors))
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No benchmark yields for {country}."
    return df.to_markdown(floatfmt=".3f")


@mcp.tool()
def symbol_data(symbol: str, fields: str) -> str:
    """
    Any fields of one symbol.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL", "BINANCE:BTCUSDT"
        fields: Comma-separated API field names, e.g. "close,market_cap_basic,RSI,price_earnings_ttm"
    """
    try:
        data = get_symbol(symbol, *[f.strip() for f in fields.split(",") if f.strip()])
    except Exception as e:
        return f"Error: {e}"
    if data is None:
        return f"Symbol {symbol} not found."
    return json.dumps(data, indent=2, default=str)


# =============================================================================
# COMPANY DATA: FINANCIALS, EVENTS, SEASONALS, QUOTES
# =============================================================================

@mcp.tool()
def financials(symbol: str, statement: str = "income", period: str = "FY", periods: int = 8) -> str:
    """
    Financial statement history of a company, as on TradingView's financials pages.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
        statement: "income", "balance_sheet", "cash_flow" or "statistics" (ratios, per-share values, valuation)
        period: "FY" (annual, ~20 years), "FQ" (quarterly, ~32 quarters), "FH" (semi-annual) or "TTM"
        periods: Number of most recent periods to show (default 8, max 40)

    Returns:
        Markdown table: one row per item, one column per period (oldest to newest).
        Statement amounts are in millions of the reporting currency; statistics are shown as is.
    """
    try:
        df = get_financials(symbol, statement, period)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No {period} {statement} data for {symbol}."
    table = df.drop(columns="period_end").tail(min(periods, 40)).T
    currency = df.attrs.get("currency") or ""
    if statement == "statistics":
        return f"{symbol} statistics ({period}, {currency}):\n\n" + table.to_markdown(floatfmt=".4g")
    return f"{symbol} {statement} ({period}, millions {currency}):\n\n" + (table / 1e6).to_markdown(floatfmt=",.0f")


@mcp.tool()
def corporate_events(symbol: str) -> str:
    """
    Recent dividends, earnings releases (actual vs estimate, next release date) and stock splits of a company.

    Only recent history is available: about 20 dividends and 2 years of earnings.
    For longer EPS or revenue history use financials.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
    """
    try:
        events = get_corporate_events(symbol)
    except Exception as e:
        return f"Error: {e}"
    parts = []
    for kind, df in events.items():
        body = df.to_markdown(index=False) if not df.empty else "None."
        parts.append(f"## {kind.capitalize()}\n\n{body}")
    return "\n\n".join(parts)


@mcp.tool()
def seasonals(symbol: str, start_year: int | None = None, end_year: int | None = None) -> str:
    """
    Monthly returns (%) of a symbol, one row per year, with the average and share of positive years per month.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL", "BINANCE:BTCUSDT"
        start_year: First year (default 9 years before end_year)
        end_year: Last year (default current year)
    """
    try:
        df = get_seasonals(symbol, start_year, end_year)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No seasonal data for {symbol}."
    years = df.copy()
    df.loc["Average"] = years.mean()
    df.loc["% positive"] = (years > 0).sum() / years.notna().sum() * 100
    return df.to_markdown(floatfmt=".2f")


@mcp.tool()
def quotes(symbols: str, wait_seconds: float = 5) -> str:
    """
    Current quotes pushed by TradingView: last price, change, volume, bid/ask, pre/after-market price.

    Args:
        symbols: Comma-separated exchange-prefixed symbols, e.g. "NASDAQ:AAPL,BINANCE:BTCUSDT"
        wait_seconds: Maximum time to collect quotes (default 5, max 30)

    Returns:
        Markdown table; update_mode shows whether a quote is real time ("streaming") or delayed
    """
    names = _list_arg(symbols)
    if not names:
        return "Error: no symbols given"
    latest = {}
    try:
        for update in stream_quotes(names, duration=min(max(wait_seconds, 1), 30)):
            latest[update["symbol"]] = update
            if all("price" in latest.get(n, {}) or "error" in latest.get(n, {}) for n in names):
                break
    except Exception as e:
        return f"Error: {e}"
    rows = [{k: v for k, v in latest.get(n, {"symbol": n, "error": "no data"}).items() if k != "updated"}
            for n in names]
    return pd.DataFrame(rows).to_markdown(index=False)


# =============================================================================
# NEWS, FILINGS AND TRANSCRIPTS
# =============================================================================

@mcp.tool()
def news(
    symbol: str | None = None,
    provider: str | None = None,
    market: str | None = None,
    sector: str | None = None,
    corp_activity: str | None = None,
    country: str | None = None,
    priority: str | None = None,
    limit: int = 20
) -> str:
    """
    Latest news headlines, newest first. Filters are combined with AND; each takes one value.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL" (default: all news)
        provider: e.g. "reuters", "dow-jones", "business_wire", "tradingview", "zacks", "benzinga"
        market: "stock", "etf", "crypto", "forex", "index", "futures", "bond", "corp_bond" or "economic"
        sector: Stock sector, e.g. "Finance"
        corp_activity: "ipo", "earnings", "earnings_calls", "dividends", "share_buybacks",
            "mergers_and_acquisitions", "management", "insider_trading", "ownership_changes", "esg",
            "recommendation" (analyst ratings) or "credit_ratings"
        country: ISO code of the market, e.g. "US"
        priority: "flash", "important", "top_stories" or "key_facts"
        limit: Maximum headlines (default 20, max 200)

    Returns:
        Markdown table with an id per story; pass it to read_text for the full article
    """
    try:
        df = get_news(symbol, provider=provider, market=market, sector=sector, corp_activity=corp_activity,
                      country=country, priority=priority)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return "No news found."
    df = df[["published", "title", "provider", "related_symbols", "id"]].head(min(limit, 200)).copy()
    df["related_symbols"] = df["related_symbols"].map(lambda s: ", ".join(s[:5]))
    return df.to_markdown(index=False)


@mcp.tool()
def company_documents(
    symbol: str,
    category: str | None = None,
    start: str | None = None,
    end: str | None = None,
    limit: int = 30
) -> str:
    """
    Filings, reports and transcripts of a company, newest first: 10-Q, 10-K, earnings releases,
    earnings call and event transcripts (provider: Quartr).

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
        category: Comma-separated categories: "quarterly_report", "annual_report", "interim_report",
            "earnings_release", "call_transcript", "event_transcript", "slides" (default all)
        start: First day, YYYY-MM-DD (default full history)
        end: Last day, YYYY-MM-DD (default today)
        limit: Maximum rows (default 30, max 200)

    Returns:
        Markdown table; pass transcript_id or summary_id to read_text for the text
    """
    try:
        df = get_documents(symbol, category=_list_arg(category), start=start, end=end)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No documents for {symbol}."
    columns = ["date", "title", "category", "form", "fiscal_year", "fiscal_period", "transcript_id", "summary_id"]
    return df[columns].head(min(limit, 200)).to_markdown(index=False)


@mcp.tool()
def earnings_calls(symbol: str, start: str | None = None, end: str | None = None) -> str:
    """
    Past and scheduled earnings calls of a company, with live transcript and recording links.

    Args:
        symbol: Exchange-prefixed symbol, e.g. "NASDAQ:AAPL"
        start: First day, YYYY-MM-DD (default one year before end)
        end: Last day, YYYY-MM-DD (default 90 days from today, to include scheduled calls)
    """
    try:
        df = get_earnings_calls(symbol, start=start, end=end)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No earnings calls for {symbol}."
    return df.drop(columns="id").to_markdown(index=False)


@mcp.tool()
def read_text(id: str, max_chars: int = 20000) -> str:
    """
    Full text of a news story, transcript or document summary.

    Args:
        id: A story id from news, or a transcript_id / summary_id from company_documents
        max_chars: Maximum characters returned (default 20000)
    """
    try:
        text = get_document(id) if id.startswith("urn:") else get_article(id)
    except Exception as e:
        return f"Error: {e}"
    if not text:
        return "No text available."
    if len(text) > max_chars:
        return text[:max_chars] + f"\n\n[... truncated, {len(text):,} characters in total]"
    return text


# =============================================================================
# SYMBOLS, PEERS, FUTURES AND OPTIONS
# =============================================================================

@mcp.tool()
def find_symbols(text: str, type: str | None = None, exchange: str | None = None, country: str | None = None,
                 limit: int = 20) -> str:
    """
    Search symbols by ticker, company name, ISIN or CUSIP. Returns exchange-prefixed symbols for the other tools.

    Args:
        text: e.g. "AAPL", "apple", "US0378331005"
        type: "stock", "funds", "futures", "forex", "crypto", "index", "bond" or "economic" (default all)
        exchange: Restrict to an exchange, e.g. "NASDAQ", "XETR"
        country: ISO code whose listings come first, e.g. "DE"
        limit: Maximum results (default 20, max 200)
    """
    try:
        df = search_symbols(text, type=type, exchange=exchange, country=country, limit=min(limit, 200))
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No symbols found for {text!r}."
    return df.drop(columns=["typespecs"]).to_markdown(index=False)


@mcp.tool()
def peers(symbol: str, n: int = 10, by: str = "industry") -> str:
    """
    Largest companies of the same industry (or sector) and market as a stock.

    Args:
        symbol: Exchange-prefixed stock symbol, e.g. "NASDAQ:AAPL"
        n: Number of peers (default 10, max 50)
        by: "industry" or "sector"
    """
    try:
        df = get_peers(symbol, n=min(n, 50), by=by)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No peers found for {symbol}."
    return df.to_markdown(index=False)


@mcp.tool()
def forward_curve(root: str) -> str:
    """
    Futures forward curve: every listed contract month of a futures root, by expiration.

    Args:
        root: Exchange-prefixed root, e.g. "NYMEX:CL" (crude oil), "COMEX:GC" (gold), "CME_MINI:ES".
            A continuous symbol such as "NYMEX:CL1!" works too. find_symbols(text, type="futures") finds roots.
    """
    try:
        df = get_forward_curve(root)
    except Exception as e:
        return f"Error: {e}"
    if df.empty:
        return f"No contracts found for {root}."
    return df.to_markdown(index=False)


@mcp.tool()
def volatility_smile(symbol: str, expiration: str, root: str | None = None, x: str = "strike") -> str:
    """
    Implied volatility smile of one option expiration.

    Args:
        symbol: Exchange-prefixed underlying, e.g. "NASDAQ:AAPL"
        expiration: Expiration date, YYYY-MM-DD
        root: Option root when it differs from the ticker, e.g. "SPXW" for SP:SPX weeklies
        x: "strike" or "moneyness" (log-moneyness, 0 at the money)

    Returns:
        Markdown table of implied volatility (fraction, 0.27 = 27%) by strike or moneyness
    """
    try:
        df = get_volatility_smile(symbol, expiration, root=root, x=x)
    except Exception as e:
        return f"Error: {e}"
    return df.to_markdown(index=False, floatfmt=".4g")


def run():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    run()
