# Quick Start Guide

Get up and running with tvscreener in 5 minutes.

## Installation

```bash
pip install tvscreener
```

## Basic Usage

```python
import tvscreener as tvs

# Create a screener and get data
ss = tvs.StockScreener()
df = ss.get()  # Returns pandas DataFrame with 150 stocks
```

## Filtering Stocks

Use Python comparison operators directly on fields:

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()

# Filter by price, volume, and market cap
ss.where(StockField.PRICE > 10)
ss.where(StockField.VOLUME >= 1_000_000)
ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 50e9))

df = ss.get()
```

## Selecting Fields

Choose which data columns to retrieve:

```python
ss = StockScreener()
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUME,
    StockField.PE_RATIO_TTM
)
df = ss.get()
```

Or get all ~3,500 available fields:

```python
ss = StockScreener()
ss.select_all()
df = ss.get()
```

## Index Constituents

Filter to stocks in major indices:

```python
from tvscreener import StockScreener, IndexSymbol

ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.set_range(0, 500)
df = ss.get()  # S&P 500 stocks only
```

## Specific Symbols

Query specific tickers:

```python
ss = StockScreener()
ss.symbols = {
    "query": {"types": []},
    "tickers": ["NASDAQ:AAPL", "NASDAQ:MSFT", "NYSE:JPM"]
}
df = ss.get()
```

## Other Screeners

```python
import tvscreener as tvs

# Forex
fs = tvs.ForexScreener()
df = fs.get()

# Crypto
cs = tvs.CryptoScreener()
df = cs.get()

# Bonds
bs = tvs.BondScreener()
df = bs.get()

# Futures
futs = tvs.FuturesScreener()
df = futs.get()
```

## Next Steps

- [Filtering Guide](filtering.md) - Complete filtering reference
- [Stock Screening Examples](examples/stock-screening.md) - Value, momentum, dividend strategies
- [Technical Analysis Examples](examples/technical-analysis.md) - RSI, MACD, multi-timeframe
- [Field Reference](fields/README.md) - All 13,000+ available fields
