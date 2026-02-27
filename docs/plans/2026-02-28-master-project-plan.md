---
title: Forex Scanner - Master Project Plan
type: master-plan
date: 2026-02-28
status: active
---

# Forex Scanner - Master Project Plan

## Project Overview

Build a comprehensive Forex Opportunity + Strategy screener CLI with multi-timeframe analysis, confluence detection, and signal ranking.

## Current Status

- **Tests:** 205 passing ✅
- **Lint:** Clean ✅  
- **Feature:** Multi-TF confluence scanner implemented ✅

---

## Learnings & Validation Results

### What Works Well

1. **Confluence Detection Logic** - Mathematically verified: 0 pattern/direction/score mismatches
2. **Threshold Tuning** - `mr_threshold=0.15` reveals more "pullback entry" candidates vs 0.2
3. **3-TF Alignment** - 240/60/15 trend alignment works correctly
4. **CLI Integration** - `--strategy confluence` works properly

### Key Validations

| Test | Result |
|------|--------|
| Trend continuation detection | ✅ Pass |
| MR Entry detection (HTF trend + LTF/STF extremes) | ✅ Pass |
| Confluence scoring (1-5 scale) | ✅ Pass |
| ROC bonus | ✅ Pass |
| CLI --mr-threshold override | ✅ Pass |

### Market Observations (2026-02-28 Validation)

**With default mr_threshold=0.2:**
- Majors: 3 signals (USDCHF short trend_pullback, AUDUSD/EURUSD long trend_continuation)
- Minors: 4 signals (EURJPY long score 4, GBPJPY/AUDJPY long, EURCHF short)

**With mr_threshold=0.15:**
- Majors: 3 signals (same as above)
- Minors: 6 signals (GBPCAD/EURGBP with trend_mr_entry score 4)

**Validation Confirmed:**
- GBPCAD short: trend_mr_entry, score 4 (HTF bearish + STF/LTF overbought) ✅
- EURGBP long: trend_mr_entry, score 4 (HTF bullish + STF/LTF oversold) ✅
- EURJPY long: trend_continuation, score 4 (best clean trend) ✅

---

## Pending Tasks (10 items)

### P1 - Security & Critical (4)

| ID | Task | Effort | Risk |
|----|------|--------|------|
| 027 | Fix XML Injection in export_helpers.py | 10 min | Low |
| 028 | Fix Path Traversal in config save/load | 30 min | Low |
| 029 | Fix DataFrame copies in filter pipeline | 2-3 hrs | Medium |
| 030 | Add MCP Agent parity for CLI features | 4-6 hrs | Low |

### P2 - Code Quality (4)

| ID | Task | Effort | Risk |
|----|------|--------|------|
| 031 | Consolidate duplicated export methods | 2-3 hrs | Low |
| 032 | Remove duplicate timeframe weight parsing | 30 min | Low |
| 033 | Add type hints to CLI helper functions | 15 min | None |
| 036 | Remove dead `_add_confluence_and_direction` method | 5 min | Low |

### P3 - Low Priority (2)

| ID | Task | Effort | Risk |
|----|------|--------|------|
| 034 | Remove unused `_apply_filters` method | 1 min | None |
| 037 | Optimize confluence detection (optional) | N/A | Skip |

---

## Recommended Execution Order

### Phase 1: Quick Wins (Start here)
1. **033** - Add type hints (15 min) - trivial
2. **034** - Remove dead `_apply_filters` (1 min) - trivial  
3. **036** - Remove dead `_add_confluence_and_direction` (5 min) - from recent code review

### Phase 2: Security Fixes (Important)
4. **027** - Fix XML injection (10 min)
5. **028** - Fix path traversal (30 min)

### Phase 3: Code Quality
6. **031** - Consolidate export methods (2-3 hrs)
7. **032** - Remove duplicate timeframe parsing (30 min)

### Phase 4: Performance & MCP (Later)
8. **029** - Fix DataFrame copies (2-3 hrs) - only if needed at scale
9. **030** - MCP parity (4-6 hrs) - future feature

---

## Dependencies

- **027** (XML injection): No dependencies
- **028** (Path traversal): No dependencies
- **029** (DataFrame copies): Requires understanding filter pipeline
- **030** (MCP parity): Requires CLI understanding
- **031** (Export): Requires both forex_opportunity.py and forex_strategy.py
- **032** (Timeframe): Requires settings.py and cli.py
- **033** (Type hints): No dependencies
- **034** (Dead code): No dependencies
- **036** (Dead method): No dependencies
- **037** (Perf): Skip - not needed at current scale

---

## Next Steps

1. Execute Phase 1 quick wins
2. Run scanners to validate
3. Commit changes
4. Continue to Phase 2
