---
title: "Confluence Score Audit - Multi-Timeframe Factors"
type: review
date: 2026-02-22
status: completed
---

# Confluence Score Audit - Multi-Timeframe Factors

## Overview

The system calculates **two types of confluence**:

1. **Timeframe Confluence (TF_CONFLUENCE)**: How many timeframes agree on direction
2. **Factor Confluence (FACTOR_BULLISH_COUNT)**: How many scoring factors agree

---

## 1. Timeframe Confluence

### Calculation

```python
# For each timeframe (15, 60, 240):
TF_X_DIR = "bullish" if Recommend All|X > 0 else "bearish" if < 0 else "neutral"

# Count aligned timeframes:
TF_CONFLUENCE_LONG = count of TFs with value > 0
TF_CONFLUENCE_SHORT = count of TFs with value < 0
```

### Distribution (25 pairs)

| TF_CONFLUENCE_LONG | Count | CONFLUENCE_LEVEL |
|-------------------|-------|------------------|
| 0 | 9 | strong (short) |
| 1 | 3 | medium |
| 2 | 6 | medium |
| 3 | 7 | strong |

### Issue: TF weights not used in confluence

**Current**: Simple count (0-3)
**Not using**: TF weights (15=0.5, 60=0.3, 240=0.2)

**Result**: All TFs treated equally in confluence count, but weighted in score calculation.

---

## 2. Factor Confluence

### Calculation

```python
# For each factor (TREND, MA, OSC, ROC):
FACTOR_DIR = "bullish" if FACTOR_SCORE > 0 else "bearish" if < 0 else "neutral"

# Count bullish factors:
FACTOR_BULLISH_COUNT = count of factors with DIR == "bullish"
```

### Distribution (25 pairs)

| FACTOR_BULLISH_COUNT | Count |
|---------------------|-------|
| 0 | 12 |
| 2 | 1 |
| 3 | 5 |
| 4 | 7 |

### Issue: No FACTOR_BEARISH_COUNT

**Current**: Only bullish count
**Missing**: Symmetric bearish count for short signals

### Issue: No FACTOR_BEARISH_COUNT = 1

**Gap**: Distribution jumps from 0 → 2, skipping 1
**Cause**: Factors tend to align together (correlation)

---

## 3. CONFLUENCE_LEVEL Classification

### Current Logic

```python
if DIRECTION == "long":
    if TF_CONFLUENCE_LONG >= 3: "strong"
    elif TF_CONFLUENCE_LONG == 2: "medium"
    elif TF_CONFLUENCE_LONG == 1: "weak"
    else: "none"
else:  # short
    if TF_CONFLUENCE_SHORT >= 3: "strong"
    elif TF_CONFLUENCE_SHORT == 2: "medium"
    elif TF_CONFLUENCE_SHORT == 1: "weak"
    else: "none"
```

### Distribution

| Level | Count | Percentage |
|-------|-------|------------|
| strong | 16 | 64% |
| medium | 9 | 36% |
| weak | 0 | 0% |
| none | 0 | 0% |

### Issue: No "weak" or "none" signals

**Cause**: All signals have at least 1-2 TFs aligned
**Problem**: Classification not discriminating enough

---

## 4. Strategy CONFLUENCE_SCORE

Each strategy has its own CONFLUENCE_SCORE:

| Strategy | CONFLUENCE_SCORE | Meaning |
|----------|-----------------|---------|
| Trend Following | 2 | HTF + STF aligned |
| Mean Reversion | 1 | Single factor (LTF) |
| Hybrid | 2 | HTF trend + LTF MR |
| Breakout | 3 | All TFs aligned on ROC |

### Issue: Different scales for different strategies

**Problem**: Mean Reversion always scores 1, Breakout always scores 3
**Result**: `min_confluence > 1` filters out ALL mean reversion signals

---

## 5. Scoring Pipeline

### Current Flow

```
1. Calculate factor scores (TREND, MA, OSC, ROC)
   - Each = weighted average across timeframes
   - TF weights: 15=0.5, 60=0.3, 240=0.2

2. Calculate ensemble score
   - ENSEMBLE = TREND*0.4 + MA*0.3 + OSC*0.2 + ROC*0.1

3. Calculate direction
   - DIRECTION = "long" if ENSEMBLE > 0 else "short"

4. Calculate TF confluence
   - TF_CONFLUENCE_LONG/SHORT = count of aligned TFs
   - TF_X_DIR for each TF

5. Calculate factor confluence
   - FACTOR_BULLISH_COUNT = count of bullish factors

6. Assign CONFLUENCE_LEVEL
   - Based only on TF_CONFLUENCE (not FACTOR)
```

### Issue: Factor confluence not used in CONFLUENCE_LEVEL

**Current**: Only TF_CONFLUENCE determines level
**Missing**: FACTOR_BULLISH_COUNT could strengthen/weaken level

---

## 6. Issues Summary

| Issue | Severity | Description |
|-------|----------|-------------|
| TF weights unused in confluence | Medium | Confluence uses count, not weighted |
| No FACTOR_BEARISH_COUNT | Medium | Asymmetric for short signals |
| No "weak" or "none" levels | Low | All signals classified as medium/strong |
| Strategy CONFLUENCE_SCORE varies | Medium | Mean reversion always = 1 |
| Factor confluence ignored | Medium | FACTOR_BULLISH_COUNT not used in level |

---

## 7. Recommendations

### High Priority

1. **Add FACTOR_BEARISH_COUNT** for symmetry:
   ```python
   FACTOR_BEARISH_COUNT = count of factors with DIR == "bearish"
   ```

2. **Include factor confluence in CONFLUENCE_LEVEL**:
   ```python
   # Combine TF + Factor confluence
   TOTAL_CONFLUENCE = TF_CONFLUENCE + FACTOR_CONFLUENCE
   
   if TOTAL_CONFLUENCE >= 5: "strong"
   elif TOTAL_CONFLUENCE >= 3: "medium"
   else: "weak"
   ```

### Medium Priority

3. **Use weighted TF confluence**:
   ```python
   WEIGHTED_TF_CONFLUENCE = sum(TF_value * TF_weight for each TF)
   ```

4. **Normalize strategy CONFLUENCE_SCORE**:
   - Scale all strategies to 0-3 range
   - Or make strategy-specific thresholds

### Low Priority

5. **Add more granular levels**:
   - "very_strong" (5+ confluence)
   - "strong" (4)
   - "medium" (2-3)
   - "weak" (1)
   - "none" (0)

---

## 8. Current Weights Reference

### Timeframe Weights

| TF | Weight | Rationale |
|----|--------|-----------|
| 15m | 0.5 | Most recent, highest reactivity |
| 60m | 0.3 | Medium-term trend |
| 240m (4H) | 0.2 | Higher-timeframe context |

### Factor Weights

| Factor | Weight | Rationale |
|--------|--------|-----------|
| TREND | 0.4 | Primary trend direction |
| MA | 0.3 | Moving average alignment |
| OSC | 0.2 | Oscillator extremes |
| ROC | 0.1 | Momentum |
