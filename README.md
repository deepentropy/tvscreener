<div align="center">
  <img src="https://raw.githubusercontent.com/deepentropy/tvscreener/main/.github/img/logo.svg" alt="TradingView Screener API Logo" width="200" height="200"><br>
  <h1>TradingView™ Screener API</h1>
</div>

-----------------

# TradingView™ Screener API: simple Python library to retrieve data from TradingView™ Screener

[![PyPI version](https://badge.fury.io/py/tvscreener.svg)](https://badge.fury.io/py/tvscreener)
[![Downloads](https://pepy.tech/badge/tvscreener)](https://pepy.tech/project/tvscreener)
[![Coverage](https://codecov.io/github/deepentropy/tvscreener/coverage.svg?branch=main)](https://codecov.io/gh/deepentropy/tvscreener)
![tradingview-screener.png](https://raw.githubusercontent.com/deepentropy/tvscreener/main/.github/img/tradingview-screener.png)

Get the results as a Pandas Dataframe

![dataframe.png](https://github.com/deepentropy/tvscreener/blob/main/.github/img/dataframe.png?raw=true)

## Disclaimer

**This is an unofficial, third-party library and is not affiliated with, endorsed by, or connected to TradingView™ in any way.** TradingView™ is a trademark of TradingView™, Inc. This independent project provides a Python interface to publicly available data from TradingView's screener. Use of this library is at your own risk and subject to TradingView's terms of service.

# Main Features

- Query **Stock**, **Forex** and **Crypto** Screener
- All the **fields available**: ~300 fields - even hidden ones)
- **Any time interval** (`no need to be a registered user` - 1D, 5m, 1h, etc.)
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

For Stocks screener:

```python
import tvscreener as tvs

ss = tvs.StockScreener()
df = ss.get()

# ... returns a dataframe with 150 rows by default
``` 

For Forex screener:

```python
import tvscreener as tvs

fs = tvs.ForexScreener()
df = fs.get()
```

For Crypto screener:

```python
import tvscreener as tvs

cs = tvs.CryptoScreener()
df = cs.get()
```

## Parameters

For Options and Filters, please check the [notebooks](https://github.com/deepentropy/tvscreener/tree/main/notebooks) for
examples.

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