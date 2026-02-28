---
title: Forex Scanner Execution Plan
date: 2026-02-28
status: active
---

# Forex Scanner Execution Plan

## Quick Reference Commands

### Daily Scan Commands

```bash
# Opportunity scanner - ranked opportunities
uv run python -m tvscreener.cli --scanner opportunity --universe all

# Strategy scanner - all strategies
uv run python -m tvscreener.cli --scanner strategy --strategy all --universe all

# Confluence scanner - with MR detection
uv run python -m tvscreener.cli --scanner strategy --strategy confluence --universe all --mr-threshold 0.15

# With risk filters
uv run python -m tvscreener.cli --scanner strategy --strategy all \
  --min-confluence 3 \
  --min-tf-alignment 2 \
  --require-momentum \
  --min-rvol 1.2
```

### Filter Commands

| Filter | CLI Option | Example |
|--------|-----------|---------|
| Min confluence | `--min-confluence 3` | Score 3+ signals |
| Min TF alignment | `--min-tf-alignment 2` | 2+ aligned TFs |
| Require momentum | `--require-momentum` | ROC matches direction |
| Min RVOL | `--min-rvol 1.2` | Volume > 1.2x average |
| Volume spike | `--require-volume-spike` | Volume > 1.5x average |

### Risk Management

| Parameter | CLI Option | Default |
|-----------|-----------|---------|
| Risk per trade | `--risk-per-trade 1.0` | 1% |
| ATR multiplier | `--atr-multiplier 2.0` | 2.0 |
| Min R:R | `--min-risk-reward 1.5` | 1.5:1 |
| Account balance | `--account-balance 10000` | 10,000 |

---

## Validation Checklist

- [ ] Run opportunity scanner
- [ ] Run strategy scanner (all strategies)
- [ ] Run with risk filters
- [ ] Verify output format
- [ ] Check signal counts
- [ ] Validate ranking order

---

## Expected Outputs

### Opportunity Scanner

| Column | Description |
|--------|-------------|
| Pair | Currency pair |
| Price | Current price |
| Rating | ENSEMBLE_SCORE (0-1) |
| ROC % | Rate of change |

### Strategy Scanner

| Column | Description |
|--------|-------------|
| Pair | Currency pair |
| Direction | long/short |
| Pattern | Strategy type |
| Score | Confluence score |
| MR | Mean reversion strength |

---

## Notes

- Tests: 222 passing ✅
- All new CLI args working
- Risk utils module functional
