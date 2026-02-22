---
date: 2026-02-22
topic: asset-agnostic-screener-pipeline
---

# Asset-Agnostic Screener Pipeline

## What We're Building

A generalized screener framework that supports multiple asset types (forex, stocks/ETFs, commodities, crypto) with the same core code. Each asset type will have its own configuration (pairs, timeframes, indicator fields) but share the same filtering, scoring, and strategy detection logic.

The goal is to make it easy to add new asset types by creating configuration rather than writing new code.

## Why This Approach

We explored three approaches:

1. **Separate screeners per asset** - Simple but code duplication
2. **Single unified screener with conditionals** - Gets messy with if/else
3. **Configuration-driven with shared engine** - Most extensible, cleanest long-term

We chose approach #3 because:
- New asset types = new config, not new code
- Shared logic means shared bugs fixes
- Clear separation of concerns: config vs engine

## Key Decisions

- **AssetUniverse config pattern**: Each asset type defines its pairs, timeframes, default weights, and field mappings in a dataclass. The engine reads this config.

- **Indicator field abstraction**: Instead of hardcoding `"Recommend All|{tf}"`, use `universe.fields["recommend_all"].format(tf=...)` to handle asset-specific field patterns.

- **Strategy detection is generic**: Same trend_following, mean_reversion, breakout, hybrid logic works across assets. Each asset provides its own indicators (RSI for stocks, ROC for forex, etc.) via config.

- **Full parity with forex**: All existing forex features (scoring weights, confluence metrics, CLI output) must work identically for new assets.

## Asset Config Structure

```python
@dataclass
class AssetUniverse:
    name: str                           # "forex", "stocks", "commodity", "crypto"
    pairs: list[str]                    # or market identifier
    timeframes: list[str]               # ["15", "60", "240", "D"]
    default_tf_weights: dict[str, float]
    fields: IndicatorFields             # field name patterns
    exchanges: list[str] | None         # preferred exchanges


@dataclass  
class IndicatorFields:
    recommend_all: str      # "Recommend All|{tf}"
    recommend_ma: str       # "Recommend MA|{tf}" 
    recommend_osc: str      # "Recommend Other|{tf}"
    momentum: str           # "Roc|{tf}" or "RSI|{tf}"
```

## Supported Assets (Initial)

| Asset | Pairs | Unique Indicators |
|-------|-------|-------------------|
| Forex | 27 majors/minors | ROC |
| Stocks/ETFs | Dynamic | RSI, VWMA |
| Commodities | Dynamic | STOCH |
| Crypto | Dynamic | MACD |

## Open Questions

- Should we support mixed portfolios (e.g., forex + stocks in one scan)?
- How do we handle different field availability per asset in the API?

## Next Steps

→ `/workflows:plan` for implementation details
