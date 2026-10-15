# Filters API Reference

Filter operators and conditions for screening.

## FieldCondition

Created automatically when using comparison operators on fields.

```python
from tvscreener import StockField

# These create FieldCondition objects
condition1 = StockField.PRICE > 100
condition2 = StockField.PE_RATIO_TTM.between(10, 25)
condition3 = StockField.SECTOR.isin(['Electronic Technology', 'Health Technology'])
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `field` | `Field` | The field being compared |
| `operation` | `FilterOperator` | The comparison operator |
| `value` | `Any` | The comparison value |

### Methods

#### `to_filter()`

Convert to TradingView API filter format.

```python
condition = StockField.PRICE > 100
filter_dict = condition.to_filter()
# {'left': 'close', 'operation': 'greater', 'right': 100}
```

## FilterOperator

Enum of available filter operations.

```python
from tvscreener import FilterOperator
```

### Comparison Operators

| Operator | Python Syntax | FilterOperator |
|----------|---------------|----------------|
| Greater than | `>` | `FilterOperator.ABOVE` |
| Greater or equal | `>=` | `FilterOperator.ABOVE_OR_EQUAL` |
| Less than | `<` | `FilterOperator.BELOW` |
| Less or equal | `<=` | `FilterOperator.BELOW_OR_EQUAL` |
| Equal | `==` | `FilterOperator.EQUAL` |
| Not equal | `!=` | `FilterOperator.NOT_EQUAL` |

### Range Operators

| Method | FilterOperator |
|--------|----------------|
| `.between(min, max)` | `FilterOperator.IN_RANGE` |
| `.not_between(min, max)` | `FilterOperator.NOT_IN_RANGE` |

### List Operators

| Method | FilterOperator |
|--------|----------------|
| `.isin(values)` | `FilterOperator.IN_RANGE` |
| `.not_in(values)` | `FilterOperator.NOT_IN_RANGE` |

### Set, Empty and Date Operators

| Method | FilterOperator | API operation |
|--------|----------------|---------------|
| `.has(values)` | `FilterOperator.HAS` | `has` (any of the values) |
| `.has_none_of(values)` | `FilterOperator.HAS_NONE_OF` | `has_none_of` |
| `.is_empty()` | `FilterOperator.EMPTY` | `empty` |
| `.not_empty()` | `FilterOperator.NOT_EMPTY` | `nempty` |
| `.in_day_range(start, end)` | `FilterOperator.IN_DAY_RANGE` | `in_day_range` (day offsets from today) |

### Percent Operators

`other` is a field or a number. Percentages are converted to factors (`5` becomes `1.05`).

| Method | FilterOperator | Condition |
|--------|----------------|-----------|
| `.above_pct(other, pct)` | `FilterOperator.ABOVE_PERCENT` | field > other × (1 + pct/100) |
| `.below_pct(other, pct)` | `FilterOperator.BELOW_PERCENT` | field < other × (1 − pct/100) |
| `.within_pct(other, low, high)` | `FilterOperator.IN_RANGE_PERCENT` | other × (1 + low/100) ≤ field ≤ other × (1 + high/100) |
| `.not_within_pct(other, low, high)` | `FilterOperator.NOT_IN_RANGE_PERCENT` | outside that range |

## ConditionGroup

Created by combining conditions with `|` (OR) and `&` (AND). Sent to TradingView as a `filter2` tree.

```python
from tvscreener import StockField

group = (StockField.SECTOR == 'Finance') | (StockField.SECTOR == 'Utilities')
group = group & (StockField.MARKET_CAPITALIZATION > 1e11)
ss.where(group)
```

| Property / Method | Description |
|-------------------|-------------|
| `operator` | `"and"` or `"or"` |
| `operands` | `FieldCondition` and nested `ConditionGroup` objects. Nested groups with the same operator are flattened. |
| `conditions()` | Iterates over every `FieldCondition`, at any depth |
| `to_dict()` | The `filter2` dictionary |

## ExtraFilter

Special filters not tied to specific fields.

```python
from tvscreener import ExtraFilter, FilterOperator
```

### Available Extra Filters

| Filter | Description |
|--------|-------------|
| `ExtraFilter.PRIMARY` | Primary listing only |
| `ExtraFilter.CURRENT_TRADING_DAY` | Currently trading |

### Usage

```python
ss = StockScreener()
ss.add_filter(ExtraFilter.PRIMARY, FilterOperator.EQUAL, True)
ss.add_filter(ExtraFilter.CURRENT_TRADING_DAY, FilterOperator.EQUAL, True)
```

## Legacy Syntax

The original filter syntax is still supported:

```python
from tvscreener import StockScreener, StockField, FilterOperator

ss = StockScreener()

# Legacy syntax
ss.where(StockField.PRICE, FilterOperator.ABOVE, 100)
ss.where(StockField.VOLUME, FilterOperator.ABOVE_OR_EQUAL, 1_000_000)

# Equivalent new syntax
ss.where(StockField.PRICE > 100)
ss.where(StockField.VOLUME >= 1_000_000)
```

## Filter Chaining

All `where()` calls are combined with AND logic. Use `|` inside a call for OR (see ConditionGroup):

```python
ss = StockScreener()

# All conditions must be true
ss.where(StockField.PRICE > 50)           # AND
ss.where(StockField.PRICE < 500)          # AND
ss.where(StockField.VOLUME >= 1_000_000)  # AND
ss.where(StockField.PE_RATIO_TTM.between(10, 30))

df = ss.get()  # Returns stocks matching ALL conditions
```

## Type Validation

Filters are validated against the screener type:

```python
ss = StockScreener()

# Valid - StockField with StockScreener
ss.where(StockField.PRICE > 100)

# Invalid - CryptoField with StockScreener
# ss.where(CryptoField.PRICE > 100)  # Raises error
```

## Complex Filters Example

```python
from tvscreener import StockScreener, StockField, IndexSymbol

ss = StockScreener()

# Index filter
ss.set_index(IndexSymbol.SP500)

# Price range
ss.where(StockField.PRICE.between(20, 500))

# Volume filter
ss.where(StockField.VOLUME >= 500_000)

# Valuation filters
ss.where(StockField.PE_RATIO_TTM.between(5, 25))
ss.where(StockField.PRICE_TO_BOOK_FY < 5)

# Sector filter
ss.where(StockField.SECTOR.not_in(['Finance', 'Utilities']))

# Technical filter
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(30, 70))

# Performance filter
ss.where(StockField.CHANGE_PERCENT > 0)

df = ss.get()
```
