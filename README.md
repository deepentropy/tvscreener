<div align="center">
  <svg xmlns="http://www.w3.org/2000/svg"
       viewBox="0 0 130 130"
       width="200"
       height="200"
       role="img"
       aria-labelledby="title">
    <title>Grid logo for screener API</title>
    <g fill="#ff4b5c">
      <rect x="10" y="10" width="30" height="30" rx="6"/>
      <rect x="50" y="10" width="30" height="30" rx="6"/>
      <rect x="90" y="10" width="30" height="30" rx="6"/>
      <rect x="10" y="50" width="30" height="30" rx="6"/>
      <rect x="50" y="50" width="30" height="30" rx="6"/>
      <rect x="90" y="50" width="30" height="30" rx="6"/>
      <rect x="10" y="90" width="30" height="30" rx="6"/>
      <rect x="50" y="90" width="30" height="30" rx="6"/>
      <rect x="90" y="90" width="30" height="30" rx="6"/>
    </g>
  </svg><br>
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