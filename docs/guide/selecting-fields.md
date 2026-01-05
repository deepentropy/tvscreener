# Selecting Fields

Control which data columns are returned in your results.

## Basic Selection

Use `select()` to choose specific fields:

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUME
)
df = ss.get()
```

## Select All Fields

Retrieve all ~3,500 available fields:

```python
ss = StockScreener()
ss.select_all()
df = ss.get()

print(f"Columns: {len(df.columns)}")  # ~3,500 columns
```

!!! note "Performance"
    `select_all()` returns a large DataFrame. Use it for exploration, then narrow down to needed fields.

## Field Discovery

### Search by Name

```python
# Find RSI-related fields
matches = StockField.search("rsi")
for field in matches[:10]:
    print(field.name)
```

### Technical Indicators

```python
# Get all technical indicator fields
technicals = StockField.technicals()
for field in technicals[:10]:
    print(field.name)
```

### Recommendations

```python
# Get analyst recommendation fields
recs = StockField.recommendations()
for field in recs:
    print(field.name)
```

## Field Presets

Pre-defined groups of commonly used fields:

```python
# Valuation fields
ss.select(*StockField.valuations())

# Dividend fields
ss.select(*StockField.dividends())

# Oscillator fields
ss.select(*StockField.oscillators())

# Moving averages
ss.select(*StockField.moving_averages())

# Performance fields
ss.select(*StockField.performance())
```

## Field Properties

Each field has properties you can inspect:

```python
field = StockField.PRICE

print(field.label)       # Human-readable name
print(field.field_name)  # API field name
print(field.format)      # Data format (currency, percent, etc.)
```

## Common Field Categories

### Price & Volume

```python
ss.select(
    StockField.PRICE,
    StockField.OPEN,
    StockField.HIGH,
    StockField.LOW,
    StockField.CLOSE,
    StockField.VOLUME
)
```

### Valuation

```python
ss.select(
    StockField.PE_RATIO_TTM,
    StockField.PRICE_TO_BOOK_FY,
    StockField.PRICE_TO_SALES_FY,
    StockField.EV_TO_EBITDA_TTM,
    StockField.MARKET_CAPITALIZATION
)
```

### Dividends

```python
ss.select(
    StockField.DIVIDEND_YIELD_FY,
    StockField.DIVIDENDS_PER_SHARE_FY,
    StockField.PAYOUT_RATIO_TTM,
    StockField.EX_DIVIDEND_DATE
)
```

### Performance

```python
ss.select(
    StockField.CHANGE_PERCENT,
    StockField.WEEKLY_PERFORMANCE,
    StockField.MONTHLY_PERFORMANCE,
    StockField.PERFORMANCE_3_MONTH,
    StockField.PERFORMANCE_6_MONTH,
    StockField.PERFORMANCE_YTD,
    StockField.PERFORMANCE_1_YEAR
)
```

### Technical Indicators

```python
ss.select(
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.MACD_LEVEL_12_26,
    StockField.MACD_SIGNAL_12_26,
    StockField.SIMPLE_MOVING_AVERAGE_50,
    StockField.SIMPLE_MOVING_AVERAGE_200,
    StockField.EXPONENTIAL_MOVING_AVERAGE_20,
    StockField.AVERAGE_TRUE_RANGE_14,
    StockField.BOLLINGER_UPPER_BAND_20,
    StockField.BOLLINGER_LOWER_BAND_20
)
```

### Profitability

```python
ss.select(
    StockField.RETURN_ON_EQUITY_TTM,
    StockField.RETURN_ON_ASSETS_TTM,
    StockField.GROSS_MARGIN_TTM,
    StockField.NET_MARGIN_TTM,
    StockField.OPERATING_MARGIN_TTM
)
```

## Combining Selection with Filtering

```python
ss = StockScreener()

# Filter
ss.where(StockField.PRICE > 10)
ss.where(StockField.MARKET_CAPITALIZATION > 1e9)

# Select (order doesn't matter)
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MARKET_CAPITALIZATION
)

df = ss.get()
```

## Chaining Methods

```python
df = (
    StockScreener()
    .select(StockField.NAME, StockField.PRICE, StockField.VOLUME)
    .where(StockField.PRICE > 100)
    .sort_by(StockField.VOLUME, ascending=False)
    .get()
)
```

## Default Fields

If you don't call `select()`, a default set of fields is returned:

```python
ss = StockScreener()
df = ss.get()
print(df.columns.tolist())
```

## Field Count by Screener

| Screener | Field Count |
|----------|-------------|
| Stock | ~3,526 |
| Crypto | ~3,108 |
| Forex | ~2,965 |
| Bond | ~201 |
| Futures | ~393 |
| Coin | ~3,026 |
