# Crypto Trading Strategies

Screen cryptocurrencies using various trading strategies.

## Market Cap Tiers

### Large Cap Only

Focus on established cryptocurrencies:

```python
from tvscreener import CryptoScreener, CryptoField

cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION > 10e9)  # >$10B
cs.sort_by(CryptoField.MARKET_CAPITALIZATION, ascending=False)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.MARKET_CAPITALIZATION,
    CryptoField.CHANGE_PERCENT
)

df = cs.get()
```

### Mid Cap Discovery

Find emerging projects:

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION.between(100e6, 1e9))
cs.where(CryptoField.VOLUME > 5_000_000)
cs.sort_by(CryptoField.CHANGE_PERCENT, ascending=False)

df = cs.get()
```

### Small Cap with Volume

High risk, high potential:

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION.between(10e6, 100e6))
cs.where(CryptoField.VOLUME > 1_000_000)  # Liquidity filter
cs.sort_by(CryptoField.WEEKLY_PERFORMANCE, ascending=False)

df = cs.get()
```

## Momentum Strategies

### Daily Gainers

```python
cs = CryptoScreener()
cs.where(CryptoField.CHANGE_PERCENT > 10)
cs.where(CryptoField.VOLUME > 10_000_000)
cs.sort_by(CryptoField.CHANGE_PERCENT, ascending=False)
cs.set_range(0, 50)

df = cs.get()
```

### Weekly Momentum

```python
cs = CryptoScreener()
cs.where(CryptoField.WEEKLY_PERFORMANCE > 30)
cs.where(CryptoField.MARKET_CAPITALIZATION > 100e6)
cs.sort_by(CryptoField.WEEKLY_PERFORMANCE, ascending=False)

df = cs.get()
```

### Monthly Breakouts

```python
cs = CryptoScreener()
cs.where(CryptoField.MONTHLY_PERFORMANCE > 50)
cs.where(CryptoField.VOLUME > 5_000_000)
cs.sort_by(CryptoField.MONTHLY_PERFORMANCE, ascending=False)

df = cs.get()
```

## Technical Analysis

### RSI Oversold

```python
cs = CryptoScreener()
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14 < 30)
cs.where(CryptoField.MARKET_CAPITALIZATION > 100e6)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.RELATIVE_STRENGTH_INDEX_14,
    CryptoField.CHANGE_PERCENT
)
cs.sort_by(CryptoField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = cs.get()
```

### RSI Overbought

Potential reversal candidates:

```python
cs = CryptoScreener()
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14 > 70)
cs.where(CryptoField.VOLUME > 10_000_000)
cs.sort_by(CryptoField.RELATIVE_STRENGTH_INDEX_14, ascending=False)

df = cs.get()
```

### MACD Bullish

```python
cs = CryptoScreener()
cs.where(CryptoField.MACD_LEVEL_12_26 > 0)
cs.where(CryptoField.VOLUME > 5_000_000)

df = cs.get()
```

### Above Moving Averages

Note: Field-to-field comparisons are NOT supported by the TradingView API.
Retrieve data and filter with pandas instead:

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION > 1e9)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.SIMPLE_MOVING_AVERAGE_50,
    CryptoField.SIMPLE_MOVING_AVERAGE_200
)

df = cs.get()

# Filter using pandas
bullish = df[
    (df['Price'] > df['SMA 50']) &
    (df['SMA 50'] > df['SMA 200'])
]

df = cs.get()
```

## Volume Analysis

### Volume Spike

Unusual volume activity:

```python
cs = CryptoScreener()
cs.where(CryptoField.RELATIVE_VOLUME > 3)  # 3x normal volume
cs.where(CryptoField.MARKET_CAPITALIZATION > 50e6)
cs.sort_by(CryptoField.RELATIVE_VOLUME, ascending=False)

df = cs.get()
```

### High Volume Movers

```python
cs = CryptoScreener()
cs.where(CryptoField.VOLUME > 100_000_000)
cs.where(CryptoField.CHANGE_PERCENT.not_between(-2, 2))  # Significant move
cs.sort_by(CryptoField.VOLUME, ascending=False)

df = cs.get()
```

## Multi-Timeframe

### Daily + Hourly RSI

```python
cs = CryptoScreener()

# Daily RSI moderate
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14.between(35, 50))

# Hourly RSI oversold
rsi_1h = CryptoField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
cs.where(rsi_1h < 30)

cs.where(CryptoField.MARKET_CAPITALIZATION > 500e6)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.RELATIVE_STRENGTH_INDEX_14,
    rsi_1h,
    CryptoField.CHANGE_PERCENT
)

df = cs.get()
```

### 4-Hour Trend Confirmation

```python
cs = CryptoScreener()

# Daily trend up
cs.where(CryptoField.PRICE > CryptoField.SIMPLE_MOVING_AVERAGE_50)

# 4-hour MACD bullish
macd_4h = CryptoField.MACD_LEVEL_12_26.with_interval('240')
cs.where(macd_4h > 0)

# 4-hour RSI not overbought
rsi_4h = CryptoField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
cs.where(rsi_4h < 65)

df = cs.get()
```

## Volatility Screens

### High Volatility

For active traders:

```python
cs = CryptoScreener()
cs.where(CryptoField.VOLATILITY > 5)
cs.where(CryptoField.VOLUME > 10_000_000)
cs.sort_by(CryptoField.VOLATILITY, ascending=False)

df = cs.get()
```

### Low Volatility Large Cap

For conservative positions:

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION > 5e9)
cs.where(CryptoField.VOLATILITY < 3)
cs.sort_by(CryptoField.MARKET_CAPITALIZATION, ascending=False)

df = cs.get()
```

## Recovery Screens

### Bouncing from Lows

```python
cs = CryptoScreener()
cs.where(CryptoField.MONTHLY_PERFORMANCE < -30)  # Down 30%+ monthly
cs.where(CryptoField.CHANGE_PERCENT > 5)          # Up today
cs.where(CryptoField.VOLUME > 5_000_000)
cs.sort_by(CryptoField.CHANGE_PERCENT, ascending=False)

df = cs.get()
```

### RSI Reversal Setup

```python
cs = CryptoScreener()
cs.where(CryptoField.RELATIVE_STRENGTH_INDEX_14.between(30, 40))
cs.where(CryptoField.CHANGE_PERCENT > 0)
cs.where(CryptoField.MARKET_CAPITALIZATION > 100e6)

df = cs.get()
```

## Specific Cryptos

Track specific assets:

```python
cs = CryptoScreener()
cs.symbols = {
    "query": {"types": []},
    "tickers": [
        "BINANCE:BTCUSDT",
        "BINANCE:ETHUSDT",
        "BINANCE:SOLUSDT",
        "BINANCE:ADAUSDT",
        "BINANCE:DOTUSDT"
    ]
}
cs.select_all()

df = cs.get()
```

## Streaming Monitor

Real-time updates:

```python
cs = CryptoScreener()
cs.where(CryptoField.MARKET_CAPITALIZATION > 1e9)
cs.sort_by(CryptoField.CHANGE_PERCENT, ascending=False)
cs.set_range(0, 20)
cs.select(
    CryptoField.NAME,
    CryptoField.PRICE,
    CryptoField.CHANGE_PERCENT,
    CryptoField.VOLUME
)

for df in cs.stream(interval=10):
    print("\n=== Top 20 Large Cap Movers ===")
    print(df)
```

## Notes

- Crypto markets are 24/7 - different dynamics than stocks
- Higher volatility requires stricter risk management
- Volume is crucial for entry/exit execution
- Consider timezone for volume patterns
