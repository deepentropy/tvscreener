# Stock Screening Examples

Practical examples for common stock screening strategies.

## Value Investing

### Low P/E Stocks

Find undervalued stocks by P/E ratio:

```python
from tvscreener import StockScreener, StockField, IndexSymbol

ss = StockScreener()
ss.set_index(IndexSymbol.SP500)

ss.where(StockField.PE_RATIO_TTM.between(5, 15))      # Low P/E
ss.where(StockField.PRICE_TO_BOOK_FY < 3)              # Low P/B
ss.where(StockField.MARKET_CAPITALIZATION > 10e9)      # Large cap

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PE_RATIO_TTM,
    StockField.PRICE_TO_BOOK_FY,
    StockField.DIVIDEND_YIELD_FY
)
ss.sort_by(StockField.PE_RATIO_TTM, ascending=True)

df = ss.get()
```

### Graham Number Stocks

Benjamin Graham's value criteria:

```python
ss = StockScreener()

ss.where(StockField.PE_RATIO_TTM < 15)
ss.where(StockField.PRICE_TO_BOOK_FY < 1.5)
ss.where(StockField.CURRENT_RATIO_FY > 2)              # Strong liquidity
ss.where(StockField.TOTAL_DEBT_TO_EQUITY_FY < 0.5)     # Low debt
ss.where(StockField.EARNINGS_PER_SHARE_DILUTED_TTM > 0) # Profitable

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PE_RATIO_TTM,
    StockField.PRICE_TO_BOOK_FY,
    StockField.CURRENT_RATIO_FY,
    StockField.TOTAL_DEBT_TO_EQUITY_FY
)

df = ss.get()
```

### PEG Ratio Screening

Growth at a reasonable price:

```python
ss = StockScreener()

ss.where(StockField.PRICE_EARNINGS_TO_GROWTH_TTM.between(0, 1))  # PEG < 1
ss.where(StockField.EARNINGS_PER_SHARE_DILUTED_GROWTH_TTM > 10)   # Growing earnings
ss.where(StockField.MARKET_CAPITALIZATION > 1e9)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PE_RATIO_TTM,
    StockField.PRICE_EARNINGS_TO_GROWTH_TTM,
    StockField.EARNINGS_PER_SHARE_DILUTED_GROWTH_TTM
)

df = ss.get()
```

## Dividend Investing

### High Dividend Yield

```python
ss = StockScreener()

ss.where(StockField.DIVIDEND_YIELD_FY > 4)             # Yield > 4%
ss.where(StockField.DIVIDENDS_PAID_FY < 0)             # Actually paying dividends
ss.where(StockField.PAYOUT_RATIO_TTM.between(20, 80))  # Sustainable payout
ss.where(StockField.MARKET_CAPITALIZATION > 5e9)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.DIVIDEND_YIELD_FY,
    StockField.PAYOUT_RATIO_TTM,
    StockField.DIVIDENDS_PER_SHARE_FY
)
ss.sort_by(StockField.DIVIDEND_YIELD_FY, ascending=False)

df = ss.get()
```

### Dividend Growth

Stocks with growing dividends:

```python
ss = StockScreener()

ss.where(StockField.DIVIDEND_YIELD_FY > 2)
ss.where(StockField.DPS_COMMON_STOCK_PRIMARY_ISSUE_GROWTH_FY > 5)  # Dividend growing
ss.where(StockField.PAYOUT_RATIO_TTM < 70)

ss.select(
    StockField.NAME,
    StockField.DIVIDEND_YIELD_FY,
    StockField.DPS_COMMON_STOCK_PRIMARY_ISSUE_GROWTH_FY,
    StockField.PAYOUT_RATIO_TTM
)

df = ss.get()
```

## Momentum Strategies

### Top Gainers Today

```python
ss = StockScreener()

ss.where(StockField.CHANGE_PERCENT > 5)               # Up > 5%
ss.where(StockField.VOLUME > 1_000_000)                # High volume
ss.where(StockField.PRICE > 5)                         # No penny stocks

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.VOLUME,
    StockField.RELATIVE_VOLUME
)
ss.sort_by(StockField.CHANGE_PERCENT, ascending=False)
ss.set_range(0, 50)

df = ss.get()
```

### 52-Week High Breakouts

```python
ss = StockScreener()

# Price near 52-week high
ss.where(StockField.PRICE_52_WEEK_HIGH > 0)            # Has 52w high data
ss.where(StockField.HIGH_52_WEEK_PERFORMANCE > -5)     # Within 5% of high
ss.where(StockField.VOLUME > 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PRICE_52_WEEK_HIGH,
    StockField.HIGH_52_WEEK_PERFORMANCE,
    StockField.VOLUME
)

df = ss.get()
```

### Strong 3-Month Momentum

```python
ss = StockScreener()
ss.set_index(IndexSymbol.SP500)

ss.where(StockField.PERFORMANCE_3_MONTH > 20)          # Up 20%+ in 3 months
ss.where(StockField.PERFORMANCE_1_MONTH > 5)           # Still trending up
ss.where(StockField.VOLUME >= 500_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.PERFORMANCE_1_MONTH,
    StockField.PERFORMANCE_3_MONTH,
    StockField.RELATIVE_STRENGTH_INDEX_14
)
ss.sort_by(StockField.PERFORMANCE_3_MONTH, ascending=False)

df = ss.get()
```

## Sector Analysis

### Technology Sector Screen

```python
ss = StockScreener()

ss.where(StockField.SECTOR == 'Electronic Technology')
ss.where(StockField.MARKET_CAPITALIZATION > 10e9)
ss.where(StockField.REVENUE_GROWTH_TTM > 10)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MARKET_CAPITALIZATION,
    StockField.REVENUE_GROWTH_TTM,
    StockField.PE_RATIO_TTM
)
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)

df = ss.get()
```

### Healthcare Growth Stocks

```python
ss = StockScreener()

ss.where(StockField.SECTOR.isin(['Health Technology', 'Health Services']))
ss.where(StockField.REVENUE_GROWTH_TTM > 15)
ss.where(StockField.MARKET_CAPITALIZATION.between(1e9, 50e9))  # Mid-cap

ss.select(
    StockField.NAME,
    StockField.SECTOR,
    StockField.MARKET_CAPITALIZATION,
    StockField.REVENUE_GROWTH_TTM,
    StockField.GROSS_MARGIN_TTM
)

df = ss.get()
```

## Quality Screens

### High ROE Stocks

```python
ss = StockScreener()
ss.set_index(IndexSymbol.SP500)

ss.where(StockField.RETURN_ON_EQUITY_TTM > 20)         # ROE > 20%
ss.where(StockField.RETURN_ON_ASSETS_TTM > 10)         # ROA > 10%
ss.where(StockField.TOTAL_DEBT_TO_EQUITY_FY < 1)       # Moderate debt

ss.select(
    StockField.NAME,
    StockField.RETURN_ON_EQUITY_TTM,
    StockField.RETURN_ON_ASSETS_TTM,
    StockField.GROSS_MARGIN_TTM,
    StockField.TOTAL_DEBT_TO_EQUITY_FY
)
ss.sort_by(StockField.RETURN_ON_EQUITY_TTM, ascending=False)

df = ss.get()
```

### Profitable and Growing

```python
ss = StockScreener()

ss.where(StockField.NET_MARGIN_TTM > 10)               # Profitable
ss.where(StockField.REVENUE_GROWTH_TTM > 10)           # Growing revenue
ss.where(StockField.EARNINGS_PER_SHARE_DILUTED_GROWTH_TTM > 10)  # Growing earnings
ss.where(StockField.FREE_CASH_FLOW_TTM > 0)            # Positive free cash flow

ss.select(
    StockField.NAME,
    StockField.NET_MARGIN_TTM,
    StockField.REVENUE_GROWTH_TTM,
    StockField.EARNINGS_PER_SHARE_DILUTED_GROWTH_TTM,
    StockField.FREE_CASH_FLOW_TTM
)

df = ss.get()
```

## Small Cap Discovery

### Small Cap Value

```python
ss = StockScreener()

ss.where(StockField.MARKET_CAPITALIZATION.between(300e6, 2e9))  # Small cap
ss.where(StockField.PE_RATIO_TTM.between(5, 15))
ss.where(StockField.VOLUME > 100_000)                           # Liquid enough

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MARKET_CAPITALIZATION,
    StockField.PE_RATIO_TTM,
    StockField.VOLUME
)

df = ss.get()
```

### Small Cap Growth

```python
ss = StockScreener()

ss.where(StockField.MARKET_CAPITALIZATION.between(300e6, 2e9))
ss.where(StockField.REVENUE_GROWTH_TTM > 25)
ss.where(StockField.GROSS_MARGIN_TTM > 40)

ss.select(
    StockField.NAME,
    StockField.MARKET_CAPITALIZATION,
    StockField.REVENUE_GROWTH_TTM,
    StockField.GROSS_MARGIN_TTM
)

df = ss.get()
```

## ETF Screening

### High-Volume ETFs

```python
from tvscreener import SymbolType

ss = StockScreener()
ss.set_symbol_types(SymbolType.ETF)

ss.where(StockField.VOLUME > 1_000_000)
ss.where(StockField.PRICE > 10)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.VOLUME,
    StockField.CHANGE_PERCENT
)
ss.sort_by(StockField.VOLUME, ascending=False)

df = ss.get()
```

## International Stocks

### Japanese Large Caps

```python
from tvscreener import Market

ss = StockScreener()
ss.set_markets(Market.JAPAN)

ss.where(StockField.MARKET_CAPITALIZATION > 10e9)
ss.where(StockField.VOLUME > 100_000)

ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.MARKET_CAPITALIZATION,
    StockField.PE_RATIO_TTM
)

df = ss.get()
```

### European Dividend Stocks

```python
ss = StockScreener()
ss.set_markets(Market.GERMANY)

ss.where(StockField.DIVIDEND_YIELD_FY > 3)
ss.where(StockField.MARKET_CAPITALIZATION > 5e9)

df = ss.get()
```
