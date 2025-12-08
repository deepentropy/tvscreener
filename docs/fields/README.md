# TvScreener Field Reference

This directory contains documentation for all available fields across different screener types.

## Screener Types

| Screener | Field Class | Total Fields | Default Fields | Documentation |
|----------|-------------|--------------|----------------|---------------|
| Stock/ETF | `StockField` | 3,526 | 424 | [stock_fields.md](stock_fields.md) |
| Crypto | `CryptoField` | 3,108 | 180 | [crypto_fields.md](crypto_fields.md) |
| Forex | `ForexField` | 2,965 | 167 | [forex_fields.md](forex_fields.md) |
| Bond | `BondField` | 201 | - | [bond_fields.md](bond_fields.md) |
| Futures | `FuturesField` | 393 | - | [futures_fields.md](futures_fields.md) |
| Coin (CEX/DEX) | `CoinField` | 3,026 | - | [coin_fields.md](coin_fields.md) |

## Field Categories

Fields are organized into the following categories:

### Price & Volume
- Price data (open, high, low, close)
- Volume metrics
- Bid/Ask spreads

### Performance
- Daily, weekly, monthly performance
- Year-to-date (YTD) performance
- All-time highs/lows

### Technical Indicators
- Moving Averages (SMA, EMA, HullMA, VWMA)
- Oscillators (RSI, MACD, Stochastic, CCI)
- Volatility (ATR, Bollinger Bands, Keltner Channels)
- Trend (ADX, Aroon, Ichimoku, Parabolic SAR)
- Pivot Points (Classic, Fibonacci, Camarilla, Woodie, DeMark)
- Candlestick Patterns

### Fundamental Data (Stocks only)
- Valuation (P/E, P/B, P/S, EV/EBITDA)
- Profitability (ROE, ROA, margins)
- Growth metrics
- Dividends
- Balance sheet items
- Cash flow metrics

### Bond-Specific
- Yield metrics
- Coupon information
- Maturity data
- Credit ratings

### Crypto-Specific
- Market cap
- 24h volume
- Available/Total coins

### DEX-Specific (CoinField)
- DEX buy/sell volumes
- Liquidity metrics
- Token holder data

## Usage

```python
from tvscreener import StockScreener, StockField

# Use default fields
screener = StockScreener()
df = screener.get()

# Use all available fields
screener.specific_fields = StockField
df = screener.get()

# Use specific fields
screener.specific_fields = [
    StockField.NAME,
    StockField.PRICE,
    StockField.MARKET_CAPITALIZATION,
    StockField.PE_RATIO_TTM,
]
df = screener.get()
```

## Field Definition Structure

Each field enum has the following attributes:
- `label`: Human-readable name
- `field_name`: API field name used in requests
- `format`: Data format type (float, percent, text, etc.)
- `interval`: Whether field supports time intervals
- `historical`: Whether field supports historical lookback
