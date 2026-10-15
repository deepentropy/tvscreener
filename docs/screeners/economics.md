# Economics Screener

Screen economic indicators (GDP, employment, inflation, rates, trade...) for 190+ countries. About 15,000 indicators.

## Quick Start

```python
from tvscreener import EconomicsScreener, EconomicsField, EconomicCategory

es = EconomicsScreener()
es.where(EconomicsField.COUNTRY_CODE == 'US')
es.where(EconomicsField.ECONOMIC_CATEGORY_ID == EconomicCategory.LABOUR)
df = es.get()
```

## Fields

| Field | Description |
|-------|-------------|
| `NAME`, `DESCRIPTION` | Indicator code and name, e.g. `USUR` "United States Unemployment Rate" |
| `COUNTRY_CODE` | ISO country code |
| `ECONOMIC_CATEGORY_ID` | Category, see `EconomicCategory` |
| `CLOSE` | Latest value |
| `TIME` | Period of the latest value (converted to a UTC datetime) |
| `CHANGE`, `CHANGE_ABS` | Change from the previous period (% and absolute) |
| `VALUE_UNIT_ID` | Unit, e.g. `PCT`, `PSN` (persons), `POINT`, `BLL` (barrels) |
| `CURRENCY` | Currency of money values |

## Categories

`EconomicCategory`: `GDP`, `LABOUR`, `PRICES`, `MONEY`, `TRADE`, `GOVERNMENT`, `BUSINESS`, `CONSUMER`, `HOUSING`, `TAXES`, `HEALTH`, `ENERGY`, `CLIMATE`.

## Example: Inflation by Country

```python
es = EconomicsScreener()
es.where(EconomicsField.ECONOMIC_CATEGORY_ID == EconomicCategory.PRICES)
es.where(EconomicsField.NAME.match('IRYY$'))     # inflation rate YoY
es.set_range(0, 500)
df = es.get()
```
