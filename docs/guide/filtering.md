# Filtering Guide

Complete reference for filtering screener results.

## Comparison Operators

Use Python operators directly on fields:

| Operator | Example | Description |
|----------|---------|-------------|
| `>` | `StockField.PRICE > 100` | Greater than |
| `>=` | `StockField.VOLUME >= 1e6` | Greater than or equal |
| `<` | `StockField.RSI < 30` | Less than |
| `<=` | `StockField.PE_RATIO_TTM <= 15` | Less than or equal |
| `==` | `StockField.COUNTRY == 'United States'` | Equal to |
| `!=` | `StockField.SECTOR != 'Finance'` | Not equal to |

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()
ss.where(StockField.PRICE > 50)
ss.where(StockField.PRICE < 200)
ss.where(StockField.VOLUME >= 500_000)
```

## Range Filters

### between(min, max)
Values within a range (inclusive):

```python
ss.where(StockField.PRICE.between(50, 200))
ss.where(StockField.PE_RATIO_TTM.between(10, 25))
ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 10e9))  # $1B - $10B
```

### not_between(min, max)
Values outside a range:

```python
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.not_between(30, 70))  # Overbought or oversold
```

## List Filters

### isin(values)
Match any value in a list:

```python
from tvscreener import Exchange, Sector

ss.where(StockField.EXCHANGE.isin([Exchange.NASDAQ, Exchange.NYSE]))
ss.where(StockField.SECTOR.isin(['Electronic Technology', 'Health Technology']))
```

### not_in(values)
Exclude values in a list:

```python
ss.where(StockField.SECTOR.not_in(['Finance', 'Utilities']))
```

## Chaining Filters

All filters are combined with AND logic:

```python
ss = StockScreener()
ss.where(StockField.PRICE > 10)                              # AND
ss.where(StockField.PRICE < 100)                             # AND
ss.where(StockField.VOLUME >= 1_000_000)                     # AND
ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 50e9)) # AND
ss.where(StockField.PE_RATIO_TTM.between(5, 25))

df = ss.get()
```

## OR and Nested Conditions

Combine conditions with `|` (OR) and `&` (AND). Python evaluates `|` and `&` before comparisons, so put each comparison in parentheses.

```python
ss = StockScreener()

# Finance OR Utilities
ss.where((StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities'))

# Nested: large cap AND (oversold OR overbought)
rsi = StockField.RELATIVE_STRENGTH_INDEX_14
ss.where((StockField.MARKET_CAPITALIZATION > 1e10) & ((rsi < 30) | (rsi > 70)))

df = ss.get()
```

Groups are sent as TradingView's `filter2` tree. Plain `where()` filters and every group are combined with AND.

## Set, Empty and Date Filters

```python
# Symbol type tags (typespecs): any of / none of
ss.where(StockField.TYPESPECS.has('etf'))
ss.where(StockField.TYPESPECS.has_none_of(['preferred', 'etn']))

# Field has a value / has no value
ss.where(StockField.DIVIDENDS_YIELD.not_empty())
ss.where(StockField.DIVIDENDS_YIELD.is_empty())

# Dates relative to today, in days (TradingView's day boundaries)
ss.where(StockField.UPCOMING_EARNINGS_DATE.in_day_range(0, 7))   # next week
ss.where(StockField.RECENT_EARNINGS_DATE.in_day_range(-7, 0))    # last week
```

## Percent Filters

Compare a field with a percentage of another field or a number.

```python
# Price more than 5% above SMA 50
ss.where(StockField.PRICE.above_pct(StockField.SIMPLE_MOVING_AVERAGE_50, 5))

# Price more than 10% below SMA 200
ss.where(StockField.PRICE.below_pct(StockField.SIMPLE_MOVING_AVERAGE_200, 10))

# Price within 5% of the all-time high
ss.where(StockField.PRICE.within_pct(StockField.ALL_TIME_HIGH, -5, 0))

# Price not within 10% of SMA 200, either side
ss.where(StockField.PRICE.not_within_pct(StockField.SIMPLE_MOVING_AVERAGE_200, -10, 10))
```

Percentages are converted to the factors TradingView expects: `above_pct(x, 5)` sends `above% [x, 1.05]`.

## Market Filters

### By Exchange

```python
from tvscreener import Exchange

ss.where(StockField.EXCHANGE == Exchange.NASDAQ)
# Or multiple:
ss.where(StockField.EXCHANGE.isin([Exchange.NASDAQ, Exchange.NYSE]))
```

### By Country

```python
ss.where(StockField.COUNTRY == 'United States')
```

### By Market Region

```python
from tvscreener import Market

ss = StockScreener()
ss.set_markets(Market.AMERICA)  # US stocks
# Or:
ss.set_markets(Market.JAPAN)
ss.set_markets(Market.GERMANY)
ss.set_markets(Market.ALL)  # Global
```

## Index Filters

Filter to index constituents:

```python
from tvscreener import IndexSymbol

ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.set_range(0, 500)
```

Available indices:

| Index | Symbol |
|-------|--------|
| S&P 500 | `IndexSymbol.SP500` |
| NASDAQ 100 | `IndexSymbol.NASDAQ_100` |
| Dow Jones | `IndexSymbol.DOW_JONES` |
| Russell 2000 | `IndexSymbol.RUSSELL_2000` |
| Russell 1000 | `IndexSymbol.RUSSELL_1000` |

Sector indices:

```python
ss.set_index(IndexSymbol.SP500_INFORMATION_TECHNOLOGY)
ss.set_index(IndexSymbol.SP500_HEALTH_CARE)
ss.set_index(IndexSymbol.PHLX_SEMICONDUCTOR)
```

Multiple indices:

```python
ss.set_index(IndexSymbol.SP500, IndexSymbol.NASDAQ_100)
```

## Symbol Type Filters

Filter by security type:

```python
from tvscreener import SymbolType

ss = StockScreener()
ss.set_symbol_types(SymbolType.COMMON_STOCK)
# Or multiple:
ss.set_symbol_types(SymbolType.COMMON_STOCK, SymbolType.ETF)
```

Available types:
- `SymbolType.COMMON_STOCK`
- `SymbolType.ETF`
- `SymbolType.PREFERRED_STOCK`
- `SymbolType.REIT`
- `SymbolType.CLOSED_END_FUND`
- `SymbolType.MUTUAL_FUND`

## Extra Filters

### Primary Listing Only

```python
from tvscreener import ExtraFilter, FilterOperator

ss.add_filter(ExtraFilter.PRIMARY, FilterOperator.EQUAL, True)
```

### Currently Trading

```python
ss.add_filter(ExtraFilter.CURRENT_TRADING_DAY, FilterOperator.EQUAL, True)
```

## Search

Text search across name and description:

```python
ss = StockScreener()
ss.search('semiconductor')
df = ss.get()
```

## Sorting

```python
ss = StockScreener()
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)  # Largest first
ss.sort_by(StockField.CHANGE_PERCENT, ascending=False)         # Top gainers
ss.sort_by(StockField.VOLUME, ascending=False)                  # Most active
```

## Pagination

```python
ss = StockScreener()
ss.set_range(0, 100)    # First 100 results
ss.set_range(100, 200)  # Next 100 results
ss.set_range(0, 1000)   # First 1000 results
```

## Complete Example

```python
from tvscreener import StockScreener, StockField, IndexSymbol, Exchange

ss = StockScreener()

# S&P 500 stocks only
ss.set_index(IndexSymbol.SP500)

# Price and volume filters
ss.where(StockField.PRICE.between(20, 500))
ss.where(StockField.VOLUME >= 500_000)

# Valuation filters
ss.where(StockField.PE_RATIO_TTM.between(5, 30))
ss.where(StockField.PRICE_TO_BOOK_FY < 5)

# Performance filter
ss.where(StockField.CHANGE_PERCENT > 0)  # Up today

# Technical filter
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(40, 60))

# Select fields
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUME,
    StockField.PE_RATIO_TTM,
    StockField.RELATIVE_STRENGTH_INDEX_14
)

# Sort by market cap
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)

# Get up to 500 results
ss.set_range(0, 500)

df = ss.get()
```
