# Crypto Screener

Screen cryptocurrencies across major exchanges.

## Quick Start

```python
from tvscreener import CryptoScreener, CryptoField

cs = CryptoScreener()
df = cs.get()
```

## Field Count

The Crypto Screener has access to **~3,108 fields** covering:

- Price & Volume data
- Market metrics (market cap, circulating supply)
- Technical indicators
- Performance metrics

## Common Fields

### Price & Volume

```python
CryptoField.PRICE           # Current price
CryptoField.OPEN            # Day open
CryptoField.HIGH            # Day high
CryptoField.LOW             # Day low
CryptoField.VOLUME          # 24h volume
CryptoField.CHANGE_PERCENT  # 24h change
```

### Market Data

```python
CryptoField.MARKET_CAPITALIZATION    # Market cap
CryptoField.CIRCULATING_SUPPLY       # Circulating supply
CryptoField.TOTAL_SUPPLY             # Total supply
```

### Technical

```python
CryptoField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
CryptoField.MACD_LEVEL_12_26              # MACD
CryptoField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
CryptoField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
CryptoField.AVERAGE_TRUE_RANGE_14         # ATR
CryptoField.VOLATILITY                    # Daily volatility
```

### Performance

```python
CryptoField.WEEKLY_PERFORMANCE      # 7d change
CryptoField.MONTHLY_PERFORMANCE     # 30d change
CryptoField.PERFORMANCE_3_MONTH     # 90d change
CryptoField.PERFORMANCE_YTD         # Year to date
CryptoField.PERFORMANCE_1_YEAR      # 1 year
```

## Example Screens

### Top Market Cap

```python
cs = CryptoScreener()
cs.sort_by(CryptoField.MARKET_CAPITALIZATION, ascending=False)
cs.set_range(0, 100)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.MARKET_CAPITALIZATION,
    CryptoField.CHANGE_PERCENT
)

df = cs.get()
```

### High Volume Gainers

```python
cs = CryptoScreener()
cs.where(CryptoField.CHANGE_PERCENT > 10)
cs.where(CryptoField.VOLUME > 10_000_000)
cs.sort_by(CryptoField.CHANGE_PERCENT, ascending=False)
cs.set_range(0, 50)

df = cs.get()
```

### Oversold RSI

```python
cs = CryptoScreener()
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14 < 30)
cs.where(CryptoField.MARKET_CAPITALIZATION > 100_000_000)
cs.sort_by(CryptoField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = cs.get()
```

### Large Cap with Low Volatility

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION > 1e9)
cs.where(CryptoField.VOLATILITY < 5)
cs.sort_by(CryptoField.MARKET_CAPITALIZATION, ascending=False)

df = cs.get()
```

### Weekly Momentum

```python
cs = CryptoScreener()
cs.where(CryptoField.WEEKLY_PERFORMANCE > 20)
cs.where(CryptoField.VOLUME > 5_000_000)
cs.sort_by(CryptoField.WEEKLY_PERFORMANCE, ascending=False)

df = cs.get()
```

## Multi-Timeframe Analysis

```python
cs = CryptoScreener()

# Daily RSI oversold
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14 < 35)

# 4-hour RSI also oversold
rsi_4h = CryptoField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
cs.where(rsi_4h < 30)

cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.RELATIVE_STRENGTH_INDEX_14,
    rsi_4h
)

df = cs.get()
```

## Specific Cryptos

Query specific cryptocurrencies:

```python
cs = CryptoScreener()
cs.symbols = {
    "query": {"types": []},
    "tickers": ["BINANCE:BTCUSDT", "BINANCE:ETHUSDT", "BINANCE:SOLUSDT"]
}
cs.select_all()

df = cs.get()
```

## All Fields

```python
cs = CryptoScreener()
cs.select_all()
cs.set_range(0, 100)

df = cs.get()
print(f"Columns: {len(df.columns)}")  # ~3,108
```

## Notes

- Crypto markets trade 24/7 - volume is typically 24h volume
- Prices are quoted in various currencies depending on the exchange pair
- Use exchange prefix for specific pairs (e.g., `BINANCE:BTCUSDT`)
