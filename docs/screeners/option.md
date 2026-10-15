# Option Screener

Screen option chains with greeks and implied volatility.

## Quick Start

```python
from tvscreener import OptionScreener, OptionField

os_ = OptionScreener("NASDAQ:AAPL")
df = os_.get()
```

An underlying symbol is required, with its exchange prefix (`NASDAQ:AAPL`, `AMEX:SPY`, `SP:SPX`, `NSE:NIFTY`). Several underlyings can be passed at once:

```python
os_ = OptionScreener("NASDAQ:AAPL", "NASDAQ:MSFT")
os_.set_underlying("AMEX:SPY")  # replaces the underlyings
```

!!! note "Chain size"
    A single underlying can have thousands of contracts (AAPL: ~3,500, SPX: ~29,000). The default range returns the first 150, sorted by expiration. Use `set_range()` or filters to get the rest.

## Fields

The Option Screener has access to **28 fields**:

```python
OptionField.UNDERLYING_SYMBOL        # e.g. NASDAQ:AAPL
OptionField.OPTION_TYPE              # "call" or "put"
OptionField.STRIKE
OptionField.EXPIRATION               # datetime in the result
OptionField.BID
OptionField.ASK
OptionField.BID_ASK_SPREAD_PCT
OptionField.THEORETICAL_PRICE
OptionField.IMPLIED_VOLATILITY       # mid IV
OptionField.BID_IMPLIED_VOLATILITY
OptionField.ASK_IMPLIED_VOLATILITY
OptionField.DELTA
OptionField.GAMMA
OptionField.THETA
OptionField.VEGA
OptionField.RHO
```

!!! warning
    - Implied volatilities are fractions: `0.27` means 27%.
    - Values close to expiration can be extreme (several hundred percent on same-day expirations).
    - The options scanner does not return last price, volume or open interest.
    - Data is delayed (`OptionField.DATA_DELAY`, in seconds).

## Example Screens

### Near-the-money Calls for one Expiration

```python
import datetime as dt

os_ = OptionScreener("NASDAQ:AAPL")
os_.where(OptionField.OPTION_TYPE == "call")
os_.where(OptionField.DELTA.between(0.4, 0.6))
os_.where(OptionField.EXPIRATION == dt.date(2026, 11, 20))

df = os_.get()
```

Expiration filters accept `date`, `datetime`, ISO strings (`"2026-11-20"`) or `YYYYMMDD` integers.

### Full Chain for a Strike Range

```python
os_ = OptionScreener("AMEX:SPY")
os_.where(OptionField.STRIKE.between(600, 700))
os_.sort_by(OptionField.STRIKE)
os_.set_range(0, 5000)

df = os_.get()
```

### Volatility Smile

```python
os_ = OptionScreener("NASDAQ:AAPL")
os_.where(OptionField.EXPIRATION == "2026-11-20")
os_.select(OptionField.STRIKE, OptionField.OPTION_TYPE, OptionField.IMPLIED_VOLATILITY)
os_.set_range(0, 1000)

df = os_.get()
smile = df.pivot_table(index="Strike", columns="Option Type", values="Implied Volatility")
```

`get_volatility_smile()` returns TradingView's fitted smile for one expiration directly, from its volatility chart:

```python
from tvscreener import get_volatility_smile

df = get_volatility_smile("NASDAQ:AAPL", "2026-11-13")                  # columns: strike, iv
df = get_volatility_smile("NASDAQ:AAPL", "2026-11-13", x="moneyness")   # log-moneyness, 0 at the money
df = get_volatility_smile("SP:SPX", "2026-11-13", root="SPXW")          # option root differs from the ticker
```

`iv` is a fraction. It raises `requests.HTTPError` (404) when the expiration does not exist.

## IV Term Structure

`get_iv_term_structure()` returns the implied volatility of an underlying by time to expiration.

```python
from tvscreener import get_iv_term_structure

df = get_iv_term_structure("NASDAQ:AAPL")
```

| Column | Description |
|--------|-------------|
| `kind` | `listed`: one point per listed expiration. `standard`: interpolated constant tenors (1w, 2w, 1m, 2m, 3m, 6m, 9m, 1y) |
| `tenor` | Span as text, e.g. `29d`, `3m` |
| `span_value`, `span_unit` | Span as returned by TradingView (`d`, `w`, `m`, `y`) |
| `days` | Span in days. Approximate for `w`, `m` and `y` (1m = 365/12 days) |
| `iv` | Implied volatility (fraction) |

It raises `requests.HTTPError` when the symbol is unknown or has no options.
