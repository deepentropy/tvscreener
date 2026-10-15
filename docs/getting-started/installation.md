# Installation

## Requirements

- Python 3.10 or higher
- pandas
- requests

## Install from PyPI

```bash
pip install tvscreener
```

## Install from Source

```bash
git clone https://github.com/deepentropy/tvscreener.git
cd tvscreener
pip install -e .
```

## Verify Installation

```python
import tvscreener as tvs

ss = tvs.StockScreener()
df = ss.get()
print(f"Retrieved {len(df)} stocks")
```

## Upgrade

```bash
pip install --upgrade tvscreener
```

## Dependencies

tvscreener automatically installs these dependencies:

| Package | Purpose |
|---------|---------|
| `pandas` | DataFrames for results |
| `requests` | HTTP requests to TradingView |
| `websocket-client` | TradingView's data websocket (financials, real-time quotes, events, seasonals) |

## Optional Dependencies

For MCP server integration (AI assistants like Claude):

```bash
pip install tvscreener[mcp]

# Run the MCP server
tvscreener-mcp

# Register with Claude Code
claude mcp add tvscreener -- tvscreener-mcp
```

The server exposes 24 tools:

- **Screeners:** `discover_fields`, `custom_query`, `search_stocks`, `search_crypto`, `search_forex`, `get_top_movers`, `symbol_data`
- **Company data:** `financials`, `corporate_events`, `seasonals`, `quotes`, `peers`
- **News and filings:** `news`, `company_documents`, `earnings_calls`, `read_text`
- **Markets:** `get_calendar` (earnings, dividends, IPO, economic), `yield_curve`, `forward_curve`, `volatility_smile`, `find_symbols`
- **Reference:** `list_field_types`, `list_sectors`, `list_filter_operators`

For styled output (colored tables):

```bash
pip install rich
```

For Jupyter notebook integration:

```bash
pip install ipywidgets
```

## Troubleshooting

### Import Error

If you get an import error, ensure you're using Python 3.10+:

```bash
python --version
```

### Connection Issues

tvscreener connects to TradingView's public API. If you experience timeouts:

1. Check your internet connection
2. Try again (TradingView may be rate-limiting)
3. Use a VPN if TradingView is blocked in your region

### No Data Returned

If `ss.get()` returns an empty DataFrame:

1. Check your filters - they may be too restrictive
2. Verify field names are correct (use autocomplete in your IDE)
3. Try without filters first: `StockScreener().get()`
