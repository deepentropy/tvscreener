---
title: Prettify Signal Output - Detailed TF & Factor Confluence Tables
date: 2026-02-28
status: draft
---

# Prettify Signal Output - Detailed TF & Factor Confluence Tables

## Overview

Enhance the scanner output with detailed tables showing:
1. **Timeframe breakdown** - TREND, MA, OSC, ROC per TF (240/60/15)
2. **TF Confluence** - How many TFs align per factor
3. **Factor Confluence** - How many factors align
4. **Combined Confluence Grade** - A+ to F ranking

---

## Current State

### Current Output (forex_opportunity.py:318-346)

```python
table = Table(title="Forex Opportunities")
table.add_column("Pair", style="cyan")
table.add_column("Price", style="white", justify="right")
table.add_column("Rating", style="green", justify="right")
table.add_column("ROC %", style="yellow", justify="right")
```

**Columns:** Pair | Price | Rating | ROC %

---

## Proposed Enhanced Output Formats

### Format 1: Clean Summary Table

Best for quick scan - ranked by ensemble score with confluence indicators.

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                    FOREX OPPORTUNITIES - SIGNAL RANKING                    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
┃ Rank │ Pair   │ Direction │ Ensemble │ TF Conf │ Factor Conf │ Grade │
├──────┼────────┼───────────┼──────────┼─────────┼─────────────┼───────┤
│  1   │ AUDJPY │ LONG      │   +0.46  │  3/3    │    4/4      │  A+   │
│  2   │ GBPJPY │ LONG      │   +0.40  │  3/3    │    4/4      │  A+   │
│  3   │ EURUSD │ LONG      │   +0.38  │  3/3    │    4/4      │  A+   │
│  4   │ EURJPY │ LONG      │   +0.35  │  3/3    │    3/4      │  A    │
│  5   │ USDJPY │ LONG      │   +0.33  │  3/3    │    4/4      │  A+   │
├──────┼────────┼───────────┼──────────┼─────────┼─────────────┼───────┤
│ 18   │ EURCHF │ SHORT     │   -0.13  │  1/3    │    1/4      │  D    │
│ 19   │ USDCHF │ SHORT     │   -0.16  │  1/3    │    1/4      │  D    │
│ 20   │ EURNZD │ SHORT     │   -0.22  │  0/3    │    0/4      │  F    │
│ 21   │ USDCAD │ SHORT     │   -0.23  │  0/3    │    0/4      │  F    │
└──────┴────────┴───────────┴──────────┴─────────┴─────────────┴───────┘
```

### Format 2: Detailed Per-Pair Breakdown

Best for analysis - shows each TF and factor with direction indicators.

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                     AUDJPY - DETAILED SIGNAL BREAKDOWN                     ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║ Direction: LONG  │  Ensemble: +0.458  │  Total Confluence: 7/10  Grade: A+ ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                        TIMEFRAME ANALYSIS                                 ║
╠─────────────┬──────────────┬──────────────┬──────────────┬──────────────┤
║ Timeframe   │ TREND        │ MA           │ OSC          │ ROC          ║
╠─────────────┼──────────────┼──────────────┼──────────────┼──────────────┤
║ 240 (HTF)  │ +0.47 🟢     │ +0.93 🟢     │ +0.00 ⚪      │     -       ║
║ 60 (MTF)   │ +0.45 🟢     │ +0.80 🟢     │ +0.09 🟢     │ +0.12 🟢    ║
║ 15 (LTF)   │ +0.47 🟢     │ +0.67 🟢     │ +0.27 🟢     │     -       ║
╠═════════════╪═══════════════╪═══════════════╪═══════════════╪════════════╣
║ AGGREGATE   │ +0.46 🟢     │ +0.76 🟢     │ +0.16 🟢     │ +0.12 🟢    ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                        CONFLUENCE BREAKDOWN                               ║
╠───────────────────────────────────────────────────────────────────────────╣
║ TF Confluence:   3L/0S (100%) - All TFs aligned BULLISH               ║
║ Factor Confluence: T:3/3 🟢  M:3/3 🟢  O:2/3 🟢  R:1/1 🟢           ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

### Format 3: Compact Matrix View

Best for comparing multiple pairs - matrix of TF × Factor.

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃              CONFLUENCE MATRIX - ALL PAIRS (Top 10)                  ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━┇━━━━━━━━━━━┇━━━━━━━━━━━┇━━━━━━━━━━━┇━━━━━━━━━┩
┃ Pair        ┃ TREND    ┃ MA       ┃ OSC       ┃ ROC       ┃ Grade   ┃
┃             ┃ 240│60│15 ┃ 240│60│15 ┃ 240│60│15 ┃ 60│15  ┃         ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
┃ AUDJPY      ┃ L │L │L  ┃ L │L │L  ┃ N │L │L  ┃ L │    ┃ A+      ┃
┃ GBPJPY      ┃ L │L │L  ┃ L │L │L  ┃ L │L │L  ┃ L │    ┃ A+      ┃
┃ EURUSD      ┃ L │L │L  ┃ L │L │L  ┃ L │N │L  ┃ L │    ┃ A+      ┃
┃ EURJPY      ┃ L │L │L  ┃ L │L │L  ┃ L │S │S  ┃ L │    ┃ A       ┃
┃ USDJPY      ┃ L │L │L  ┃ L │L │L  ┃ S │L │L  ┃ L │    ┃ A+      ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━┩
┃ GBPCAD      ┃ S │S │L  ┃ S │S │L  ┃ L │L │L  ┃ S │    ┃ C       ┃
┃ EURCHF      ┃ S │S │L  ┃ S │S │L  ┃ S │N │S  ┃ S │    ┃ D       ┃
┃ USDCAD      ┃ S │S │S  ┃ S │S │N  ┃ L │N │S  ┃     │    ┃ F       ┃
└─────────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
Legend: L=Bullish 🟢  N=Neutral ⚪  S=Bearish 🔴
```

---

## Implementation Plan

### Phase 1: Add Confluence Data Columns

1. Calculate TF-level direction (bullish/neutral/bearish) for each factor
2. Add columns: `TF_TREND_DIR`, `TF_MA_DIR`, `TF_OSC_DIR`, `TF_ROC_DIR`
3. Calculate: `TF_CONFLUENCE_SCORE`, `FACTOR_CONFLUENCE_SCORE`, `CONFLUENCE_GRADE`

### Phase 2: Create New Print Methods

1. Add `print_detailed_summary()` method
2. Add `print_matrix_summary()` method
3. Support `--detailed` and `--matrix` CLI flags

### Phase 3: Rich Table Styling

1. Add color coding (🟢🟡🔴)
2. Add alignment indicators
3. Add grade badges

---

## CLI Options

```bash
# Current
uv run python -m tvscreener.cli --scanner opportunity --universe majors

# New options
--detailed              # Show detailed per-pair breakdown
--matrix                # Show confluence matrix view
--show-tf-scores        # Show TF-level scores
--show-factor-scores    # Show factor breakdown
--confluence-grade A   # Filter by grade (A+, A, B, C, D, F)
--min-confluence 5      # Filter by confluence score
```

---

## Acceptance Criteria

- [x] Clean summary table with Grade column
- [x] Detailed per-pair breakdown with TF × Factor matrix
- [x] Color-coded direction indicators
- [x] `--detailed` CLI flag
- [x] `--matrix` CLI flag
- [x] Grade filtering support
- [x] All existing tests pass
