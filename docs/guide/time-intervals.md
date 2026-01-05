# Time Intervals

Use technical indicators on different timeframes with `with_interval()`.

## Overview

By default, technical indicators use daily data. Use `with_interval()` to analyze on different timeframes:

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()

# Hourly RSI
rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
ss.where(rsi_1h < 30)

df = ss.get()
```

## Available Intervals

| Timeframe | Code | Description |
|-----------|------|-------------|
| 1 minute | `'1'` | Intraday |
| 5 minutes | `'5'` | Intraday |
| 15 minutes | `'15'` | Intraday |
| 30 minutes | `'30'` | Intraday |
| 1 hour | `'60'` | Intraday |
| 2 hours | `'120'` | Intraday |
| 4 hours | `'240'` | Intraday |
| Daily | `'1D'` | Default |
| Weekly | `'1W'` | Longer term |
| Monthly | `'1M'` | Longer term |

## Syntax

```python
field.with_interval('interval_code')
```

## Examples

### RSI on Different Timeframes

```python
ss = StockScreener()

# Default daily RSI
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 40)

# 1-hour RSI
rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
ss.where(rsi_1h < 30)

# 4-hour RSI
rsi_4h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
ss.where(rsi_4h < 35)

df = ss.get()
```

### MACD on Multiple Timeframes

```python
ss = StockScreener()

# Daily MACD bullish
ss.where(StockField.MACD_LEVEL_12_26 > 0)

# Hourly MACD also bullish
macd_1h = StockField.MACD_LEVEL_12_26.with_interval('60')
ss.where(macd_1h > 0)

df = ss.get()
```

### Moving Averages

```python
ss = StockScreener()

# Price above weekly 50 SMA
sma50_weekly = StockField.SIMPLE_MOVING_AVERAGE_50.with_interval('1W')
ss.where(StockField.PRICE > sma50_weekly)

df = ss.get()
```

## Multi-Timeframe Analysis

### Higher Timeframe Confirmation

Confirm signals on multiple timeframes:

```python
ss = StockScreener()

# Daily trend: above 50 SMA
ss.where(StockField.PRICE > StockField.SIMPLE_MOVING_AVERAGE_50)

# Hourly momentum: RSI oversold
rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
ss.where(rsi_1h < 40)

# 15-minute entry: RSI bouncing
rsi_15m = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('15')
ss.where(rsi_15m.between(30, 50))

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.RELATIVE_STRENGTH_INDEX_14,  # Daily
    rsi_1h,   # Hourly
    rsi_15m   # 15-minute
)

df = ss.get()
```

### Weekly + Daily Confirmation

```python
ss = StockScreener()

# Weekly RSI not overbought
rsi_weekly = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('1W')
ss.where(rsi_weekly < 60)

# Daily RSI oversold (entry signal)
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 30)

df = ss.get()
```

### 4-Hour + 1-Hour MACD

```python
ss = StockScreener()

# 4-hour MACD positive (trend)
macd_4h = StockField.MACD_LEVEL_12_26.with_interval('240')
ss.where(macd_4h > 0)

# 1-hour MACD positive (entry signal)
macd_1h = StockField.MACD_LEVEL_12_26.with_interval('60')
ss.where(macd_1h > 0)

# Note: Field-to-field comparisons (e.g., MACD > Signal) are NOT supported.
# Retrieve data and filter with pandas instead.

df = ss.get()
```

## Selecting Interval Fields

Include interval fields in your selection:

```python
ss = StockScreener()

rsi_1h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')
rsi_4h = StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.RELATIVE_STRENGTH_INDEX_14,  # Daily (default)
    rsi_1h,  # Hourly
    rsi_4h   # 4-hour
)

df = ss.get()
```

## Which Fields Support Intervals?

Technical indicators support intervals:

- RSI, MACD, Stochastic, CCI, etc.
- Moving averages (SMA, EMA)
- Bollinger Bands
- ATR, ADX
- Volume indicators

Fundamental fields do NOT support intervals:

- P/E, P/B, Market Cap (these are point-in-time values)
- Revenue, Earnings, Margins
- Dividend data

## Best Practices

!!! tip "Start with Higher Timeframes"
    Use higher timeframes for trend direction, lower timeframes for entry timing.

!!! tip "Avoid Over-Filtering"
    More timeframes = fewer results. Start with 2-3 timeframes.

!!! tip "Match Your Trading Style"
    - Day trading: 1min, 5min, 15min
    - Swing trading: 1h, 4h, 1D
    - Position trading: 1D, 1W, 1M
