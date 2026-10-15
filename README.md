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
- Select from 10 screener types (Stock, ETF, Crypto, Forex, Bond, Government Bond, Futures, Coin, Index, Economics)
- Build filters visually with 13,000+ fields, combined with AND / OR
- Generate ready-to-use Python code
- Copy and run in your environment

---

![tradingview-screener.png](https://raw.githubusercontent.com/deepentropy/tvscreener/main/.github/img/tradingview-screener.png)

Get the results as a Pandas Dataframe

![dataframe.png](https://github.com/deepentropy/tvscreener/blob/main/.github/img/dataframe.png?raw=true)

## Disclaimer

**This is an unofficial, third-party library and is not affiliated with, endorsed by, or connected to TradingView™ in any way.** TradingView™ is a trademark of TradingView™, Inc. This independent project provides a Python interface to publicly available data from TradingView's screener. Use of this library is at your own risk and subject to TradingView's terms of service.

# Main Features

- Query **Stock**, **ETF**, **Forex**, **Crypto**, **Bond**, **Government Bond**, **Futures**, **Coin**, **Option**, **Index** and **Economics** Screeners
- **OR / nested filters** with `|` and `&`, and operators such as `has()`, `above_pct()`, `in_day_range()`
- **TradingView presets** (gainers, losers, all-time highs...) and **earnings, dividend, IPO and economic calendars**
- **Financial statements**: about 20 years of annual and 8 years of quarterly income statement, balance sheet and cash flow
- **Real-time quotes** pushed by TradingView, recent dividends, earnings and splits, and **seasonals**
- **News** with filters, **filings and earnings call transcripts**
- **Yield curves and matrix**, futures forward curves, IV term structure and smile, symbol search, peers and single-symbol lookups
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
- **MCP server** for AI assistants: `pip install tvscreener[mcp]`, then `claude mcp add tvscreener -- tvscreener-mcp`

> [!TIP]
> **New in 0.8:** financial statements, real-time quotes, economic calendar, news, filings and earnings call transcripts, also as MCP tools. See [Financials and Events](https://deepentropy.github.io/tvscreener/docs/guide/fundamentals/) and [News and Filings](https://deepentropy.github.io/tvscreener/docs/guide/news-documents/).

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

# Option Screener - option chains with greeks and IV (underlying required)
opts = tvs.OptionScreener("NASDAQ:AAPL")
opts.where(tvs.OptionField.DELTA.between(0.4, 0.6))
df = opts.get()

# Implied volatility term structure
df = tvs.get_iv_term_structure("NASDAQ:AAPL")

# ETF Screener - ETFs sorted by assets under management
etfs = tvs.ETFScreener()
etfs.where(tvs.StockField.EXPENSE_RATIO < 0.1)
df = etfs.get()

# Index Screener - indices, CFDs, crypto market caps
df = tvs.IndexScreener().main_indices().get()

# Economics Screener - 15,000+ economic indicators
es = tvs.EconomicsScreener()
es.where(tvs.EconomicsField.COUNTRY_CODE == 'US')
df = es.get()

# Government bond yield curve
df = tvs.get_yield_curve("US")
```

### OR Filters and Presets

```python
ss = tvs.StockScreener()
ss.where((tvs.StockField.SECTOR == 'Finance') | (tvs.StockField.SECTOR == 'Utilities'))
ss.where(tvs.StockField.PRICE.above_pct(tvs.StockField.SIMPLE_MOVING_AVERAGE_50, 5))
df = ss.get()

# TradingView's own screens
df = tvs.StockScreener().set_preset(tvs.Preset.GAINERS).get()
```

### Calendars

```python
earnings = tvs.get_earnings_calendar("2026-10-12", "2026-10-18")
dividends = tvs.get_dividends_calendar("2026-10-12", "2026-10-18")
ipos = tvs.get_ipo_calendar("2026-10-01", "2026-10-31", markets=tvs.Market.ALL)
macro = tvs.get_economic_calendar("2026-10-12", "2026-10-18", countries=["US", "EU"], importance="high")
```

### Financials, Events and Real-Time Quotes

```python
income = tvs.get_financials("NASDAQ:AAPL", "income", "FY")       # ~20 fiscal years
balance = tvs.get_financials("NASDAQ:AAPL", "balance_sheet", "FQ")
events = tvs.get_corporate_events("NASDAQ:AAPL")                  # dividends, earnings, splits
seasonals = tvs.get_seasonals("NASDAQ:AAPL")                      # monthly returns by year

for quote in tvs.stream_quotes(["NASDAQ:AAPL", "BINANCE:BTCUSDT"], duration=60):
    print(quote["symbol"], quote.get("price"))
```

### News, Filings and Market Helpers

```python
news = tvs.get_news("NASDAQ:AAPL", corp_activity="insider_trading")
text = tvs.get_article(news["id"].iloc[0])
docs = tvs.get_documents("NASDAQ:AAPL", category="call_transcript")
transcript = tvs.get_document(docs["transcript_id"].iloc[0])

tvs.search_symbols("US0378331005")             # ISIN -> NASDAQ:AAPL and other listings
tvs.get_peers("NASDAQ:AAPL")
tvs.get_forward_curve("NYMEX:CL")
tvs.get_yield_matrix(["US", "DE", "JP"])
tvs.get_volatility_smile("NASDAQ:AAPL", "2026-11-13")
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
| [Financials and Events](https://deepentropy.github.io/tvscreener/docs/guide/fundamentals/) | Statements, dividends, earnings, seasonals |
| [News and Filings](https://deepentropy.github.io/tvscreener/docs/guide/news-documents/) | Filtered news, 10-Q/10-K, call transcripts |
| [Streaming](https://deepentropy.github.io/tvscreener/docs/guide/streaming/) | Screener refreshes and real-time quotes |
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
