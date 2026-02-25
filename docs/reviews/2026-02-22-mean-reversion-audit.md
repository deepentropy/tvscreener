---
title: "Mean Reversion Strategy Audit"
type: review
date: 2026-02-22
status: completed
---

# Mean Reversion Strategy Audit

## Current Implementation

### Detection Logic (`_detect_mean_reversion`)

```python
ltf_col = "Recommend Other|15"  # Fixed to 15m timeframe
osc_value = result[ltf_col].fillna(0)

# Signal conditions
long_mask = osc_value < -self.config.mr_threshold   # Oversold → Long
short_mask = osc_value > self.config.mr_threshold    # Overbought → Short

result["CONFLUENCE_SCORE"] = 1  # Fixed at 1
```

### Configuration Defaults

| Parameter | Default | Current Range |
|-----------|---------|---------------|
| `mr_threshold` | 0.2 | 0.1-0.3 tested |
| `min_confluence` | 1 | - |

## Findings

### What Works

1. **Direction logic is correct**: 
   - Oversold (< -threshold) → Long ✅
   - Overbought (> +threshold) → Short ✅

2. **Threshold scaling works**:
   - `mr_threshold=0.1`: 12 signals
   - `mr_threshold=0.2`: 5 signals  
   - `mr_threshold=0.3`: 3 signals

3. **CONFLUENCE_SCORE = 1** for all MR signals (single-factor strategy)

### Issues Identified

| Issue | Severity | Description |
|-------|----------|-------------|
| **Hardcoded timeframe** | Medium | Always uses 15m (`Recommend Other|15`), not configurable |
| **No short signals** | Medium | Current market has 0 overbought pairs (oscillator range: -0.36 to +0.18) |
| **CONFLUENCE_SCORE = 1** | Low | Single-factor, filtered out by min_confluence > 1 |
| **No ranking within strategy** | Low | No scoring to rank MR signals by strength |

### Current Oscillator Distribution (25 pairs)

| Range | Count | Pairs |
|-------|-------|-------|
| < -0.3 | 3 | GBPNZD, GBPAUD, EURNZD |
| -0.3 to -0.2 | 2 | GBPUSD, USDCAD |
| -0.2 to 0 | 13 | Most pairs |
| 0 to +0.2 | 7 | EURUSD, AUDUSD, etc. |
| > +0.2 | 0 | None |

## Ranking/Filter Pipeline

### Current Pipeline

```
1. Fetch raw data (25 pairs)
2. Apply MR threshold → 5 signals (osc < -0.2)
3. Set CONFLUENCE_SCORE = 1
4. Apply min_confluence filter (default: 1) → passes all
5. Apply direction filter (if specified)
6. Return results
```

### Missing Features

1. **No strength ranking**: MR signals not ranked by how extreme the oscillator is
2. **No within-strategy sorting**: Results sorted by overall score, not by MR strength

## Recommendations

### High Priority

1. **Add configurable LTF timeframe**:
   ```python
   ltf_col = f"Recommend Other|{self.config.ltf_timeframe}"
   ```

2. **Add MR-specific ranking**:
   ```python
   # Rank by absolute oscillator value (most extreme first)
   result = result.sort_values('LTF_MOMENTUM', key=abs, ascending=False)
   ```

### Medium Priority

3. **Add oscillator extremes ranking**:
   - Create `MR_STRENGTH` column = absolute value of oscillator
   - Sort by this for MR-specific results

4. **Consider multi-timeframe MR**:
   - Check multiple LTF timeframes for confluence
   - e.g., 15m AND 5m both oversold = higher confidence

## Test Results

| Configuration | Signals | Long | Short |
|--------------|---------|------|--------|
| threshold=0.1 | 12 | 12 | 0 |
| threshold=0.2 | 5 | 5 | 0 |
| threshold=0.3 | 3 | 3 | 0 |

Note: No short signals in current market (oscillator never exceeds +0.2).
