# Futures Screener

Screen futures contracts across commodities, indices, and currencies.

## Quick Start

```python
from tvscreener import FuturesScreener, FuturesField

fs = FuturesScreener()
df = fs.get()
```

## Field Count

The Futures Screener has access to **~393 fields** covering:

- Price data (open, high, low, close)
- Volume and open interest
- Technical indicators
- Performance metrics

## Common Fields

### Price & Volume

```python
FuturesField.PRICE           # Current price
FuturesField.OPEN            # Day open
FuturesField.HIGH            # Day high
FuturesField.LOW             # Day low
FuturesField.VOLUME          # Trading volume
FuturesField.CHANGE_PERCENT  # Daily change
```

### Technical

```python
FuturesField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
FuturesField.MACD_LEVEL_12_26              # MACD
FuturesField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
FuturesField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
FuturesField.AVERAGE_TRUE_RANGE_14         # ATR
```

### Performance

```python
FuturesField.PERF_W                  # 1 week
FuturesField.PERF_1M                 # 1 month
FuturesField.PERF_YTD                # Year to date
FuturesField.PERF_Y                  # 1 year
```

## Example Screens

### All Futures by Volume

```python
fs = FuturesScreener()
fs.sort_by(FuturesField.VOLUME, ascending=False)
fs.set_range(0, 50)
fs.select(
    FuturesField.NAME,
    FuturesField.PRICE,
    FuturesField.CHANGE_PERCENT,
    FuturesField.VOLUME
)

df = fs.get()
```

### Top Gainers

```python
fs = FuturesScreener()
fs.where(FuturesField.CHANGE_PERCENT > 2)
fs.sort_by(FuturesField.CHANGE_PERCENT, ascending=False)
fs.select(
    FuturesField.NAME,
    FuturesField.PRICE,
    FuturesField.CHANGE_PERCENT
)

df = fs.get()
```

### Oversold RSI

```python
fs = FuturesScreener()
fs.where(FuturesField.RELATIVE_STRENGTH_INDEX_14 < 30)
fs.select(
    FuturesField.NAME,
    FuturesField.PRICE,
    FuturesField.RELATIVE_STRENGTH_INDEX_14
)
fs.sort_by(FuturesField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = fs.get()
```

### High Volatility

```python
fs = FuturesScreener()
fs.where(FuturesField.AVERAGE_TRUE_RANGE_14 > 0)
fs.sort_by(FuturesField.AVERAGE_TRUE_RANGE_14, ascending=False)
fs.select(
    FuturesField.NAME,
    FuturesField.PRICE,
    FuturesField.AVERAGE_TRUE_RANGE_14,
    FuturesField.VOLATILITY_D
)
fs.set_range(0, 20)

df = fs.get()
```

## Specific Futures

Query specific contracts:

```python
fs = FuturesScreener()
fs.symbols = {
    "query": {"types": []},
    "tickers": ["CME:ES1!", "CME:NQ1!", "COMEX:GC1!", "NYMEX:CL1!"]
}
fs.select_all()

df = fs.get()
```

## Common Futures Symbols

### Index Futures

| Contract | Symbol |
|----------|--------|
| E-mini S&P 500 | `CME:ES1!` |
| E-mini NASDAQ | `CME:NQ1!` |
| E-mini Dow | `CBOT:YM1!` |
| E-mini Russell | `CME:RTY1!` |

### Commodity Futures

| Contract | Symbol |
|----------|--------|
| Gold | `COMEX:GC1!` |
| Silver | `COMEX:SI1!` |
| Crude Oil | `NYMEX:CL1!` |
| Natural Gas | `NYMEX:NG1!` |
| Corn | `CBOT:ZC1!` |
| Soybeans | `CBOT:ZS1!` |

### Currency Futures

| Contract | Symbol |
|----------|--------|
| Euro FX | `CME:6E1!` |
| British Pound | `CME:6B1!` |
| Japanese Yen | `CME:6J1!` |

## Multi-Timeframe

```python
fs = FuturesScreener()

# Daily trend
fs.where(FuturesField.PRICE > FuturesField.SIMPLE_MOVING_AVERAGE_50)

# 4-hour RSI
rsi_4h = FuturesField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
fs.where(rsi_4h.between(40, 60))

fs.select(
    FuturesField.NAME,
    FuturesField.PRICE,
    FuturesField.RELATIVE_STRENGTH_INDEX_14,
    rsi_4h
)

df = fs.get()
```

## All Fields

```python
fs = FuturesScreener()
fs.select_all()
fs.set_range(0, 100)

df = fs.get()
print(f"Columns: {len(df.columns)}")  # ~393
```

## Notes

- Futures symbols typically end with `1!` for the front-month contract
- Volume and open interest are key metrics for futures
- Different exchanges have different trading hours
