---
title: Multi-TF Opportunity Ranking Scanner Validation
date: 2026-02-28
status: complete
---

# Multi-TF Opportunity Ranking Scanner Validation

## Overview

Validated the multi-timeframe opportunity ranking scanner functionality, scoring engine, and CLI outputs.

---

## Validation Summary

| Component | Status | Notes |
|-----------|--------|-------|
| ScoringEngine ranking logic | ✅ Pass | Full pipeline working |
| Multi-TF factor calculations | ✅ Pass | 3-TF weighted scoring |
| CLI opportunity scanner | ✅ Pass | All options working |
| Weighting configuration | ✅ Pass | Defaults: 0.4/0.3/0.2/0.1 |
| Unit tests | ✅ Pass | 33/33 scoring tests pass |

---

## Scoring Engine Pipeline

### Flow

```
1. calculate_factor_scores(df, "TREND", "Recommend All|")
2. calculate_factor_scores(df, "MA", "Recommend Ma|")
3. calculate_factor_scores(df, "OSC", "Recommend Other|")
4. calculate_roc_score(df)
5. calculate_ensemble_score(df)  → weights: T:0.4, M:0.3, O:0.2, R:0.1
6. calculate_confluence(df)
7. Sort by ENSEMBLE_SCORE descending
```

### Default Weights

| Factor | Weight | Description |
|--------|--------|-------------|
| trend | 0.4 | Recommend All (overall trend) |
| ma | 0.3 | Recommend MA (moving average) |
| osc | 0.2 | Recommend Other (oscillators) |
| roc | 0.1 | Rate of Change (momentum) |

### Timeframe Weights (Default)

| Timeframe | Weight |
|-----------|--------|
| 240 | 0.33 |
| 60 | 0.33 |
| 15 | 0.33 |

---

## Sample Output Analysis

### Test Run: Majors (2026-02-28)

| Pair | TREND | MA | OSC | ROC | ENSEMBLE | Direction | TF Confluence | Factor Confluence |
|------|-------|-----|-----|-----|----------|-----------|----------------|-------------------|
| EURUSD | 0.37 | 0.67 | 0.08 | 0.09 | 0.376 | long | 3L/0S | 4L/0R = 7 |
| USDJPY | 0.33 | 0.59 | 0.08 | 0.06 | 0.332 | long | 3L/0S | 4L/0R = 7 |
| AUDUSD | 0.32 | 0.63 | 0.02 | 0.06 | 0.326 | long | 3L/0S | 4L/0R = 7 |
| GBPUSD | 0.20 | 0.23 | 0.18 | -0.06 | 0.180 | long | 2L/1S | 3L/1R = 5 |
| USDCHF | -0.12 | -0.33 | 0.09 | -0.27 | -0.158 | short | 1L/2S | 1L/3R = 5 |

### Key Observations

1. **EURUSD, USDJPY, AUDUSD**: Strong alignment (TF_L:3, F_L:4, TC:7) - all TFs and factors bullish
2. **GBPUSD**: Mixed signal (TF_L:2, TF_S:1) but still positive ensemble due to weighted scoring
3. **USDCHF**: Clear short signal (ensemble negative, TF_S > TF_L)

---

## CLI Validation

### Commands Tested

| Command | Status |
|---------|--------|
| `--scanner opportunity --universe majors` | ✅ Pass |
| `--scanner opportunity --universe minors` | ✅ Pass |
| `--opportunity-trend-weight 0.6` | ✅ Pass |
| `--opportunity-timeframe-weights "240=0.6,60=0.3,15=0.1"` | ✅ Pass |
| `--min-ma-rating 0.5` | ✅ Pass |
| `--min-roc 0.1` | ✅ Pass |

---

## Confluence Calculation

### Formula

```
TF_CONFLUENCE_LONG = count(Recommend All|tf > 0)
TF_CONFLUENCE_SHORT = count(Recommend All|tf < 0)

FACTOR_BULLISH_COUNT = count(TREND_DIR="bullish", MA_DIR="bullish", OSC_DIR="bullish", ROC_DIR="bullish")
FACTOR_BEARISH_COUNT = count(TREND_DIR="bearish", ...)

TOTAL_CONFLUENCE = (TF_CONFLUENCE + FACTOR_BULLISH_COUNT) when long
                  (TF_CONFLUENCE + FACTOR_BEARISH_COUNT) when short
```

### Confluence Levels

| Level | Threshold |
|-------|-----------|
| strong | TOTAL_CONFLUENCE >= 5 |
| medium | TOTAL_CONFLUENCE >= 3 |
| weak | TOTAL_CONFLUENCE >= 1 |
| none | else |

---

## Issues Found

### None Critical

1. **GBPUSD mixed signal**: Direction shows "long" despite TF alignment being mixed (2L/1S). This is expected behavior since weighted ensemble score can be positive even with mixed TFs.

---

## Conclusion

The multi-TF opportunity ranking scanner is functioning correctly:
- Scoring pipeline properly calculates factor scores
- Timeframe weighting works
- CLI options all functional
- Unit tests all pass (33/33)

The system ranks opportunities by ENSEMBLE_SCORE (weighted combination of trend, MA, oscillator, and ROC factors across 3 timeframes), with confluence calculated separately for display.
