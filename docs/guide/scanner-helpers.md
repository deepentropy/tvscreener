# Scanner Helpers

Small functions for scanner endpoints that are not screener queries, and symbol search.

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

## Symbol Search

`search_symbols()` works like the search box on TradingView. It matches tickers, names, ISINs and CUSIPs, and returns exchange-prefixed symbols ready for the other functions.

```python
from tvscreener import search_symbols

df = search_symbols("apple", type="stock")
df = search_symbols("US0378331005")                 # by ISIN
df = search_symbols("SAP", exchange="XETR")
df = search_symbols("AAPL", country="DE")           # German listings first
df = search_symbols("gold", type="futures")         # futures are returned as roots, e.g. COMEX:GC
```

`type` is one of `stock`, `funds`, `futures`, `forex`, `crypto`, `index`, `bond`, `economic`.
Columns: `symbol`, `ticker`, `description`, `type`, `exchange`, `currency`, `country`, `isin`, `cusip`, `typespecs`, `is_primary_listing`.
`limit` caps the number of results (default 50).

## Peers

`get_peers()` returns the largest companies of the same industry and market, like the "related symbols" on a symbol page. The stock itself is excluded.

```python
from tvscreener import get_peers

df = get_peers("NASDAQ:AAPL")                 # 10 largest in the same industry
df = get_peers("XETR:SAP", n=5, by="sector")
```

Columns: `symbol`, `name`, `description`, `industry`, `sector`, `market_cap`, `close`, `change` (%), `currency`.
