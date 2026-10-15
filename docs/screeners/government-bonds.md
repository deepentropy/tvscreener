# Government Bonds and Yield Curves

Benchmark government bonds of about 50 countries, by tenor (1 month to 50 years). Each tenor has two series:

- the **yield**, e.g. `TVC:US10Y` (`CLOSE` in percent)
- the **price**, e.g. `TVC:US10`

`BondScreener` covers individual corporate and government bonds instead.

## Yield Curve

```python
from tvscreener import get_yield_curve

df = get_yield_curve("US")
```

| Column | Description |
|--------|-------------|
| `tenor` | `1M`, `3M`, `1Y`, `10Y`... |
| `days_to_maturity`, `maturity_date` | Maturity of the benchmark bond |
| `yield` | Yield in percent |
| `change` | Yield change since the previous close (percentage points) |

## Screener

```python
from tvscreener import GovernmentBondScreener, GovernmentBondField

gs = GovernmentBondScreener().yields_only()
gs.where(GovernmentBondField.COUNTRY_CODE.isin(['DE', 'FR', 'IT']))
gs.where(GovernmentBondField.NAME.match('10Y$'))
df = gs.get()     # 10-year yields of Germany, France and Italy
```

- `yields_only()` / `prices_only()` keep one of the two series.
- Results are sorted by days to maturity. `MATURITY_DATE` is converted to a datetime.
