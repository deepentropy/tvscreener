# Changelog

All notable changes to tvscreener.

## [Unreleased]

### Added

- **OR and nested filter logic** (#62)
  - Combine conditions with `|` and `&`: `ss.where((StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities'))`
  - Sent as TradingView's `filter2` tree; new `ConditionGroup` class
  - MCP `custom_query` accepts `{"or": [...]}` / `{"and": [...]}` groups
- **New filter operations** (#63)
  - `has()`, `has_none_of()` for set fields such as `typespecs`
  - `is_empty()`, `not_empty()`
  - `in_day_range(start, end)` for dates relative to today
  - `above_pct()`, `below_pct()`, `within_pct()`, `not_within_pct()` to compare with a percentage of another field or a number
  - Available in the MCP `custom_query` tool
- **Scanner helpers** (#72)
  - `get_symbol(symbol, *fields)`: any fields of one symbol
  - `get_enum_values(*ids)`: valid values of enumerable fields (sector, exchange, ETF issuer...)
  - `get_metainfo(market)` and `Screener.metainfo()`: field catalogue of a scanner market
- **Field enums regenerated from TradingView's metainfo** (#64)
  - New `scripts/generate_fields.py`: adds the fields that return data, marks the ones that never do as deprecated
  - Stocks: analyst estimates (`*_ESTIMATE_FQ/FY/FH/NTM`), forward multiples (`PRICE_EARNINGS_FWD`...), IPO fields, `EARNINGS_FQ_H` / `REVENUES_FQ_H` history
  - Coin: `FUNDING_RATE`, `OPEN_INTEREST`, open interest change and long/short liquidations (15m to 24h)
  - Bond: durations, `CONVEXITY`, `DV_01`, Z/G/F spreads, YTM/YTW bid/ask, Moody's and Fitch ratings
  - All price markets: 17 candlestick patterns, absolute performance (`PERF_*_ABS`)
  - Deprecated fields warn when used and are left out of `select_all()`. Full lists: [Field Changes](field-changes.md)

| Enum | Added | Deprecated |
|------|-------|------------|
| `StockField` | 129 | 26 |
| `CryptoField` | 33 | 131 |
| `ForexField` | 31 | 108 |
| `BondField` | 29 | 34 |
| `FuturesField` | 29 | 34 |
| `CoinField` | 56 | 257 |
| `EconomicsField` (new) | 37 | 0 |
| `IndexField` (new) | 358 | 0 |
| `GovernmentBondField` (new) | 129 | 0 |

- **`ETFScreener`** (#69): ETFs and ETNs sorted by AUM; new `INDEX_TRACKED` and readable `*_NAME` ETF fields (`ASSET_CLASS_NAME`, `FOCUS_NAME`...)
- **`EconomicsScreener`** (#66): 15,000+ economic indicators by country and `EconomicCategory`
- **`IndexScreener`** (#67): stock indices, index/commodity CFDs and crypto market-cap indices
- **`GovernmentBondScreener` and `get_yield_curve(country)`** (#68): benchmark government bond yields and prices by tenor
- **`Field.match(pattern)`**: case-insensitive regex match on text fields
- **Presets and calendars** (#70)
  - `StockScreener.set_preset()` with the `Preset` enum (gainers, losers, most volatile, all-time high, oversold...)
  - `get_earnings_calendar()`, `get_dividends_calendar()`, `get_ipo_calendar()` for a date range and markets
- **`set_currency()`** (#71)
  - Converts fundamentals (market cap, revenue, EPS...) to one currency: `ss.set_currency("eur")`
  - Prices are not converted
- **Code Generator: new operators and OR**
  - Operators: has any of, has none of, % above, % below, within %, outside %, day range, has a value, is empty
  - AND / OR toggle between filters; OR filters are grouped in one `where()` call

### Fixed

- **`StockField.DIVIDEND_YIELD_FY`** pointed to `dividend_yield_recent`, which returns no data; it now points to `DIVIDENDS_YIELD_FY`
- **Docs**: coin examples used `CoinField.MARKET_CAP` / `VOLUME`, which return no data; they use `MARKET_CAP_CALC` / `N24H_VOL_CMC`
- **`with_history()` rejected 26 indicators** (#65)
  - `StockField` indicators such as `RSI2`, `STOCH_K_5_3_3`, `ADX_PLUS_DI_50` and `MOM_14` have previous-bar values in TradingView but raised `ValueError`

### Changed

- `StockScreener.set_markets()` returns the screener, so it can be chained
- Filters on the same field are merged into one `in_range` filter only for the original comparison operations. The new operations are always kept as separate filters.

---

## [0.6.0] - 14/10/2026

### Added

- **`OptionScreener` and `OptionField`** (#53)
  - Option chains from the TradingView options scanner, for one or more underlyings (`OptionScreener("NASDAQ:AAPL")`)
  - Greeks (delta, gamma, theta, vega, rho), implied volatility (mid, bid, ask), theoretical price, bid/ask
  - Expiration is returned as a datetime; expiration filters accept dates, ISO strings or `YYYYMMDD` integers
- **`get_iv_term_structure(symbol)`** (#53)
  - Implied volatility by time to expiration: one point per listed expiration and standard tenors (1w to 1y)

---

## [0.5.2] - 23/09/2026

### Fixed

- **`with_interval()` rejects fields that already have a time interval**
  - Fields such as `StockField.EMA12_5` (`EMA12|5`) produced an invalid column like `EMA12|5|60`
  - They now raise `ValueError`
  - New `Field.accepts_interval()` tells if `with_interval()` can be applied

### Changed

- **Code Generator redesign**
  - New layout and styling
  - Searchable field picker for filters and sort; every field is reachable
  - Search matches initials (`rsi`, `sma50`)
  - Timeframe (`with_interval()`) for filters, columns and sort
  - `not in list` operator (`not_in()`)
  - Market selection for stocks (`set_markets()`); the market list now matches the `Market` enum

---

## [0.5.1] - 23/09/2026

### Fixed

- **`tvscreener-mcp` now works with mcp 2.x** (#60)
  - mcp 2.x renamed `FastMCP` to `MCPServer`, which made the server crash at startup
  - The server supports both mcp 1.x and 2.x

---

## [0.5.0] - 15/09/2026

### Fixed

- **`Rating.find()` now classifies boundary values correctly** (#57)
  - `0.5` maps to Buy instead of Strong Buy
  - `0.1` maps to Neutral instead of Buy
  - Rating bands no longer overlap at their boundaries

---

## [0.4.1] - 2026

### Fixed

- **`with_interval()` and `with_history()` no longer crash `get()`** (#56, #57)
  - `FieldWithInterval` and `FieldWithHistory` were missing `has_recommendation()`,
    which `get_columns_to_request()` calls on every selected field
  - Any `select()` using an interval or history wrapper raised `AttributeError`

- **Historical offset now placed before the interval suffix**
  - The auto-added 'Prev.' column built `RSI|1W[1]`, which TradingView
    answers with `null`; the valid form is `RSI[1]|1W`
  - Pre-baked interval fields (e.g. `ForexField.ADX_PLUS_DI_1_1`) are handled too
  - `with_history()` no longer stacks a second offset, which previously
    produced a duplicate `RSI[1][1]` column

- **`select_all()` works on every screener**
  - Forex, Crypto, Bond, Futures and Coin raised
    `ValueError: N columns passed, passed data had N+1 columns`
  - Two name collisions dropped a header entry: those enums define a field
    named `symbol` that clashed with the injected ticker column, and some
    distinct fields share one label (`High.All` and `all_time_high` are both
    'All Time High')
  - Duplicate names now get a `.1`, `.2` suffix, matching `pandas.read_csv`

### Changed

- `test_current_trading_day` no longer asserts a fixed row count. The
  `active_symbol` filter returns 0 rows outside market hours, so the test
  failed whenever it ran off-session.

---

## [0.2.1] - 2026

### Fixed

- **Field-to-field comparisons** now supported (e.g., `StockField.EMA5 >= StockField.EMA25`)
  - Removed incorrect TypeError that blocked field-to-field comparisons
  - The TradingView API does support these comparisons natively
  - Enables strategies like Golden Cross, EMA stacking, etc.

---

## [0.2.0] - 2025

### Added

- **MCP Server Integration** - Model Context Protocol server for AI assistants
  - Enable AI assistants (Claude, etc.) to query market data directly
  - `tvscreener.mcp` subpackage with full MCP support
  - `tvscreener-mcp` CLI entry point

- **MCP Tools**:
  - `discover_fields` - Search 3500+ available fields by keyword
  - `list_field_types` - Explore field categories
  - `custom_query` - Flexible queries with any fields and filters
  - `search_stocks` - Screen stocks by price, market cap, sector
  - `search_crypto` - Screen crypto by volume, market cap
  - `search_forex` - Screen forex pairs
  - `get_top_movers` - Get top gainers/losers
  - `list_sectors` - List available stock sectors
  - `list_filter_operators` - List available filter operators

### Installation

```bash
# Install with MCP support
pip install tvscreener[mcp]

# Run MCP server
tvscreener-mcp

# Register with Claude Code
claude mcp add tvscreener -- tvscreener-mcp
```

---

## [0.1.0] - 2024

### Added

- **Pythonic Comparison Operators** - Use `>`, `<`, `>=`, `<=`, `==`, `!=` directly on fields
  ```python
  ss.where(StockField.PRICE > 100)
  ss.where(StockField.VOLUME >= 1_000_000)
  ```

- **Range Methods** - `between()` and `not_between()` for range filtering
  ```python
  ss.where(StockField.PE_RATIO_TTM.between(10, 25))
  ss.where(StockField.RSI.not_between(30, 70))
  ```

- **List Methods** - `isin()` and `not_in()` for list matching
  ```python
  ss.where(StockField.SECTOR.isin(['Technology', 'Healthcare']))
  ```

- **Fluent API** - All methods return `self` for chaining
  ```python
  df = StockScreener().select(...).where(...).sort_by(...).get()
  ```

- **Index Filtering** - Filter by index constituents
  ```python
  ss.set_index(IndexSymbol.SP500)
  ```

- **Select All** - Retrieve all ~3,500 fields
  ```python
  ss.select_all()
  ```

- **Time Intervals** - Use indicators on multiple timeframes
  ```python
  rsi_1h = StockField.RSI.with_interval('60')
  ```

- **All 6 Screeners** - Stock, Crypto, Forex, Bond, Futures, Coin

### Changed

- Improved type safety with Field enums
- Better error messages for invalid field types

### Backward Compatibility

- Legacy `where(field, operator, value)` syntax still supported
- All existing code continues to work

---

## [0.0.x] - Previous Versions

Initial releases with basic screening functionality.

### Features

- Basic screener classes
- Filter by field and operator
- Select specific fields
- Sorting and pagination
- Streaming updates
- Styled output with `beautify()`
