---
title: "Forex Scanner Audit: Multi-Timeframe and Factors Confluence"
type: review
date: 2026-02-22
status: completed
---

# Forex Scanner Audit: Multi-Timeframe and Factors Confluence

## Current Implementation Analysis

### 1. Multi-Timeframe Confluence

**What's Implemented:**
- Timeframe weights: 15m=0.5, 60=0.3, 240=0.2
- Weighted average scoring across timeframes
- Strategy detection (trend_following, breakout) checks alignment

**What's Missing:**
- `TIMEFRAME_CONFLUENCE` score - count of TFs agreeing on direction
- `HTF_ALIGNED`, `STF_ALIGNED` boolean flags
- Confluence level classification (strong/medium/weak)

### 2. Factors Confluence

**What's Implemented:**
- TREND_SCORE (Recommend.All weighted)
- MA_SCORE (Recommend.MA weighted)
- OSC_SCORE (Recommend.Other weighted)
- ROC_SCORE (rate of change)
- ENSEMBLE_SCORE (weighted sum: 40/30/20/10)

**What's Missing:**
- `FACTOR_CONFLUENCE` score - count of factors agreeing on direction
- Factor agreement flags
- Individual factor direction (bullish/bearish per factor)

### 3. Scoring Weights

| Component | Current | Recommended |
|----------|---------|-------------|
| Trend | 40% | 35% |
| MA | 30% | 25% |
| OSC | 20% | 25% |
| ROC | 10% | 15% |

## Gap Analysis

### Confluence Metrics to Add

```python
# Timeframe confluence
df["HTF_ALIGNED"] = df["Recommend All|240"].apply(lambda x: "bullish" if x > 0 else "bearish" if x < 0 else "neutral")
df["STF_ALIGNED"] = df["Recommend All|60"].apply(lambda x: "bullish" if x > 0 else "bearish" if x < 0 else "neutral")
df["LTF_ALIGNED"] = df["Recommend All|15"].apply(lambda x: "bullish" if x > 0 else "bearish" if x < 0 else "neutral")

# Count aligned TFs
df["TF_CONFLUENCE"] = sum([
    df["HTF_ALIGNED"] == direction,
    df["STF_ALIGNED"] == direction, 
    df["LTF_ALIGNED"] == direction
])

# Factor confluence
df["FACTOR_BULLISH_COUNT"] = sum([
    df["TREND_SCORE"] > 0,
    df["MA_SCORE"] > 0,
    df["OSC_SCORE"] > 0,
    df["ROC_SCORE"] > 0
])
```

### Output Columns to Add

| Column | Description |
|--------|-------------|
| `TF_CONFLUENCE` | 0-3 timeframes aligned |
| `FACTOR_CONFLUENCE` | 0-4 factors bullish |
| `HTF_DIRECTION` | bullish/bearish/neutral |
| `STF_DIRECTION` | bullish/bearish/neutral |
| `MA_DIRECTION` | bullish/bearish/neutral |
| `OSC_DIRECTION` | bullish/bearish/neutral |
| `CONFLUENCE_LEVEL` | strong (3+), medium (2), weak (1) |

## Recommendations

### High Priority
1. Add `TF_CONFLUENCE` score (timeframe alignment count)
2. Add `FACTOR_CONFLUENCE` score (factor alignment count)
3. Add direction columns for each factor

### Medium Priority
4. Add confluence level classification (strong/medium/weak)
5. Make weights configurable per factor
6. Add confidence score from alignment

### Low Priority
7. Add correlation matrix between factors
8. Add historical confluence tracking
9. Add signal quality metrics

## Files Affected

- `tvscreener/screeners/forex_opportunity.py` - Add confluence scoring
- `tvscreener/screeners/forex_strategy.py` - Enhance strategy detection

## Summary

The current implementation has solid foundation with:
- ✅ Multi-timeframe weighted scoring
- ✅ Factor decomposition (TREND, MA, OSC, ROC)
- ✅ Ensemble scoring with configurable weights
- ✅ Direction detection

Needs enhancement for:
- ❌ Timeframe confluence counting
- ❌ Factor confluence counting
- ❌ Direction per factor
- ❌ Confluence level classification
