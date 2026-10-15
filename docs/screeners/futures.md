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
FuturesField.CLOSE           # Current price
FuturesField.OPEN            # Day open
FuturesField.HIGH            # Day high
FuturesField.LOW             # Day low
FuturesField.VOLUME          # Trading volume
FuturesField.CHANGE  # Daily change
```

### Technical

```python
FuturesField.RSI    # RSI(14)
FuturesField.MACD_MACD              # MACD
FuturesField.SMA50      # SMA 50
FuturesField.SMA200     # SMA 200
FuturesField.ATR         # ATR
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
    FuturesField.CLOSE,
    FuturesField.CHANGE,
    FuturesField.VOLUME
)

df = fs.get()
```

### Top Gainers

```python
fs = FuturesScreener()
fs.where(FuturesField.CHANGE > 2)
fs.sort_by(FuturesField.CHANGE, ascending=False)
fs.select(
    FuturesField.NAME,
    FuturesField.CLOSE,
    FuturesField.CHANGE
)

df = fs.get()
```

### Oversold RSI

```python
fs = FuturesScreener()
fs.where(FuturesField.RSI < 30)
fs.select(
    FuturesField.NAME,
    FuturesField.CLOSE,
    FuturesField.RSI
)
fs.sort_by(FuturesField.RSI, ascending=True)

df = fs.get()
```

### High Volatility

```python
fs = FuturesScreener()
fs.where(FuturesField.ATR > 0)
fs.sort_by(FuturesField.ATR, ascending=False)
fs.select(
    FuturesField.NAME,
    FuturesField.CLOSE,
    FuturesField.ATR,
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
fs.where(FuturesField.CLOSE > FuturesField.SMA50)

# 4-hour RSI
rsi_4h = FuturesField.RSI.with_interval('240')
fs.where(rsi_4h.between(40, 60))

fs.select(
    FuturesField.NAME,
    FuturesField.CLOSE,
    FuturesField.RSI,
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

## Forward Curve

`get_forward_curve()` returns every listed contract month of a futures root, sorted by expiration.

```python
from tvscreener import get_forward_curve

df = get_forward_curve("NYMEX:CL")       # crude oil
df = get_forward_curve("CME_MINI:ES1!")  # a continuous symbol works too

contango = df["close"].iloc[-1] > df["close"].iloc[0]
```

Columns: `symbol`, `name`, `description`, `expiration`, `close`, `change` (%), `volume`, `open_interest`, `currency`.
The result is empty when the root is unknown. `search_symbols("ES", type="futures")` finds roots.

## Notes

- Futures symbols typically end with `1!` for the front-month contract
- Volume and open interest are key metrics for futures
- Different exchanges have different trading hours
