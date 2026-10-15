# Financials and Events

These functions read TradingView's data websocket, the one behind its charts and financials pages. No account is needed.

## Financial Statements

`get_financials()` returns the history of a company's statements, as on its TradingView financials pages.

```python
from tvscreener import get_financials

income = get_financials("NASDAQ:AAPL")                                   # annual income statement
balance = get_financials("NASDAQ:AAPL", "balance_sheet", "FQ")           # quarterly balance sheet
cash = get_financials("NYSE:JPM", "cash_flow", "TTM")                    # trailing twelve months
ratios = get_financials("NASDAQ:AAPL", "statistics", labels=False)       # field ids as columns

income["Total revenue"].pct_change()                                     # revenue growth
income.attrs["currency"]                                                 # 'USD'
```

| Parameter | Values |
|-----------|--------|
| `statement` | `income`, `balance_sheet`, `cash_flow`, `statistics` (ratios, per-share values, valuation...) |
| `period` | `FY` (annual), `FQ` (quarterly), `FH` (semi-annual), `TTM` (trailing twelve months, at each quarter end) |
| `labels` | `True`: readable columns (`Total revenue`). `False`: field ids (`total_revenue`) |

The result has one row per fiscal period, oldest first, indexed by the period label (`2025`, `2026-Q3`).

- The first column, `period_end`, is the period end date (UTC).
- The other columns are the statement items, in TradingView's order. Each item is followed by its sub-items.
- Items without data are left out.

Large companies have about 20 fiscal years and 32 quarters.

Banks, insurers and industrial companies have different statement layouts. The function uses the layout that matches the company's data.

!!! note
    Some periods do not apply to some statements or companies. For example, balance sheets have no `TTM`, and US companies have no `FH`. The result is then empty.

`get_fundamentals_config()` returns TradingView's catalogue of fundamental fields: id, name, statement, period and layout.

## Corporate Events

`get_corporate_events()` returns dividends, earnings releases and stock splits.

```python
from tvscreener import get_corporate_events

events = get_corporate_events("NASDAQ:AAPL")
events["dividends"]      # ex_date, payment_date, amount, net_amount
events["earnings"]       # date, fiscal_period_end, reported, eps_reported, eps_estimate, eps_diluted,
                         # revenue_actual, revenue_estimate
get_corporate_events("NASDAQ:NVDA", "splits")["splits"]   # date, numerator, denominator, ratio
```

- `earnings` includes the next scheduled release, with `reported` False and only estimates.
- `eps_reported` is the EPS TradingView compares with the estimate.
- `eps_diluted` is the diluted EPS from the income statement. It can differ after one-off items.
- `ratio` is 10 for a 10-for-1 split.

!!! note "Recent history only"
    Without an account, TradingView sends recent events only: about the last 20 dividends, 2 years of earnings, and the latest splits. For longer earnings history, use `get_financials()` (EPS and revenue go back 20 years).

## Seasonals

`get_seasonals()` returns the monthly returns of a symbol, one row per year, as on its seasonals page.

```python
from tvscreener import get_seasonals

df = get_seasonals("NASDAQ:AAPL")                          # last 10 years, % change per month
df = get_seasonals("BINANCE:BTCUSDT", 2018, 2025)
df = get_seasonals("NASDAQ:AAPL", absolute=True)           # price change instead of %

df.mean()                                                  # average return by month
(df > 0).mean()                                            # share of positive years by month
```

Columns are `Jan` to `Dec`. Months not reached yet are `NaN`. The current month is the change so far.

## Errors

Unknown symbols raise `ValueError` (`get_financials`) or `TradingViewWebSocketError` (`get_corporate_events`, `get_seasonals`).
