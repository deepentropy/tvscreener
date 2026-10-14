# Screeners API Reference

All screener classes share a common base API.

## Available Screeners

| Class | Import | Fields Class |
|-------|--------|--------------|
| `StockScreener` | `from tvscreener import StockScreener` | `StockField` |
| `CryptoScreener` | `from tvscreener import CryptoScreener` | `CryptoField` |
| `ForexScreener` | `from tvscreener import ForexScreener` | `ForexField` |
| `BondScreener` | `from tvscreener import BondScreener` | `BondField` |
| `FuturesScreener` | `from tvscreener import FuturesScreener` | `FuturesField` |
| `CoinScreener` | `from tvscreener import CoinScreener` | `CoinField` |
| `OptionScreener` | `from tvscreener import OptionScreener` | `OptionField` |

## Common Methods

### `get()`

Execute the query and return results as a pandas DataFrame.

```python
ss = StockScreener()
df = ss.get()
```

**Returns:** `pandas.DataFrame`

---

### `where(condition)`

Add a filter condition.

```python
# New syntax (v0.1.0+)
ss.where(StockField.PRICE > 100)
ss.where(StockField.PE_RATIO_TTM.between(10, 25))

# Legacy syntax
ss.where(StockField.PRICE, FilterOperator.ABOVE, 100)
```

**Parameters:**
- `condition`: A `FieldCondition` from comparison operators

**Returns:** `self` (for chaining)

---

### `select(*fields)`

Specify which fields to include in results.

```python
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.VOLUME
)
```

**Parameters:**
- `*fields`: One or more Field enum values

**Returns:** `self` (for chaining)

---

### `select_all()`

Select all available fields (~3,500 for stocks).

```python
ss.select_all()
```

**Returns:** `self` (for chaining)

---

### `sort_by(field, ascending=True)`

Sort results by a field.

```python
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)
```

**Parameters:**
- `field`: Field enum value to sort by
- `ascending`: `True` for ascending, `False` for descending

**Returns:** `self` (for chaining)

---

### `set_range(from_index, to_index)`

Set pagination range.

```python
ss.set_range(0, 100)  # First 100 results
ss.set_range(100, 200)  # Results 101-200
```

**Parameters:**
- `from_index`: Starting index (0-based)
- `to_index`: Ending index (exclusive), max 5000

**Returns:** `self` (for chaining)

---

### `search(query)`

Text search across name and description.

```python
ss.search('semiconductor')
```

**Parameters:**
- `query`: Search string

**Returns:** `self` (for chaining)

---

### `stream(interval=10)`

Stream results with periodic updates.

```python
for df in ss.stream(interval=5):
    print(df)
```

**Parameters:**
- `interval`: Seconds between updates (default: 10)

**Yields:** `pandas.DataFrame` on each update

---

## StockScreener-Specific Methods

### `set_index(*indices)`

Filter to index constituents (Stock only).

```python
from tvscreener import IndexSymbol

ss.set_index(IndexSymbol.SP500)
ss.set_index(IndexSymbol.NASDAQ_100, IndexSymbol.DOW_JONES)
```

**Parameters:**
- `*indices`: One or more `IndexSymbol` values

**Returns:** `self` (for chaining)

---

### `set_markets(*markets)`

Filter by market region.

```python
from tvscreener import Market

ss.set_markets(Market.AMERICA)
ss.set_markets(Market.JAPAN)
```

**Parameters:**
- `*markets`: One or more `Market` values

**Returns:** `self` (for chaining)

---

### `set_symbol_types(*types)`

Filter by security type.

```python
from tvscreener import SymbolType

ss.set_symbol_types(SymbolType.COMMON_STOCK)
ss.set_symbol_types(SymbolType.ETF)
```

**Parameters:**
- `*types`: One or more `SymbolType` values

**Returns:** `self` (for chaining)

---

## Properties

### `symbols`

Direct access to symbol configuration.

```python
ss.symbols = {
    "query": {"types": []},
    "tickers": ["NASDAQ:AAPL", "NYSE:IBM"]
}
```

---

## Method Chaining

All configuration methods return `self`, enabling fluent syntax:

```python
df = (
    StockScreener()
    .select(StockField.NAME, StockField.PRICE)
    .where(StockField.PRICE > 100)
    .sort_by(StockField.VOLUME, ascending=False)
    .set_range(0, 50)
    .get()
)
```

---

## Full Example

```python
from tvscreener import StockScreener, StockField, IndexSymbol

ss = StockScreener()

# Filter to S&P 500
ss.set_index(IndexSymbol.SP500)

# Add conditions
ss.where(StockField.PRICE.between(50, 500))
ss.where(StockField.PE_RATIO_TTM.between(10, 30))
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 50)

# Select fields
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PE_RATIO_TTM,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.MARKET_CAPITALIZATION
)

# Sort and paginate
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)
ss.set_range(0, 100)

# Execute
df = ss.get()
```
