# Bond Screener

Screen government and corporate bonds.

## Quick Start

```python
from tvscreener import BondScreener, BondField

bs = BondScreener()
df = bs.get()
```

## Field Count

The Bond Screener has access to **~201 fields** covering:

- Yield and price data
- Maturity information
- Credit ratings
- Technical indicators

## Common Fields

### Price & Yield

```python
BondField.CLOSE           # Current price
BondField.CURRENT_YIELD           # Current yield
BondField.CHANGE  # Daily change
BondField.OPEN            # Day open
BondField.HIGH            # Day high
BondField.LOW             # Day low
```

### Risk

```python
BondField.YIELD_TO_MATURITY       # Yield to maturity
BondField.MODIFIED_DURATION       # Modified duration
BondField.CONVEXITY               # Convexity
BondField.Z_SPREAD                # Z-spread
BondField.CURRENT_COUPON          # Coupon rate
```

### Performance

```python
```

## Example Screens

### All Bonds by Yield

```python
bs = BondScreener()
bs.sort_by(BondField.CURRENT_YIELD, ascending=False)
bs.set_range(0, 50)
bs.select(
    BondField.NAME,
    BondField.CLOSE,
    BondField.CURRENT_YIELD,
    BondField.CHANGE
)

df = bs.get()
```

### Top Movers

```python
bs = BondScreener()
bs.sort_by(BondField.CHANGE, ascending=False)
bs.set_range(0, 20)
bs.select(
    BondField.NAME,
    BondField.CLOSE,
    BondField.CURRENT_YIELD,
    BondField.CHANGE
)

df = bs.get()
```

### Long Duration, High Yield

```python
bs = BondScreener()
bs.where(BondField.MODIFIED_DURATION > 10)
bs.where(BondField.YIELD_TO_MATURITY > 5)
bs.select(
    BondField.NAME,
    BondField.YIELD_TO_MATURITY,
    BondField.MODIFIED_DURATION
)

df = bs.get()
```

## Government Benchmark Yields

`BondScreener` covers individual bonds. Benchmark government yields such as `TVC:US10Y` are in
[`GovernmentBondScreener`](government-bonds.md), with `get_yield_curve("US")` for a whole curve.

## Common Benchmark Symbols (GovernmentBondScreener)

| Bond | Symbol |
|------|--------|
| US 10-Year | `TVC:US10Y` |
| US 2-Year | `TVC:US02Y` |
| US 30-Year | `TVC:US30Y` |
| US 5-Year | `TVC:US05Y` |
| German 10-Year | `TVC:DE10Y` |
| UK 10-Year | `TVC:GB10Y` |
| Japan 10-Year | `TVC:JP10Y` |

## All Fields

```python
bs = BondScreener()
bs.select_all()
bs.set_range(0, 100)

df = bs.get()
print(f"Columns: {len(df.columns)}")
```

## Notes

- Bond yields move inversely to prices
- Government bonds are often used as safe-haven indicators
- Monitor yield spreads (e.g., 10Y-2Y) for economic signals
