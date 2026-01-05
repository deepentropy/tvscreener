# Stock Screener

Screen stocks from global exchanges including NYSE, NASDAQ, and international markets.

## Quick Start

```python
from tvscreener import StockScreener, StockField

ss = StockScreener()
df = ss.get()
```

## Field Count

The Stock Screener has access to **~3,526 fields** covering:

- Price & Volume data
- Fundamental metrics (valuation, profitability, dividends)
- Technical indicators (oscillators, moving averages, patterns)
- Analyst ratings and recommendations

## Unique Features

### Index Filtering

Filter to index constituents:

```python
from tvscreener import IndexSymbol

ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.set_range(0, 500)
df = ss.get()
```

Available indices:

| Index | Symbol |
|-------|--------|
| S&P 500 | `IndexSymbol.SP500` |
| NASDAQ 100 | `IndexSymbol.NASDAQ_100` |
| Dow Jones | `IndexSymbol.DOW_JONES` |
| Russell 2000 | `IndexSymbol.RUSSELL_2000` |
| Russell 1000 | `IndexSymbol.RUSSELL_1000` |

Sector indices:

```python
ss.set_index(IndexSymbol.SP500_INFORMATION_TECHNOLOGY)
ss.set_index(IndexSymbol.SP500_HEALTH_CARE)
ss.set_index(IndexSymbol.PHLX_SEMICONDUCTOR)
```

Multiple indices:

```python
ss.set_index(IndexSymbol.SP500, IndexSymbol.NASDAQ_100)
```

Search for indices:

```python
results = IndexSymbol.search("technology")
for idx in results:
    print(idx.name)
```

### Market Filtering

```python
from tvscreener import Market

ss = StockScreener()
ss.set_markets(Market.AMERICA)  # US stocks
ss.set_markets(Market.JAPAN)    # Japanese stocks
ss.set_markets(Market.GERMANY)  # German stocks
ss.set_markets(Market.ALL)      # Global
```

### Symbol Type Filtering

```python
from tvscreener import SymbolType

ss = StockScreener()
ss.set_symbol_types(SymbolType.COMMON_STOCK)
ss.set_symbol_types(SymbolType.ETF)
ss.set_symbol_types(SymbolType.PREFERRED_STOCK)
ss.set_symbol_types(SymbolType.REIT)
```

## Common Fields

### Price & Volume

```python
StockField.PRICE           # Current price
StockField.OPEN            # Day open
StockField.HIGH            # Day high
StockField.LOW             # Day low
StockField.CLOSE           # Previous close
StockField.VOLUME          # Trading volume
StockField.RELATIVE_VOLUME # Volume vs average
```

### Valuation

```python
StockField.PE_RATIO_TTM              # Price/Earnings
StockField.PRICE_TO_BOOK_FY          # Price/Book
StockField.PRICE_TO_SALES_FY         # Price/Sales
StockField.EV_TO_EBITDA_TTM          # EV/EBITDA
StockField.PRICE_EARNINGS_TO_GROWTH_TTM  # PEG Ratio
StockField.MARKET_CAPITALIZATION     # Market Cap
```

### Dividends

```python
StockField.DIVIDEND_YIELD_FY        # Yield %
StockField.DIVIDENDS_PER_SHARE_FY   # DPS
StockField.PAYOUT_RATIO_TTM         # Payout Ratio
StockField.EX_DIVIDEND_DATE         # Ex-Date
```

### Profitability

```python
StockField.RETURN_ON_EQUITY_TTM     # ROE
StockField.RETURN_ON_ASSETS_TTM     # ROA
StockField.GROSS_MARGIN_TTM         # Gross Margin
StockField.NET_MARGIN_TTM           # Net Margin
StockField.OPERATING_MARGIN_TTM     # Operating Margin
```

### Technical

```python
StockField.RELATIVE_STRENGTH_INDEX_14    # RSI(14)
StockField.MACD_LEVEL_12_26              # MACD
StockField.MACD_SIGNAL_12_26             # MACD Signal
StockField.SIMPLE_MOVING_AVERAGE_50      # SMA 50
StockField.SIMPLE_MOVING_AVERAGE_200     # SMA 200
StockField.EXPONENTIAL_MOVING_AVERAGE_20 # EMA 20
StockField.AVERAGE_TRUE_RANGE_14         # ATR
StockField.AVERAGE_DIRECTIONAL_INDEX_14  # ADX
```

### Performance

```python
StockField.CHANGE_PERCENT          # Today's change
StockField.WEEKLY_PERFORMANCE      # 1 week
StockField.MONTHLY_PERFORMANCE     # 1 month
StockField.PERFORMANCE_3_MONTH     # 3 months
StockField.PERFORMANCE_6_MONTH     # 6 months
StockField.PERFORMANCE_YTD         # Year to date
StockField.PERFORMANCE_1_YEAR      # 1 year
```

## Example Screens

### Value Stocks

```python
ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.where(StockField.PE_RATIO_TTM.between(5, 15))
ss.where(StockField.PRICE_TO_BOOK_FY < 3)
ss.where(StockField.MARKET_CAPITALIZATION > 10e9)
ss.sort_by(StockField.PE_RATIO_TTM, ascending=True)

df = ss.get()
```

### High Dividend Yield

```python
ss = StockScreener()
ss.where(StockField.DIVIDEND_YIELD_FY > 4)
ss.where(StockField.PAYOUT_RATIO_TTM.between(20, 80))
ss.where(StockField.MARKET_CAPITALIZATION > 5e9)
ss.sort_by(StockField.DIVIDEND_YIELD_FY, ascending=False)

df = ss.get()
```

### Momentum

```python
ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.where(StockField.PERFORMANCE_3_MONTH > 20)
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14.between(50, 70))
ss.sort_by(StockField.PERFORMANCE_3_MONTH, ascending=False)

df = ss.get()
```

### Oversold RSI

```python
ss = StockScreener()
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 30)
ss.where(StockField.VOLUME >= 500_000)
ss.where(StockField.PRICE > 5)
ss.sort_by(StockField.RELATIVE_STRENGTH_INDEX_14, ascending=True)

df = ss.get()
```

## Field Discovery

```python
# Search for specific fields
matches = StockField.search("dividend")
for field in matches[:10]:
    print(field.name)

# Get all technical fields
technicals = StockField.technicals()

# Get all recommendations
recommendations = StockField.recommendations()

# Get all valuations
valuations = StockField.valuations()
```

## All Fields

Use `select_all()` to get all ~3,526 fields:

```python
ss = StockScreener()
ss.set_index(IndexSymbol.SP500)
ss.select_all()
ss.set_range(0, 500)

df = ss.get()
print(f"Columns: {len(df.columns)}")
```
