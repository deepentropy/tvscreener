# Forex Screener

Screen currency pairs from the foreign exchange market.

## Quick Start

```python
from tvscreener import ForexScreener, ForexField

fs = ForexScreener()
df = fs.get()
```

## Field Count

The Forex Screener has access to **~2,965 fields** covering:

- Price & Volume data
- Technical indicators
- Performance metrics
- Currency-specific metrics

## Common Fields

### Price

```python
ForexField.PRICE           # Current price
ForexField.OPEN            # Day open
ForexField.HIGH            # Day high
ForexField.LOW             # Day low
ForexField.CHANGE_PERCENT  # Daily change
```

### Technical

```python
ForexField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
ForexField.MACD_LEVEL_12_26              # MACD
ForexField.MACD_SIGNAL_12_26             # MACD Signal
ForexField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
ForexField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
ForexField.EXPONENTIAL_MOVING_AVERAGE_20 # EMA 20
ForexField.AVERAGE_TRUE_RANGE_14         # ATR
ForexField.STOCHASTIC_K_14_3_3           # Stochastic %K
ForexField.STOCHASTIC_D_14_3_3           # Stochastic %D
```

### Performance

```python
ForexField.WEEKLY_PERFORMANCE      # 1 week change
ForexField.MONTHLY_PERFORMANCE     # 1 month change
ForexField.PERFORMANCE_3_MONTH     # 3 month change
ForexField.PERFORMANCE_YTD         # Year to date
ForexField.PERFORMANCE_1_YEAR      # 1 year
```

## Example Screens

### Major Pairs Only

```python
fs = ForexScreener()
fs.search("USD")  # Pairs containing USD
fs.set_range(0, 50)
fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.CHANGE_PERCENT
)

df = fs.get()
```

### Top Movers

```python
fs = ForexScreener()
fs.sort_by(ForexField.CHANGE_PERCENT, ascending=False)
fs.set_range(0, 20)
fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.CHANGE_PERCENT,
    ForexField.HIGH,
    ForexField.LOW
)

df = fs.get()
```

### Oversold RSI

```python
fs = ForexScreener()
fs.where(ForexField.RELATIVE_STRENGTH_INDEX_14 < 30)
fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.RELATIVE_STRENGTH_INDEX_14,
    ForexField.CHANGE_PERCENT
)
fs.sort_by(ForexField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = fs.get()
```

### Golden Cross Setup

Price above moving averages:

```python
fs = ForexScreener()
# Note: Field-to-field comparisons are NOT supported by the TradingView API.
# Retrieve data and filter with pandas instead:
fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.SIMPLE_MOVING_AVERAGE_50,
    ForexField.SIMPLE_MOVING_AVERAGE_200
)

df = fs.get()

# Filter for golden cross using pandas
golden_cross = df[
    (df['Price'] > df['SMA 50']) &
    (df['SMA 50'] > df['SMA 200'])
]
```

### High ATR (Volatility)

```python
fs = ForexScreener()
fs.where(ForexField.AVERAGE_TRUE_RANGE_14 > 0.01)
fs.sort_by(ForexField.AVERAGE_TRUE_RANGE_14, ascending=False)
fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.AVERAGE_TRUE_RANGE_14,
    ForexField.VOLATILITY
)

df = fs.get()
```

## Multi-Timeframe Analysis

```python
fs = ForexScreener()

# Daily RSI
fs.where(ForexField.RELATIVE_STRENGTH_INDEX_14.between(40, 60))

# 4-hour RSI oversold
rsi_4h = ForexField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')
fs.where(rsi_4h < 35)

# 1-hour MACD bullish
macd_1h = ForexField.MACD_LEVEL_12_26.with_interval('60')
fs.where(macd_1h > 0)

fs.select(
    ForexField.NAME,
    ForexField.PRICE,
    ForexField.RELATIVE_STRENGTH_INDEX_14,
    rsi_4h,
    macd_1h
)

df = fs.get()
```

## Specific Currency Pairs

Query specific pairs:

```python
fs = ForexScreener()
fs.symbols = {
    "query": {"types": []},
    "tickers": ["FX:EURUSD", "FX:GBPUSD", "FX:USDJPY", "FX:AUDUSD"]
}
fs.select_all()

df = fs.get()
```

## Major Pairs

Common major currency pairs:

| Pair | Exchange Symbol |
|------|-----------------|
| EUR/USD | `FX:EURUSD` |
| GBP/USD | `FX:GBPUSD` |
| USD/JPY | `FX:USDJPY` |
| USD/CHF | `FX:USDCHF` |
| AUD/USD | `FX:AUDUSD` |
| USD/CAD | `FX:USDCAD` |
| NZD/USD | `FX:NZDUSD` |

## All Fields

```python
fs = ForexScreener()
fs.select_all()
fs.set_range(0, 100)

df = fs.get()
print(f"Columns: {len(df.columns)}")  # ~2,965
```

## Notes

- Forex markets trade 24/5 (closed on weekends)
- Price represents exchange rate (base/quote)
- ATR and volatility help identify trading opportunities
