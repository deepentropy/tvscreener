# Changelog

All notable changes to tvscreener.

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
