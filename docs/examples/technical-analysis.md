# Technical Analysis Examples

Screen stocks using technical indicators with multiple timeframes.

## RSI Strategies

### Oversold Stocks (RSI < 30)

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()

ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 30)
ss.where(StockField.VOLUME >= 500_000)
ss.where(StockField.PRICE > 5)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.VOLUME
)
ss.sort_by(StockField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = ss.get()
```

### Overbought Stocks (RSI > 70)

```python
ss = StockScreener()

ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 > 70)
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.CHANGE_PERCENT
)
ss.sort_by(StockField.RELATIVE_STRENGTH_INDEX_14, ascending=False)

df = ss.get()
```

### RSI Divergence Setup

RSI in neutral zone with strong price movement:

```python
ss = StockScreener()

ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(40, 60))
ss.where(StockField.CHANGE_PERCENT > 3)  # Price up but RSI neutral
ss.where(StockField.VOLUME >= 1_000_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.RELATIVE_STRENGTH_INDEX_14
)

df = ss.get()
```

## MACD Strategies

### MACD Bullish Signal

```python
ss = StockScreener()

ss.where(StockField.MACD_LEVEL_12_26 > 0)              # MACD above zero
ss.where(StockField.MACD_SIGNAL_12_26 > 0)             # Signal above zero
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MACD_LEVEL_12_26,
    StockField.MACD_SIGNAL_12_26,
    StockField.CHANGE_PERCENT
)

df = ss.get()
```

### MACD Histogram Expansion

Strong momentum with expanding histogram:

```python
ss = StockScreener()

# Note: Field-to-field comparisons (e.g., MACD > Signal) are NOT supported by the TradingView API.
# Retrieve data and filter with pandas instead:
ss.where(StockField.MACD_LEVEL_12_26 > 0)
ss.where(StockField.CHANGE_PERCENT > 2)
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MACD_LEVEL_12_26,
    StockField.MACD_SIGNAL_12_26
)

df = ss.get()

# Filter for MACD > Signal using pandas
bullish_macd = df[df['MACD (12, 26)'] > df['MACD Signal (12, 26)']]
```

## Moving Average Strategies

### Golden Cross Setup

Note: Field-to-field comparisons are NOT supported by the TradingView API.
Retrieve data and filter with pandas:

```python
ss = StockScreener()

ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.SIMPLE_MOVING_AVERAGE_50,
    StockField.SIMPLE_MOVING_AVERAGE_200,
    StockField.CHANGE_PERCENT
)

df = ss.get()
```

### Death Cross Warning

Bearish setup (retrieve data and filter with pandas):

```python
ss = StockScreener()

ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.SIMPLE_MOVING_AVERAGE_50,
    StockField.SIMPLE_MOVING_AVERAGE_200
)

df = ss.get()

# Filter for death cross using pandas
death_cross = df[
    (df['SMA50'] < df['SMA200']) &
    (df['Price'] < df['SMA50'])
]
```

### EMA Trend Following

Price above EMA stack (retrieve data and filter with pandas):

```python
ss = StockScreener()

ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.EXPONENTIAL_MOVING_AVERAGE_20,
    StockField.EXPONENTIAL_MOVING_AVERAGE_50,
    StockField.EXPONENTIAL_MOVING_AVERAGE_200
)

df = ss.get()

# Filter for EMA stack using pandas
ema_stack = df[
    (df['Price'] > df['EMA20']) &
    (df['EMA20'] > df['EMA50']) &
    (df['EMA50'] > df['EMA200'])
]
```

## Bollinger Bands

### Bollinger Squeeze

Low volatility, potential breakout:

```python
ss = StockScreener()

# Price near middle band (low volatility)
ss.where(StockField.BOLLINGER_UPPER_BAND_20 > 0)
ss.where(StockField.AVERAGE_TRUE_RANGE_14 < 2)  # Low ATR
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.BOLLINGER_LOWER_BAND_20,
    StockField.BOLLINGER_UPPER_BAND_20,
    StockField.AVERAGE_TRUE_RANGE_14
)

df = ss.get()
```

## Stochastic Oscillator

### Stochastic Oversold

```python
ss = StockScreener()

ss.where(StockField.STOCHASTIC_K_14_3_3 < 20)
ss.where(StockField.STOCHASTIC_D_14_3_3 < 20)
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.STOCHASTIC_K_14_3_3,
    StockField.STOCHASTIC_D_14_3_3
)

df = ss.get()
```

### Stochastic Bullish Cross

%K crossing above %D in oversold territory (retrieve data and filter with pandas):

```python
ss = StockScreener()

ss.where(StockField.STOCHASTIC_K_14_3_3 < 30)  # In oversold zone
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.STOCHASTIC_K_14_3_3,
    StockField.STOCHASTIC_D_14_3_3
)

df = ss.get()

# Filter for %K > %D (bullish cross) using pandas
bullish_stoch = df[df['Stoch %K'] > df['Stoch %D']]
```

## Multi-Timeframe Analysis

### Hourly RSI with Daily Filter

Use different timeframes for the same indicator:

```python
ss = StockScreener()

# Daily RSI oversold
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 40)

# Hourly RSI (use with_interval)
rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
ss.where(rsi_1h < 30)  # Even more oversold on hourly

ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    rsi_1h
)

df = ss.get()
```

### Multi-Timeframe MACD

```python
ss = StockScreener()

# Daily MACD bullish
ss.where(StockField.MACD_LEVEL_12_26 > 0)

# 4-hour MACD
macd_4h = StockField.MACD_LEVEL_12_26.with_interval('240')
ss.where(macd_4h > 0)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MACD_LEVEL_12_26,
    macd_4h
)

df = ss.get()
```

### Available Timeframes

| Interval | Code | Example |
|----------|------|---------|
| 1 minute | `'1'` | `.with_interval('1')` |
| 5 minutes | `'5'` | `.with_interval('5')` |
| 15 minutes | `'15'` | `.with_interval('15')` |
| 30 minutes | `'30'` | `.with_interval('30')` |
| 1 hour | `'60'` | `.with_interval('60')` |
| 2 hours | `'120'` | `.with_interval('120')` |
| 4 hours | `'240'` | `.with_interval('240')` |
| Daily | `'1D'` | `.with_interval('1D')` |
| Weekly | `'1W'` | `.with_interval('1W')` |
| Monthly | `'1M'` | `.with_interval('1M')` |

## ADX Trend Strength

### Strong Trending Stocks

```python
ss = StockScreener()

ss.where(StockField.AVERAGE_DIRECTIONAL_INDEX_14 > 25)  # Strong trend
ss.where(StockField.CHANGE_PERCENT > 0)                  # Uptrend
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.AVERAGE_DIRECTIONAL_INDEX_14,
    StockField.CHANGE_PERCENT
)

df = ss.get()
```

### Weak Trend (Range-Bound)

```python
ss = StockScreener()

ss.where(StockField.AVERAGE_DIRECTIONAL_INDEX_14 < 20)  # Weak trend
ss.where(StockField.VOLUME >= 500_000)

df = ss.get()
```

## Combined Technical Screens

### Momentum + Trend

```python
ss = StockScreener()

# Momentum confirmation (API-supported filters)
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(50, 70))
ss.where(StockField.MACD_LEVEL_12_26 > 0)

# Volume confirmation
ss.where(StockField.VOLUME >= 1_000_000)
ss.where(StockField.RELATIVE_VOLUME > 1)  # Above average volume

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.SIMPLE_MOVING_AVERAGE_50,
    StockField.SIMPLE_MOVING_AVERAGE_200,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.MACD_LEVEL_12_26,
    StockField.RELATIVE_VOLUME
)

df = ss.get()

# Filter for trend confirmation using pandas
# (Field-to-field comparisons must be done in pandas)
trending = df[
    (df['Price'] > df['SMA50']) &
    (df['SMA50'] > df['SMA200'])
]
```

### Oversold Bounce Setup

```python
ss = StockScreener()

# Oversold conditions
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 35)
ss.where(StockField.STOCHASTIC_K_14_3_3 < 25)

# But showing signs of reversal
ss.where(StockField.CHANGE_PERCENT > 0)  # Up today

# With volume
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.STOCHASTIC_K_14_3_3
)

df = ss.get()
```

### Support Level Test

Price near 200-day moving average (retrieve data and filter with pandas):

```python
ss = StockScreener()

# RSI not oversold (has room to bounce)
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(35, 50))

ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.SIMPLE_MOVING_AVERAGE_200,
    StockField.RELATIVE_STRENGTH_INDEX_14
)

df = ss.get()

# Filter for price within 3% of 200 SMA using pandas
# (Field-to-field comparisons must be done in pandas)
near_support = df[
    (df['Price'] > df['SMA200'] * 0.97) &
    (df['Price'] < df['SMA200'] * 1.03)
]
```

## Candlestick Patterns

### Bullish Engulfing

```python
ss = StockScreener()

ss.where(StockField.CANDLE_ENGULFING_BULLISH == True)
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.CANDLE_ENGULFING_BULLISH
)

df = ss.get()
```

### Morning Star

```python
ss = StockScreener()

ss.where(StockField.CANDLE_MORNINGSTAR == True)
ss.where(StockField.VOLUME >= 500_000)

df = ss.get()
```

### Doji at Support

```python
ss = StockScreener()

ss.where(StockField.CANDLE_DOJI == True)
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 40)  # Near oversold
ss.where(StockField.VOLUME >= 500_000)

df = ss.get()
```

## Volatility Screens

### High Volatility Stocks

```python
ss = StockScreener()

ss.where(StockField.AVERAGE_TRUE_RANGE_14 > 5)
ss.where(StockField.VOLATILITY > 3)
ss.where(StockField.VOLUME >= 1_000_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.AVERAGE_TRUE_RANGE_14,
    StockField.VOLATILITY
)

df = ss.get()
```

### Low Volatility Stocks

For conservative portfolios:

```python
ss = StockScreener()

ss.where(StockField.VOLATILITY_MONTH < 20)
ss.where(StockField.MARKET_CAPITALIZATION > 10e9)  # Large cap
ss.where(StockField.VOLUME >= 500_000)

df = ss.get()
```
