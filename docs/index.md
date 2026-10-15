# tvscreener

**Python library to retrieve data from TradingView Screener**

[![PyPI version](https://badge.fury.io/py/tvscreener.svg)](https://badge.fury.io/py/tvscreener)
[![Downloads](https://pepy.tech/badge/tvscreener)](https://pepy.tech/project/tvscreener)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Features

- **11 Screener Types**: Stock, ETF, Crypto, Forex, Bond, Government Bond, Futures, Coin, Option, Index, and Economics
- **Pythonic Filtering**: Use `>`, `<`, `>=`, `<=`, `==`, `!=` operators directly on fields, and combine them with `|` (OR) and `&`
- **Presets and Calendars**: TradingView's market movers, and earnings, dividend, IPO and economic calendars
- **Financial Statements**: up to 20 years of annual and 8 years of quarterly statements, dividends, earnings and seasonals
- **News, Filings and Transcripts**: filtered news, 10-Q/10-K lists, earnings call transcripts
- **3,500+ Fields**: Access all TradingView fields including fundamentals, technicals, and more
- **Index Filtering**: Filter by S&P 500, NASDAQ 100, Dow Jones, and 50+ other indices
- **Multi-Timeframe**: Use any technical indicator with different timeframes
- **Real-time Streaming**: Stream screener refreshes, or real-time quotes pushed by TradingView
- **Styled Output**: Beautiful formatted tables matching TradingView's style

## Quick Example

```python
from tvscreener import StockScreener, StockField, IndexSymbol

ss = StockScreener()

# Filter S&P 500 stocks
ss.set_index(IndexSymbol.SP500)

# Pythonic filtering
ss.where(StockField.PRICE > 50)
ss.where(StockField.PE_RATIO_TTM.between(10, 25))
ss.where(StockField.RELATIVE_STRENGTH_INDEX_14 < 40)

# Select fields
ss.select(
    StockField.NAME,
    StockField.PRICE,
    StockField.CHANGE_PERCENT,
    StockField.PE_RATIO_TTM,
    StockField.RELATIVE_STRENGTH_INDEX_14
)

# Sort and limit
ss.sort_by(StockField.MARKET_CAPITALIZATION, ascending=False)
ss.set_range(0, 100)

df = ss.get()
```

## Try the Code Generator

Build screener queries visually with our web app:

[:material-rocket-launch: Launch Code Generator](https://deepentropy.github.io/tvscreener/){ .md-button .md-button--primary }

## Installation

```bash
pip install tvscreener
```

## Documentation

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get up and running in 5 minutes

    [:octicons-arrow-right-24: Getting Started](getting-started/quickstart.md)

-   :material-filter:{ .lg .middle } __Filtering Guide__

    ---

    Complete reference for filtering stocks

    [:octicons-arrow-right-24: Filtering](guide/filtering.md)

-   :material-chart-line:{ .lg .middle } __Stock Screening__

    ---

    Value, dividend, momentum strategies

    [:octicons-arrow-right-24: Examples](examples/stock-screening.md)

-   :material-chart-timeline:{ .lg .middle } __Technical Analysis__

    ---

    RSI, MACD, multi-timeframe screens

    [:octicons-arrow-right-24: Technical](examples/technical-analysis.md)

</div>

## Why tvscreener?

| Feature | tvscreener | Others |
|---------|------------|--------|
| **Type-safe fields** | `StockField.PRICE` | `"close"` strings |
| **Pythonic syntax** | `field > 100` | SQL-like builders |
| **Index filtering** | `set_index(SP500)` | Manual symbol lists |
| **Field discovery** | `search("rsi")` | Read docs |
| **All fields** | `select_all()` | List each one |
| **Streaming** | Built-in | DIY |

## License

MIT License - See [LICENSE](https://github.com/deepentropy/tvscreener/blob/main/LICENSE) for details.

---

**Not affiliated with TradingView.** This library accesses publicly available data from the TradingView website.
