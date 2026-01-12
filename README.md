<div align="center">
  <img src="https://raw.githubusercontent.com/deepentropy/tvscreener/main/.github/img/logo.png" alt="TradingView Screener API Logo" width="200" height="200"><br>
  <h1>TradingView™ Screener API</h1>
</div>

-----------------

# TradingView™ Screener API: simple Python library to retrieve data from TradingView™ Screener

[![PyPI version](https://badge.fury.io/py/tvscreener.svg)](https://badge.fury.io/py/tvscreener)
[![Downloads](https://pepy.tech/badge/tvscreener)](https://pepy.tech/project/tvscreener)
[![Coverage](https://codecov.io/github/deepentropy/tvscreener/coverage.svg?branch=main)](https://codecov.io/gh/deepentropy/tvscreener)

## 🚀 Try the Code Generator

**Build screener queries visually and get Python code instantly!**

[![Code Generator](https://img.shields.io/badge/Try%20it-Code%20Generator-2962ff?style=for-the-badge&logo=python&logoColor=white)](https://deepentropy.github.io/tvscreener/)

The Code Generator lets you:
- Select from 6 screener types (Stock, Crypto, Forex, Bond, Futures, Coin)
- Build filters visually with 13,000+ fields
- Generate ready-to-use Python code
- Copy and run in your environment

---

![tradingview-screener.png](https://raw.githubusercontent.com/deepentropy/tvscreener/main/.github/img/tradingview-screener.png)

Get the results as a Pandas Dataframe

![dataframe.png](https://github.com/deepentropy/tvscreener/blob/main/.github/img/dataframe.png?raw=true)

## Disclaimer

**This is an unofficial, third-party library and is not affiliated with, endorsed by, or connected to TradingView™ in any way.** TradingView™ is a trademark of TradingView™, Inc. This independent project provides a Python interface to publicly available data from TradingView's screener. Use of this library is at your own risk and subject to TradingView's terms of service.

# What's New in v0.2.0

**MCP Server Integration** - This release adds Model Context Protocol (MCP) support, enabling AI assistants like Claude to query market data directly.

### MCP Server for AI Assistants

```bash
# Install with MCP support
pip install tvscreener[mcp]

# Run MCP server
tvscreener-mcp

# Register with Claude Code
claude mcp add tvscreener -- tvscreener-mcp
```

**MCP Tools:**
- `discover_fields` - Search 3500+ available fields by keyword
- `custom_query` - Flexible queries with any fields and filters
- `search_stocks` / `search_crypto` / `search_forex` - Simplified screeners
- `get_top_movers` - Get top gainers/losers

---

# What's New in v0.1.0

**Major API Enhancement Release** - This release significantly expands the library with new screeners, 13,000+ fields, and a more intuitive API.

### New Screeners
- **BondScreener** - Query government and corporate bonds
- **FuturesScreener** - Query futures contracts
- **CoinScreener** - Query coins from CEX and DEX exchanges

### Expanded Field Coverage
- **13,000+ fields** across all screener types (up from ~300)
- Complete technical indicator coverage with all time intervals
- Fields organized by category with search and discovery methods

### Pythonic Comparison Syntax
```python
from tvscreener import StockScreener, StockField

ss = StockScreener()
ss.where(StockField.PRICE > 50)
ss.where(StockField.VOLUME >= 1_000_000)
ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 50e9))
ss.where(StockField.SECTOR.isin(['Technology', 'Healthcare']))
df = ss.get()
```

### Fluent API
```python
# Chain methods for cleaner code
ss = StockScreener()
ss.select(StockField.NAME, StockField.PRICE, StockField.CHANGE_PERCENT)
ss.where(StockField.PRICE > 100)
df = ss.get()
```

### Field Presets
```python
from tvscreener import StockScreener, STOCK_VALUATION_FIELDS, STOCK_DIVIDEND_FIELDS

ss = StockScreener()
ss.specific_fields = STOCK_VALUATION_FIELDS + STOCK_DIVIDEND_FIELDS
```

### Type-Safe Validation
The library now validates that you're using the correct field types with each screener, catching errors early.

---

# Main Features

- Query **Stock**, **Forex**, **Crypto**, **Bond**, **Futures**, and **Coin** Screeners
- All the **fields available**: 13,000+ fields across all screener types
- **Any time interval** (`no need to be a registered user` - 1D, 5m, 1h, etc.)
- **Fluent API** with `select()` and `where()` methods for cleaner code
- **Field discovery** - search fields by name, get technicals, filter by category
- **Field presets** - curated field groups for common use cases
- **Type-safe validation** - catches field/screener mismatches
- Filters by any fields, symbols, markets, countries, etc.
- Get the results as a Pandas Dataframe
- **Styled output** with TradingView-like colors and formatting
- **Streaming/Auto-update** - continuously fetch data at specified intervals

## Installation

The source code is currently hosted on GitHub at:
https://github.com/deepentropy/tvscreener

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/tvscreener)

```sh
# or PyPI
pip install tvscreener
```

From pip + GitHub:

```sh
$ pip install git+https://github.com/deepentropy/tvscreener.git
```

## Usage

### Basic Screeners

```python
import tvscreener as tvs

# Stock Screener
ss = tvs.StockScreener()
df = ss.get()  # returns a dataframe with 150 rows by default

# Forex Screener
fs = tvs.ForexScreener()
df = fs.get()

# Crypto Screener
cs = tvs.CryptoScreener()
df = cs.get()

# Bond Screener (NEW)
bs = tvs.BondScreener()
df = bs.get()

# Futures Screener (NEW)
futs = tvs.FuturesScreener()
df = futs.get()

# Coin Screener (NEW) - CEX and DEX coins
coins = tvs.CoinScreener()
df = coins.get()
```

### Fluent API

Use `select()` and `where()` for cleaner, chainable code:

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUME,
    StockField.MARKET_CAPITALIZATION
)
ss.where(StockField.MARKET_CAPITALIZATION > 1e9)
ss.where(StockField.CHANGE_PERCENT > 5)
df = ss.get()
```

### Field Discovery

Search and explore the 13,000+ available fields:

```python
from tvscreener import StockField

# Search fields by name or label
rsi_fields = StockField.search("rsi")
print(f"Found {len(rsi_fields)} RSI-related fields")

# Get all technical indicator fields
technicals = StockField.technicals()
print(f"Found {len(technicals)} technical fields")

# Get recommendation fields
recommendations = StockField.recommendations()
```

### Field Presets

Use curated field groups for common analysis needs:

```python
from tvscreener import (
    StockScreener, get_preset, list_presets,
    STOCK_PRICE_FIELDS, STOCK_VALUATION_FIELDS, STOCK_DIVIDEND_FIELDS,
    STOCK_PERFORMANCE_FIELDS, STOCK_OSCILLATOR_FIELDS
)

# See all available presets
print(list_presets())
# ['stock_price', 'stock_volume', 'stock_valuation', 'stock_dividend', ...]

# Use presets directly
ss = StockScreener()
ss.specific_fields = STOCK_VALUATION_FIELDS + STOCK_DIVIDEND_FIELDS
df = ss.get()

# Or get preset by name
fields = get_preset('stock_performance')
```

**Available Presets:**
| Category | Presets |
|----------|---------|
| Stock | `stock_price`, `stock_volume`, `stock_valuation`, `stock_dividend`, `stock_profitability`, `stock_performance`, `stock_oscillators`, `stock_moving_averages`, `stock_earnings` |
| Crypto | `crypto_price`, `crypto_volume`, `crypto_performance`, `crypto_technical` |
| Forex | `forex_price`, `forex_performance`, `forex_technical` |
| Bond | `bond_basic`, `bond_yield`, `bond_maturity` |
| Futures | `futures_price`, `futures_technical` |
| Coin | `coin_price`, `coin_market` |

### Time Intervals for Technical Fields

Apply different time intervals to technical indicators:

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()

# Get RSI with 1-hour interval
rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval("60")

# Available intervals: 1, 5, 15, 30, 60, 120, 240, 1D, 1W, 1M
ss.specific_fields = [
    StockField.NAME,
    StockField.PRICE,
    rsi_1h,
    StockField.MACD_LEVEL_12_26.with_interval("240"),  # 4-hour MACD
]
df = ss.get()
```

## Parameters

For detailed usage examples, see the documentation and notebooks below.

## Styled Output

You can apply TradingView-style formatting to your screener results using the `beautify` function. This adds colored text for ratings and percent changes, formatted numbers with K/M/B suffixes, and visual indicators for buy/sell/neutral recommendations.

```python
import tvscreener as tvs

# Get raw data
ss = tvs.StockScreener()
df = ss.get()

# Apply TradingView styling
styled = tvs.beautify(df, tvs.StockField)

# Display in Jupyter/IPython (shows colored output)
styled
```

The styled output includes:
- **Rating columns** with colored text and directional arrows:
  - Buy signals: Blue color with up arrow (↑)
  - Sell signals: Red color with down arrow (↓)
  - Neutral: Gray color with dash (-)
- **Percent change columns**: Green for positive, Red for negative
- **Number formatting**: K, M, B, T suffixes for large numbers
- **Missing values**: Displayed as "--"

## Streaming / Auto-Update

You can use the `stream()` method to continuously fetch screener data at specified intervals. This is useful for monitoring real-time market data.

```python
import tvscreener as tvs

# Basic streaming with iteration limit
ss = tvs.StockScreener()
for df in ss.stream(interval=10, max_iterations=5):
    print(f"Got {len(df)} rows")

# Streaming with callback
from datetime import datetime

def on_update(df):
    print(f"Updated at {datetime.now()}: {len(df)} rows")

ss = tvs.StockScreener()
try:
    for df in ss.stream(interval=5, on_update=on_update):
        # Process data
        pass
except KeyboardInterrupt:
    print("Stopped streaming")

# Stream with filters
ss = tvs.StockScreener()
ss.set_markets(tvs.Market.AMERICA)
for df in ss.stream(interval=30, max_iterations=10):
    print(df.head())
```

**Parameters:**
- `interval`: Refresh interval in seconds (minimum 1.0 to avoid rate limiting)
- `max_iterations`: Maximum number of refreshes (None = infinite)
- `on_update`: Optional callback function called with each DataFrame

## Documentation

📖 **[Full Documentation](https://deepentropy.github.io/tvscreener/docs/)** - Complete guides, API reference, and examples.

### Quick Links

| Guide | Description |
|-------|-------------|
| [Quick Start](https://deepentropy.github.io/tvscreener/docs/getting-started/quickstart/) | Get up and running in 5 minutes |
| [Filtering](https://deepentropy.github.io/tvscreener/docs/guide/filtering/) | Complete filtering reference |
| [Stock Screening](https://deepentropy.github.io/tvscreener/docs/examples/stock-screening/) | Value, momentum, dividend strategies |
| [Technical Analysis](https://deepentropy.github.io/tvscreener/docs/examples/technical-analysis/) | RSI, MACD, multi-timeframe |
| [API Reference](https://deepentropy.github.io/tvscreener/docs/api/screeners/) | Screeners, Fields, Enums |

### Jupyter Notebooks

Interactive examples organized by use case:

| Notebook | Description |
|----------|-------------|
| [01-quickstart.ipynb](docs/notebooks/01-quickstart.ipynb) | Overview of all 6 screeners |
| [02-stocks.ipynb](docs/notebooks/02-stocks.ipynb) | Stock screening strategies |
| [03-crypto.ipynb](docs/notebooks/03-crypto.ipynb) | Crypto analysis |
| [04-forex.ipynb](docs/notebooks/04-forex.ipynb) | Forex pairs screening |
| [05-bonds-futures.ipynb](docs/notebooks/05-bonds-futures.ipynb) | Bonds and futures |