# Scanner Helpers

Small functions for scanner endpoints that are not screener queries.

## One Symbol

`get_symbol()` returns any fields of one symbol as a dict keyed by API field name.

```python
from tvscreener import get_symbol, StockField

data = get_symbol(
    "NASDAQ:AAPL",
    StockField.PRICE,
    StockField.RELATIVE_STRENGTH_INDEX_14.with_interval("60"),
    StockField.RSI2.with_history(1),
    "earnings_fq_h",          # API names work too
)
data["close"], data["RSI|60"], data["RSI2[1]"]
```

It returns `None` when the symbol does not exist. Unknown field names return `None` values.

## Valid Filter Values

`get_enum_values()` returns the values TradingView accepts for enumerable fields. The result maps each value to its display name.

```python
from tvscreener import get_enum_values

values = get_enum_values("sector", "exchange", "issuer", "asset_class")
values["sector"]["Electronic Technology"]   # 'Electronic technology'
```

Use the keys (not the display names) in filters. `lang` changes the display names (`lang="fr"`).

## Field Catalogue

`metainfo()` lists the fields of a screener's market, with their type and allowed values.

```python
from tvscreener import CryptoScreener, get_metainfo

df = CryptoScreener().metainfo()
df = get_metainfo("economics2")       # any scanner market
```

!!! note
    The catalogue is partly generic. It can list fields that hold no data for that market.
