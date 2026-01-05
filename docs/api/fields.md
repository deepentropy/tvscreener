# Fields API Reference

Field enums provide type-safe access to screener data.

## Field Classes

| Class | Screener | Field Count |
|-------|----------|-------------|
| `StockField` | `StockScreener` | ~3,526 |
| `CryptoField` | `CryptoScreener` | ~3,108 |
| `ForexField` | `ForexScreener` | ~2,965 |
| `BondField` | `BondScreener` | ~201 |
| `FuturesField` | `FuturesScreener` | ~393 |
| `CoinField` | `CoinScreener` | ~3,026 |

## Import

```python
from tvscreener import StockField
from tvscreener.field import StockField, CryptoField, ForexField
```

## Comparison Operators

Fields support Python comparison operators for filtering:

### Numeric Comparisons

```python
StockField.PRICE > 100          # Greater than
StockField.PRICE >= 100         # Greater than or equal
StockField.PRICE < 100          # Less than
StockField.PRICE <= 100         # Less than or equal
StockField.PRICE == 100         # Equal to
StockField.PRICE != 100         # Not equal to
```

### Range Methods

```python
StockField.PRICE.between(50, 200)       # Value in range [50, 200]
StockField.PRICE.not_between(50, 200)   # Value outside range
```

### List Methods

```python
StockField.SECTOR.isin(['Technology', 'Healthcare'])
StockField.SECTOR.not_in(['Finance', 'Utilities'])
```

## Field Properties

Each field has accessible properties:

```python
field = StockField.PRICE

field.name          # Enum name: 'PRICE'
field.value         # Field definition tuple
field.label         # Human-readable label
field.field_name    # API field name
field.format        # Data format type
```

### Format Types

| Format | Description | Example Fields |
|--------|-------------|----------------|
| `currency` | Monetary values | PRICE, MARKET_CAP |
| `percent` | Percentage | CHANGE_PERCENT, ROE |
| `float` | Decimal number | PE_RATIO, RSI |
| `number_group` | Large numbers | VOLUME, SHARES |
| `text` | Text string | NAME, SECTOR |
| `bool` | True/False | IS_PRIMARY |
| `date` | Date | EX_DIVIDEND_DATE |

## Time Intervals

Technical fields support multiple timeframes:

```python
# Default (daily)
StockField.RELATIVE_STRENGTH_INDEX_14

# With specific interval
StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('60')   # 1 hour
StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('240')  # 4 hours
StockField.RELATIVE_STRENGTH_INDEX_14.with_interval('1W')   # Weekly
```

### Available Intervals

| Code | Timeframe |
|------|-----------|
| `'1'` | 1 minute |
| `'5'` | 5 minutes |
| `'15'` | 15 minutes |
| `'30'` | 30 minutes |
| `'60'` | 1 hour |
| `'120'` | 2 hours |
| `'240'` | 4 hours |
| `'1D'` | Daily |
| `'1W'` | Weekly |
| `'1M'` | Monthly |

## Historical Data

Some fields support historical lookback:

```python
# Previous day's RSI
StockField.RELATIVE_STRENGTH_INDEX_14.with_history(1)

# RSI from 5 days ago
StockField.RELATIVE_STRENGTH_INDEX_14.with_history(5)
```

## Field Discovery

### Search

Find fields by name:

```python
matches = StockField.search("dividend")
for field in matches[:10]:
    print(f"{field.name}: {field.label}")
```

### Presets

Get grouped fields:

```python
# Technical indicators
technicals = StockField.technicals()

# Oscillators
oscillators = StockField.oscillators()

# Moving averages
mas = StockField.moving_averages()

# Valuations
valuations = StockField.valuations()

# Dividends
dividends = StockField.dividends()

# Performance
performance = StockField.performance()

# Recommendations
recommendations = StockField.recommendations()
```

## Common Fields Reference

### Price & Volume

| Field | Description |
|-------|-------------|
| `PRICE` | Current price |
| `OPEN` | Day's open |
| `HIGH` | Day's high |
| `LOW` | Day's low |
| `CLOSE` | Previous close |
| `VOLUME` | Trading volume |
| `RELATIVE_VOLUME` | Volume vs average |

### Valuation

| Field | Description |
|-------|-------------|
| `PE_RATIO_TTM` | Price/Earnings (TTM) |
| `PRICE_TO_BOOK_FY` | Price/Book |
| `PRICE_TO_SALES_FY` | Price/Sales |
| `EV_TO_EBITDA_TTM` | EV/EBITDA |
| `PRICE_EARNINGS_TO_GROWTH_TTM` | PEG Ratio |
| `MARKET_CAPITALIZATION` | Market Cap |

### Dividends

| Field | Description |
|-------|-------------|
| `DIVIDEND_YIELD_FY` | Dividend Yield % |
| `DIVIDENDS_PER_SHARE_FY` | Dividend Per Share |
| `PAYOUT_RATIO_TTM` | Payout Ratio % |
| `EX_DIVIDEND_DATE` | Ex-Dividend Date |

### Technical

| Field | Description |
|-------|-------------|
| `RELATIVE_STRENGTH_INDEX_14` | RSI (14) |
| `MACD_LEVEL_12_26` | MACD Line |
| `MACD_SIGNAL_12_26` | MACD Signal |
| `SIMPLE_MOVING_AVERAGE_50` | SMA 50 |
| `SIMPLE_MOVING_AVERAGE_200` | SMA 200 |
| `EXPONENTIAL_MOVING_AVERAGE_20` | EMA 20 |
| `AVERAGE_TRUE_RANGE_14` | ATR (14) |
| `AVERAGE_DIRECTIONAL_INDEX_14` | ADX (14) |
| `STOCHASTIC_K_14_3_3` | Stochastic %K |
| `STOCHASTIC_D_14_3_3` | Stochastic %D |
| `BOLLINGER_UPPER_BAND_20` | BB Upper |
| `BOLLINGER_LOWER_BAND_20` | BB Lower |

### Performance

| Field | Description |
|-------|-------------|
| `CHANGE_PERCENT` | Today's Change % |
| `WEEKLY_PERFORMANCE` | 1 Week Change % |
| `MONTHLY_PERFORMANCE` | 1 Month Change % |
| `PERFORMANCE_3_MONTH` | 3 Month Change % |
| `PERFORMANCE_6_MONTH` | 6 Month Change % |
| `PERFORMANCE_YTD` | Year-to-Date % |
| `PERFORMANCE_1_YEAR` | 1 Year Change % |

### Profitability

| Field | Description |
|-------|-------------|
| `RETURN_ON_EQUITY_TTM` | ROE % |
| `RETURN_ON_ASSETS_TTM` | ROA % |
| `GROSS_MARGIN_TTM` | Gross Margin % |
| `NET_MARGIN_TTM` | Net Margin % |
| `OPERATING_MARGIN_TTM` | Operating Margin % |
