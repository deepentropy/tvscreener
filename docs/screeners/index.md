# Index Screener

Screen stock indices, index and commodity CFDs, and crypto market-cap indices. About 650 symbols.

## Quick Start

```python
from tvscreener import IndexScreener, IndexField

df = IndexScreener().main_indices().get()          # main stock indices (DAX, AEX, SSE Composite...)
df = IndexScreener().cfds().get()                  # index and commodity CFDs (TVC, OANDA...)
df = IndexScreener().crypto_market_caps().get()    # CRYPTOCAP:TOTAL, BTC, ETH...
```

## Fields

`IndexField` has about 350 fields: price, change, performance and technical indicators (RSI, moving averages, MACD...). Indicators accept `with_interval()` like other screeners.

```python
ss = IndexScreener().main_indices()
ss.select(IndexField.NAME, IndexField.CLOSE, IndexField.CHANGE)
ss.where(IndexField.CHANGE < -1)
df = ss.get()
```
