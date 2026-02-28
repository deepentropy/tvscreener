---
title: Forex Scanner Execution & Validation Plan
date: 2026-02-28
status: active
---

# Forex Scanner Execution & Validation Plan

## Overview

This document outlines the execution commands and validation procedures for the forex opportunity and strategy scanners.

---

## Scanner Types

### 1. Opportunity Scanner
- Ranks all pairs by weighted ensemble score
- Uses multi-TF factor analysis (TREND, MA, OSC, ROC)
- Outputs ranked list sorted by opportunity strength

### 2. Strategy Scanner
- Detects specific trading patterns
- Supports: trend_following, mean_reversion, hybrid, breakout, confluence
- Uses 3-TF alignment (240/60/15)

---

## Execution Commands

### Daily Scan - Opportunity Ranking

```bash
# All pairs
uv run python -m tvscreener.cli --scanner opportunity --universe all

# Majors only
uv run python -m tvscreener.cli --scanner opportunity --universe majors

# Minors only
uv run python -m tvscreener.cli --scanner opportunity --universe minors
```

### Strategy Scans

```bash
# Trend Following
uv run python -m tvscreener.cli --scanner strategy --strategy trend --universe all

# Mean Reversion
uv run python -m tvscreener.cli --scanner strategy --strategy mean_reversion --universe all

# Confluence (default threshold 0.2)
uv run python -m tvscreener.cli --scanner strategy --strategy confluence --universe all

# Confluence (lower threshold for more signals)
uv run python -m tvscreener.cli --scanner strategy --strategy confluence --universe all --mr-threshold 0.15

# All strategies combined
uv run python -m tvscreener.cli --scanner strategy --strategy all --universe all
```

### Custom Weights

```bash
# Custom factor weights
uv run python -m tvscreener.cli --scanner opportunity \
  --opportunity-trend-weight 0.6 \
  --opportunity-ma-weight 0.2 \
  --opportunity-osc-weight 0.1 \
  --opportunity-roc-weight 0.1

# Custom timeframe weights
uv run python -m tvscreener.cli --scanner opportunity \
  --opportunity-timeframe-weights "240=0.6,60=0.3,15=0.1"
```

### Filters

```bash
# Filter by rating
uv run python -m tvscreener.cli --scanner opportunity --min-ma-rating 0.5

# Filter by ROC
uv run python -m tvscreener.cli --scanner opportunity --min-roc 0.1

# Long only
uv run python -m tvscreener.cli --scanner strategy --filter long

# Short only
uv run python -m tvscreener.cli --scanner strategy --filter short
```

---

## Validation Procedures

### Pre-Run Checklist

- [ ] Tests pass: `uv run pytest --tb=no -q`
- [ ] Lint clean: `uv run ruff check tvscreener/`
- [ ] Network connectivity to TradingView API

### Post-Run Validation

1. **Check output format**
   - Table displays correctly
   - All expected columns shown
   - Sorting is correct

2. **Verify scoring**
   - Top pairs have highest ensemble scores
   - Direction matches TF alignment
   - Confluence counts are accurate

3. **Review signals**
   - Strategy patterns detected correctly
   - Confluence scores match expected values
   - MR extremity values are reasonable

---

## Expected Outputs

### Opportunity Scanner Output

```
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ Pair   ┃     Price ┃ Rating ┃  ROC % ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│ AUDJPY │ 111.06750 │   0.46 │  0.12% │
│ EURJPY │ 184.43700 │   0.35 │  0.15% │
...
```

### Strategy Scanner Output

```
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┓
┃ Pair   ┃ Direction ┃ Pattern            ┃ Score ┃   MR ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━┩
│ EURJPY │ long      │ trend_continuation │     4 │ 0.18 │
│ GBPCAD │ short     │ trend_mr_entry     │     4 │ 0.27 │
...
```

---

## Troubleshooting

### No Results
- Check API connectivity
- Verify pairs are valid
- Try smaller universe (majors first)

### Unexpected Rankings
- Verify timeframe weights
- Check factor weight configuration
- Review market conditions

### Pattern Detection Issues
- Adjust thresholds (--mr-threshold, --trend-threshold)
- Check that required columns are present
- Validate signal logic in code

---

## Schedule

| Frequency | Command | Purpose |
|-----------|---------|---------|
| Daily | `--universe all` | Full market scan |
| As needed | `--universe majors` | Quick scan |
| Weekly | `--strategy all` | All strategies |
| On alert | `--filter long/short` | Direction-specific |

---

## Related Documents

- `docs/validation/2026-02-28-opportunity-scanner-validation.md`
- `docs/validation/2026-02-28-cross-minors-analysis.md`
- `docs/plans/2026-02-27-feat-multi-tf-confluence-scanner-plan.md`
