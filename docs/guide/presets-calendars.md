# Presets and Calendars

## Presets

TradingView has server-side screens for stocks: market movers, all-time highs, large caps... `set_preset()` uses them. A preset brings its own filters and sort order.

```python
from tvscreener import StockScreener, StockField, Preset, Market

ss = StockScreener().set_preset(Preset.GAINERS)
df = ss.get()   # sorted by change, largest gain first

# Combine with your own filters
ss = StockScreener().set_preset(Preset.GAINERS)
ss.where(StockField.MARKET_CAPITALIZATION > 1e10)

# Another market
ss = StockScreener().set_markets(Market.GERMANY).set_preset(Preset.LOSERS)
```

Available presets: `GAINERS`, `LOSERS`, `MOST_VOLATILE`, `VOLUME_LEADERS`, `UNUSUAL_VOLUME`, `PRE_MARKET_MOST_ACTIVE`, `PRE_MARKET_GAPPERS`, `AFTER_HOURS_GAINERS`, `AFTER_HOURS_LOSERS`, `ALL_TIME_HIGH`, `ALL_TIME_LOW`, `ABOVE_52WK_HIGH`, `BELOW_52WK_LOW`, `OVERBOUGHT`, `OVERSOLD`, `LARGE_CAP`, `SMALL_CAP`, `PENNY_STOCKS`, `HIGH_DIVIDEND`, `HIGH_BETA`, `BEST_PERFORMING`, `MOST_EXPENSIVE`, `HIGHEST_REVENUE`, `HIGHEST_NET_INCOME`, `HIGHEST_CASH`, `HIGHEST_PROFIT_PER_EMPLOYEE`, `LARGEST_EMPLOYERS`, `EARNINGS`, `IPO_CALENDAR`.

!!! note "One market at a time"
    Most presets only exist on single-market scanners. With one market selected (America by default), the request goes to that market's scanner. With several markets, only `EARNINGS` and `IPO_CALENDAR` work; other presets return an error.

- `sort_by()` after `set_preset()` replaces the preset's order.
- `set_preset(None)` removes the preset. The default sort is not restored.

## Calendars

The calendar functions return one row per event in a date range. Dates are inclusive and in UTC. `markets` takes a `Market`, a list, or `Market.ALL`; the default is America.

### Earnings

```python
from tvscreener import get_earnings_calendar, Market

df = get_earnings_calendar("2026-10-12", "2026-10-18")
df = get_earnings_calendar("2026-10-15", markets=Market.ALL)   # one day, every market
```

| Column | Description |
|--------|-------------|
| `date` | Release date and time (UTC) |
| `time` | `before_open`, `after_close` or `unspecified` |
| `reported` | True when the release already happened |
| `eps_estimate`, `revenue_estimate` | Forecast for this release |
| `eps_actual`, `revenue_actual`, `*_surprise`, `*_surprise_pct` | Only for reported releases |
| `market_cap`, `currency` | Fundamentals currency (USD by default) |

### Dividends

```python
from tvscreener import get_dividends_calendar

df = get_dividends_calendar("2026-10-12", "2026-10-18")
```

Columns: `ex_date`, `payment_date`, `amount`, `dividend_yield` (%), `currency`.

### IPOs

```python
from tvscreener import get_ipo_calendar, Market

df = get_ipo_calendar("2026-10-01", "2026-10-31", markets=Market.ALL)
```

Columns: `date`, `status`, `offer_price`, `price_range`, `offered_shares`, `deal_amount`, `market_cap`. Values are in USD.

### Economic Events

`get_economic_calendar()` returns data releases, central bank decisions and speeches. It reads TradingView's economic calendar, not the scanner, so it takes countries instead of markets.

```python
from tvscreener import get_economic_calendar

df = get_economic_calendar("2026-10-12", "2026-10-18")                        # every country
df = get_economic_calendar("2026-10-15", countries=["US", "EU"], importance="high")
```

| Column | Description |
|--------|-------------|
| `date` | Release time (UTC) |
| `country`, `currency` | `EU` for the euro area |
| `title`, `indicator`, `period` | Event name, indicator and the period it covers (e.g. `Sep`) |
| `actual`, `forecast`, `previous` | Values; `actual` is empty until the release |
| `unit`, `scale` | e.g. `%`, or `K` / `M` / `B` |
| `importance` | `low`, `medium` or `high`. `importance=` keeps events at or above that level |
| `ticker` | Indicator symbol, e.g. `ECONOMICS:USEHS`, usable with `EconomicsScreener` and `get_symbol()` |
| `category`, `source`, `reference_date`, `id` | |

The server returns at most 2,000 events per request; longer ranges are split automatically.
