---
title: Enhanced Signal Output Format - Detailed TF & Factor Confluence
date: 2026-02-28
status: draft
---

# Enhanced Signal Output Format

## Overview

Enhance the scanner output to include detailed breakdown of:
1. **Timeframe-level scores** - Each TF (240/60/15) component breakdown
2. **Factor-level scores** - TREND, MA, OSC, ROC per TF
3. **TF Confluence** - How many TFs agree on direction per factor
4. **Factor Confluence** - How many factors agree on direction
5. **Combined Confluence Score** - Weighted ranking of TF + Factor confluence

---

## Current Output Format

### Opportunity Scanner

```
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ Pair   ┃     Price ┃ Rating ┃  ROC % ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│ AUDJPY │ 111.06500 │   0.42 │  0.12% │
└────────┴───────────┴────────┴────────┘
```

### Strategy Scanner

```
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
┃ Pair   ┃ Direction ┃ Pattern            ┃ Score ┃   MR ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
│ EURJPY │ long      │ trend_continuation │     4 │ 0.18 │
└────────┴───────────┴────────────────────┴───────┴──────┘
```

---

## Proposed Enhanced Output Format

### Option 1: Compact Table with Confluence Breakdown

```
┏━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Pair   ┃ Dir     ┃ Ensemble ┃ TF Confluence              │ Factor Confluence   ┃
┡━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ AUDJPY │ LONG    │   +0.46  │ 240:3L 60:3L 15:3L = 9/9   │ T:3L M:3L O:2L R:1L ┃
│ GBPCAD │ SHORT   │   +0.03  │ 240:3S 60:1S 15:2L = 4/9  │ T:1L M:0L O:1L R:0L ┃
└────────┴─────────┴───────────┴───────────────────────────────┴───────────────────┘
```

### Option 2: Detailed Per-Pair View

```
=== AUDJPY | Direction: LONG | Ensemble: +0.46 ===

TIMEFRAME BREAKDOWN:
┌─────────┬──────────┬──────────┬──────────┬──────────┐
│ TF      │ TREND    │ MA       │ OSC      │ ROC      │
├─────────┼──────────┼──────────┼──────────┼──────────┤
│ 240     │ +0.47 🟢│ +0.93 🟢│ +0.00    │          │
│ 60      │ +0.45 🟢│ +0.80 🟢│ +0.09    │ +0.12 🟢 │
│ 15      │ +0.47 🟢│ +0.67 🟢│ +0.27 🟢│          │
└─────────┴──────────┴──────────┴──────────┴──────────┘

CONFLUENCE ANALYSIS:
TF Confluence:  240(3L) + 60(3L) + 15(3L) = 9/9 = 100% aligned
Factor Confluence:
  - TREND: 240(+0.47) + 60(+0.45) + 15(+0.47) = +1.39 bullish → 3/3 TFs bullish
  - MA:    240(+0.93) + 60(+0.80) + 15(+0.67) = +2.40 bullish → 3/3 TFs bullish
  - OSC:   240(+0.00) + 60(+0.09) + 15(+0.27) = +0.36 bullish → 2/3 TFs bullish
  - ROC:   60(+0.12) = +0.12 bullish → 1/1 TFs bullish

Combined Score: TF Confluence (9) + Factor Confluence (9) = 18/18 = MAX
```

### Option 3: JSON Export with Full Details

```json
{
  "pair": "AUDJPY",
  "direction": "long",
  "ensemble_score": 0.458,
  "timeframes": {
    "240": {
      "trend": 0.47,
      "ma": 0.93,
      "osc": 0.00,
      "roc": null,
      "direction": "long"
    },
    "60": {
      "trend": 0.45,
      "ma": 0.80,
      "osc": 0.09,
      "roc": 0.12,
      "direction": "long"
    },
    "15": {
      "trend": 0.47,
      "ma": 0.67,
      "osc": 0.27,
      "roc": null,
      "direction": "long"
    }
  },
  "confluence": {
    "tf_confluence_score": 9,
    "tf_confluence_max": 9,
    "tf_alignment_pct": 100,
    "factor_confluence": {
      "trend": {"score": 3, "direction": "long", "alignment": "100%"},
      "ma": {"score": 3, "direction": "long", "alignment": "100%"},
      "osc": {"score": 2, "direction": "long", "alignment": "67%"},
      "roc": {"score": 1, "direction": "long", "alignment": "100%"}
    },
    "total_confluence": 18,
    "max_confluence": 18,
    "confluence_grade": "A+"
  }
}
```

---

## Confluence Scoring Formula

### Timeframe Confluence

For each factor (TREND, MA, OSC, ROC):
```
TF_Factor_Confluence = Count of TFs where factor direction matches overall direction
```

### Factor Confluence

```
Factor_Score = Sum of (TF trend scores when direction matches)
```

### Combined Confluence Score

```
Total_Confluence = TF_Confluence + Factor_Confluence

Grading:
- A+ (18-20): Perfect alignment
- A  (15-17): Strong alignment
- B  (12-14): Good alignment
- C  (8-11):  Moderate alignment
- D  (4-7):   Weak alignment
- F  (0-3):   No alignment
```

---

## Component Details

### Factor Definitions

| Factor | Source Column | Description |
|--------|---------------|-------------|
| TREND | Recommend All | Overall trend direction |
| MA | Recommend Ma | Moving average alignment |
| OSC | Recommend Other | Oscillator signal |
| ROC | Change | Rate of change momentum |

### Direction Mapping

| Value Range | Direction | Symbol |
|-------------|-----------|--------|
| > 0.1 | Bullish | 🟢 / L |
| -0.1 to 0.1 | Neutral | ⚪ / N |
| < -0.1 | Bearish | 🔴 / S |

---

## CLI Options for Enhanced Output

```bash
# Show detailed breakdown
--detailed-output
--show-tf-scores
--show-factor-scores

# Confluence ranking
--rank-by-confluence
--min-confluence-grade C

# Export formats
--output detailed.json
--output-format verbose
```

---

## Example Outputs

### Top 5 Opportunities with Confluence

```
┏━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Rank ┃ Pair    ┃ Dir     ┃ Ensemble ┃ TF Conf     ┃ Grade     ┃
┡━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│  1  │ AUDJPY  │ LONG    │  +0.46  │ 9/9 (100%) │ A+        │
│  2  │ GBPJPY  │ LONG    │  +0.39  │ 9/9 (100%) │ A+        │
│  3  │ EURJPY  │ LONG    │  +0.35  │ 9/9 (100%) │ A+        │
│  4  │ EURUSD  │ LONG    │  +0.38  │ 9/9 (100%) │ A+        │
│  5  │ USDJPY  │ LONG    │  +0.35  │ 9/9 (100%) │ A+        │
└──────┴─────────┴─────────┴─────────┴─────────────┴───────────┘
```

### Confluent Combos Analysis

```
AUDIYY - Strongest Confluence (A+)
├─ TF Alignment: 240→60→15 ALL BULLISH
├─ TREND Confluence: +0.47 +0.45 +0.47 = +1.39 (3/3 TFs)
├─ MA Confluence:    +0.93 +0.80 +0.67 = +2.40 (3/3 TFs)
├─ OSC Confluence:   +0.00 +0.09 +0.27 = +0.36 (2/3 TFs)
└─ ROC Confluence:   +0.12 = +0.12 (1/1 TFs)

GBPCAD - Mixed Signals (C)
├─ TF Alignment: 240 BEARISH | 60 NEARLY FLAT | 15 BULLISH
├─ TREND Confluence: +0.47 -0.11 -0.31 = +0.05 (1/3 TFs)
├─ MA Confluence:    +0.93 -0.40 -0.80 = -0.27 (1/3 TFs)
├─ OSC Confluence:   +0.00 +0.18 +0.27 = +0.45 (2/3 TFs)
└─ ROC Confluence:   -0.18 = -0.18 (1/1 TFs)
```

---

## Implementation Plan

### Phase 1: Data Enhancement

- [ ] Add TF breakdown columns to output DataFrame
- [ ] Calculate TF-level direction for each factor
- [ ] Compute confluence scores

### Phase 2: Output Formatting

- [ ] Add `--detailed` CLI flag
- [ ] Implement compact table format
- [ ] Implement detailed per-pair view

### Phase 3: Export Formats

- [ ] Enhance JSON export with full details
- [ ] Add CSV export with confluence columns

---

## Acceptance Criteria

- [ ] Show TREND, MA, OSC, ROC per timeframe (240/60/15)
- [ ] Calculate TF confluence (how many TFs agree)
- [ ] Calculate Factor confluence (how many factors agree)
- [ ] Combined confluence score (0-18 scale)
- [ ] Grade assignment (A+ to F)
- [ ] CLI option to enable detailed output
- [ ] All tests pass
