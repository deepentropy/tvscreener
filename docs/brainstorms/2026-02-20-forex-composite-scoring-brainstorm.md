---
date: 2026-02-20
topic: forex-composite-scoring
---

# Forex Composite Scoring Enhancement

## What We're Building

Enhance the ForexOpportunityScreener with composite scoring system that produces separate long/short candidate universes:

1. **Individual factor scores** (each rated -1 to +1):
   - Trend Score: Based on Recommend.All (overall technical rating)
   - MA Score: Based on Recommend.MA (moving averages)
   - OSC Score: Based on Recommend.Other (oscillators like RSI, Stochastic)
   - ROC Score: Based on Rate of Change

2. **Ensemble score**: Weighted combination of all factors

3. **Separate universes**:
   - Long candidates: Positive ensemble score (bullish)
   - Short candidates: Negative ensemble score (bearish)

4. **Optional volume floor** filter

## Key Decisions

- **Score type**: Rating-based composite (-1 to +1 scale)
- **Universe**: Separate long/short lists
- **Weighting**: Configurable weights for each factor (default: 40/30/20/10%)
- **Volume filter**: Optional minimum volume threshold
- **Data source**: TradingView's Recommend fields already combine multiple indicators

## Technical Approach

### Score Calculation

```
Trend Score = Recommend.All (weighted by timeframe)
MA Score = Recommend.MA (weighted by timeframe)
OSC Score = Recommend.Other (weighted by timeframe)
ROC Score = normalized ROC value

Ensemble Score = (Trend * 0.4) + (MA * 0.3) + (OSC * 0.2) + (ROC * 0.1)
```

### Output

- `long_candidates`: DataFrame sorted by score (highest first)
- `short_candidates`: DataFrame sorted by score (lowest first)
- Individual factor scores as columns

### Configuration

```python
@dataclass
class ScoringConfig:
    trend_weight: float = 0.4
    ma_weight: float = 0.3
    osc_weight: float = 0.2
    roc_weight: float = 0.1
    min_volume: float | None = None
```

## Open Questions

- Should OSC include ROC or be independent? (Recommend.Other already includes momentum)
- Default timeframe weighting for multi-TF analysis
- Minimum score threshold for "qualifying" as long/short

## Next Steps

→ `/workflows:plan` for implementation details
