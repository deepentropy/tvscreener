# ETF Screener

Screen ETFs and exchange-traded notes, like TradingView's ETF screener. Results are sorted by assets under management.

## Quick Start

```python
from tvscreener import ETFScreener, StockField

es = ETFScreener()
es.where(StockField.EXPENSE_RATIO < 0.1)
es.where(StockField.ASSET_CLASS_NAME == 'Equity')
df = es.get()
```

`ETFScreener` is a `StockScreener` limited to ETFs (`typespecs` has `etf`) and structured products. Every `StockField` works: price, performance, technical indicators...

## ETF Fields

| Field | Description |
|-------|-------------|
| `AUM` | Assets under management |
| `EXPENSE_RATIO` | Expense ratio (%) |
| `NAV`, `NAV_DISCOUNT_PREMIUM` | Net asset value and discount/premium to NAV |
| `NAV_TOTAL_RETURN_1M` ... `NAV_TOTAL_RETURN_5Y` | NAV total return |
| `FUND_FLOWS_1M` ... `FUND_FLOWS_5Y` | Fund flows |
| `ETF_HOLDINGS_COUNT` | Number of holdings |
| `ISSUER`, `BRAND`, `INDEX_PROVIDER`, `INDEX_TRACKED` | Issuer and index |
| `ASSET_CLASS_NAME`, `CATEGORY_NAME`, `FOCUS_NAME`, `NICHE_NAME`, `STRATEGY_NAME` | Classification |
| `SELECTION_CRITERIA_NAME`, `WEIGHTING_SCHEME_NAME`, `HOLDINGS_REGION_NAME` | Index method and region |
| `LEVERAGED_FLAG`, `LEVERAGE_RATIO`, `ACTIVELY_MANAGED_NAME` | Leverage and management |
| `DIVIDEND_TREATMENT`, `DIVIDENDS_FREQUENCY` | Distribution policy |

!!! note "Codes and names"
    `ASSET_CLASS`, `CATEGORY`, `FOCUS`, `NICHE`, `STRATEGY`, `SELECTION_CRITERIA`, `WEIGHTING_SCHEME`, `HOLDINGS_REGION`, `ACTIVELY_MANAGED` and `K1_FORM` hold TradingView codes. The `*_NAME` fields hold the readable English names, and filters work on both.

## Examples

### Cheapest Large-Cap Equity ETFs

```python
es = ETFScreener()
es.where(StockField.FOCUS_NAME == 'Large cap')
es.where(StockField.AUM > 1e9)
es.sort_by(StockField.EXPENSE_RATIO, ascending=True)
df = es.get()
```

### Largest Inflows over 3 Months

```python
es = ETFScreener()
es.sort_by(StockField.FUND_FLOWS_3M, ascending=False)
es.set_range(0, 20)
df = es.get()
```
