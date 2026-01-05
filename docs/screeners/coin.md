# Coin Screener

Screen coins from CoinGecko data.

## Quick Start

```python
from tvscreener import CoinScreener, CoinField

cs = CoinScreener()
df = cs.get()
```

## Field Count

The Coin Screener has access to **~3,026 fields** covering:

- Price & market data
- On-chain metrics
- Technical indicators
- Performance data

## Difference from Crypto Screener

| Feature | CoinScreener | CryptoScreener |
|---------|--------------|----------------|
| Data Source | CoinGecko-style | TradingView exchanges |
| Focus | Coins/tokens | Trading pairs |
| Metrics | Market cap, supply | Exchange volume |

## Common Fields

### Price & Market

```python
CoinField.PRICE                  # Current price
CoinField.MARKET_CAPITALIZATION  # Market cap
CoinField.CHANGE_PERCENT         # 24h change
CoinField.VOLUME                 # 24h volume
```

### Technical

```python
CoinField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
CoinField.MACD_LEVEL_12_26              # MACD
CoinField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
CoinField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
```

### Performance

```python
CoinField.PERF_W                  # 7d change
CoinField.PERF_1M                 # 30d change
CoinField.PERF_YTD                # Year to date
CoinField.PERF_Y                  # 1 year
```

## Example Screens

### Top by Market Cap

```python
cs = CoinScreener()
cs.sort_by(CoinField.MARKET_CAP, ascending=False)
cs.set_range(0, 100)
cs.select(
    CoinField.NAME,
    CoinField.CLOSE,
    CoinField.MARKET_CAP,
    CoinField.CHANGE
)

df = cs.get()
```

### Top Gainers

```python
cs = CoinScreener()
cs.where(CoinField.CHANGE > 10)
cs.where(CoinField.MARKET_CAP > 10_000_000)  # Min $10M cap
cs.sort_by(CoinField.CHANGE, ascending=False)
cs.set_range(0, 50)

df = cs.get()
```

### Large Cap Oversold

```python
cs = CoinScreener()
cs.where(CoinField.MARKET_CAP > 1e9)  # $1B+ market cap
cs.where(CoinField.RELATIVE_STRENGTH_INDEX_14 < 35)
cs.select(
    CoinField.NAME,
    CoinField.CLOSE,
    CoinField.MARKET_CAP,
    CoinField.RELATIVE_STRENGTH_INDEX_14
)

df = cs.get()
```

### Weekly Momentum

```python
cs = CoinScreener()
cs.where(CoinField.PERF_W > 20)
cs.where(CoinField.MARKET_CAP > 100_000_000)
cs.sort_by(CoinField.PERF_W, ascending=False)

df = cs.get()
```

## Multi-Timeframe

```python
cs = CoinScreener()

# Daily RSI moderate
cs.where(CoinField.RELATIVE_STRENGTH_INDEX_14.between(40, 60))

# 4-hour RSI oversold
rsi_4h = CoinField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
cs.where(rsi_4h < 35)

cs.select(
    CoinField.NAME,
    CoinField.PRICE,
    CoinField.RELATIVE_STRENGTH_INDEX_14,
    rsi_4h
)

df = cs.get()
```

## All Fields

```python
cs = CoinScreener()
cs.select_all()
cs.set_range(0, 100)

df = cs.get()
print(f"Columns: {len(df.columns)}")  # ~3,026
```

## Notes

- CoinScreener focuses on individual coins/tokens
- Use CryptoScreener for exchange-specific trading pairs
- Market cap and supply data may differ from exchange data
