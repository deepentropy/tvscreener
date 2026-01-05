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
BondField.PRICE           # Current price
BondField.YIELD           # Current yield
BondField.CHANGE_PERCENT  # Daily change
BondField.OPEN            # Day open
BondField.HIGH            # Day high
BondField.LOW             # Day low
```

### Technical

```python
BondField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
BondField.MACD_LEVEL_12_26              # MACD
BondField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
BondField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
```

### Performance

```python
BondField.PERF_ALL                # All time performance
```

## Example Screens

### All Bonds by Yield

```python
bs = BondScreener()
bs.sort_by(BondField.YIELD, ascending=False)
bs.set_range(0, 50)
bs.select(
    BondField.NAME,
    BondField.PRICE,
    BondField.YIELD,
    BondField.CHANGE_PERCENT
)

df = bs.get()
```

### Top Movers

```python
bs = BondScreener()
bs.sort_by(BondField.CHANGE_PERCENT, ascending=False)
bs.set_range(0, 20)
bs.select(
    BondField.NAME,
    BondField.PRICE,
    BondField.YIELD,
    BondField.CHANGE_PERCENT
)

df = bs.get()
```

### RSI Analysis

```python
bs = BondScreener()
bs.where(BondField.RELATIVE_STRENGTH_INDEX_14 < 40)
bs.select(
    BondField.NAME,
    BondField.YIELD,
    BondField.RELATIVE_STRENGTH_INDEX_14
)

df = bs.get()
```

## Specific Bonds

Query specific bonds:

```python
bs = BondScreener()
bs.symbols = {
    "query": {"types": []},
    "tickers": ["TVC:US10Y", "TVC:US02Y", "TVC:US30Y"]
}
bs.select_all()

df = bs.get()
```

## Common Bond Symbols

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
print(f"Columns: {len(df.columns)}")  # ~201
```

## Notes

- Bond yields move inversely to prices
- Government bonds are often used as safe-haven indicators
- Monitor yield spreads (e.g., 10Y-2Y) for economic signals
