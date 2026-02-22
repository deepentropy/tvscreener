---
title: "Forex Screener Run & Pipeline Audit"
type: review
date: 2026-02-22
status: completed
---

# Forex Screener Run & Pipeline Audit

## Execution Summary

Ran the ForexOpportunityScreener and ForexStrategyScanner against:
- **Majors**: 7 pairs (EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD)
- **Minors**: 18 pairs (EURGBP, EURJPY, GBPJPY, etc.)
- **Total**: 25 pairs (2 minors not found: EURNOK, EURSEK)
- **Timeframes**: 15m, 1H, 4H

---

## Opportunity Screener Results

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total pairs scanned | 25 |
| Opportunities found | 25 |
| Long signals | 13 (52%) |
| Short signals | 12 (48%) |
| Strong confluence | 16 (64%) |
| Medium confluence | 9 (36%) |

### Top 5 Opportunities

| Rank | Pair | Ensemble Score | Direction | Confluence |
|------|------|----------------|-----------|------------|
| 1 | AUDJPY | 0.512 | long | strong |
| 2 | AUDUSD | 0.489 | long | strong |
| 3 | EURCHF | 0.461 | long | strong |
| 4 | AUDCAD | 0.418 | long | strong |
| 5 | EURGBP | 0.339 | long | strong |

### Output Columns Generated (37 total)

**Score Columns:**
- TREND_SCORE, MA_SCORE, OSC_SCORE, ROC_SCORE
- ENSEMBLE_SCORE, RATING_SCORE

**Direction Columns:**
- TF_15_DIR, TF_60_DIR, TF_240_DIR
- TREND_DIR, MA_DIR, OSC_DIR, ROC_DIR

**Confluence Columns:**
- TF_CONFLUENCE_LONG, TF_CONFLUENCE_SHORT
- FACTOR_BULLISH_COUNT, CONFLUENCE_LEVEL

---

## Strategy Scanner Results

### Summary Statistics
| Metric | Value |
|--------|-------|
| Total signals | 30 |
| Trend following | 18 (60%) |
| Breakout | 12 (40%) |
| Mean reversion | 0 (0%) |
| Hybrid | 0 (0%) |
| Long | 13 (43%) |
| Short | 17 (57%) |

### Strategy Details

**Trend Following (18 signals)**
- Requires: HTF (4H) + STF (1H) alignment
- Top: AUDJPY, AUDUSD, EURNZD

**Breakout (12 signals)**
- Requires: Multi-TF ROC alignment
- Top: GBPCAD, EURNZD, GBPAUD

**Mean Reversion (0 signals)**
- LTF oscillator extremes not detected
- Possible: threshold too high or market not in MR condition

**Hybrid (0 signals)**
- HTF trend + LTF MR not aligned

---

## Pipeline Audit

### Current Pipeline Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                        PIPELINE FLOW                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  1. FETCH                                                          │
│     └─ ForexScreener.search(pair) → select fields → get()         │
│        Per-pair API call (25 calls)                                  │
│                                                                      │
│  2. DEDUPLICATE                                                    │
│     └─ _merge_duplicates() - keeps canonical pairs                │
│        Priority: canonical > exchange > volume                      │
│                                                                      │
│  3. FILTER                                                          │
│     ├─ Contract type filter (cfd/spot/spreadbet)                    │
│     ├─ Volume filter (optional)                                      │
│     ├─ Rating filters (all/ma/oscillator + threshold)              │
│     └─ ROC filter (min/max)                                         │
│                                                                      │
│  4. SCORE                                                           │
│     ├─ Factor scores: TREND, MA, OSC, ROC                          │
│     │   └─ Weighted average across timeframes (15m=0.5, 60=0.3, 240=0.2)│
│     ├─ Ensemble score (40% trend, 30% MA, 20% OSC, 10% ROC)      │
│     └─ Direction: long if > 0, else short                          │
│                                                                      │
│  5. CONFLUENCE                                                      │
│     ├─ TF direction per timeframe (bullish/bearish/neutral)        │
│     ├─ TF confluence (count of aligned TFs)                        │
│     ├─ Factor direction                                            │
│     └─ CONFLUENCE_LEVEL (strong/medium/weak/none)                 │
│                                                                      │
│  6. OUTPUT                                                          │
│     └─ Sort by ENSEMBLE_SCORE descending                           │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Findings

### What Works Well

1. **Multi-timeframe scoring** - Weighted average across 15m/60m/240m with proper weights
2. **Confluence detection** - TF alignment and factor bullish count implemented
3. **Strategy detection** - Trend following and breakout properly detected
4. **Direction classification** - Long/short correctly assigned
5. **Deduplication** - Canonical pairs prioritized correctly

### Issues Identified

| Issue | Severity | Description |
|-------|----------|-------------|
| No mean reversion signals | Medium | Zero MR signals detected - threshold may be too high |
| No hybrid signals | Medium | Zero hybrid signals - HTF+LTF combo not working |
| Per-pair API calls | Performance | 25 sequential API calls - could batch |
| Hardcoded thresholds | Low | Strategy thresholds in code, not configurable |
| EURNOK/EURSEK missing | Low | 2 pairs not found in API |

### Filter Configuration

| Filter | Current Value | Notes |
|--------|---------------|-------|
| Contract type | cfd | Most common |
| Timeframe weights | 15m=0.5, 60=0.3, 240=0.2 | LTF weighted more |
| Scoring weights | TREND=40%, MA=30%, OSC=20%, ROC=10% | HTF weighted more |
| Min confluence | 2 | Default in StrategyConfig |

---

## Recommendations

### High Priority
1. **Investigate mean reversion** - Why zero MR signals? Check threshold
2. **Investigate hybrid** - Why zero hybrid signals? Check logic
3. **Add configurable thresholds** - Move hardcoded values to config

### Medium Priority
4. **Batch API calls** - Consider async or batch fetching
5. **Add signal strength** - Beyond just confluence, add magnitude
6. **Historical tracking** - Store results for trend analysis

### Low Priority
7. **Add more strategies** - Momentum, volatility-based
8. **Backtesting** - Validate signals against historical price action
9. **Notifications** - Alert on new signals

---

## Files Reviewed

- `tvscreener/screeners/forex_opportunity.py` - Opportunity screener
- `tvscreener/screeners/forex_strategy.py` - Strategy scanner
- `tvscreener/score.py` - Scoring engine
- `tvscreener/filter.py` - Filter classes
- `tvscreener/constants/forex.py` - Forex constants

---

## Conclusion

The screener is functional and producing reasonable signals:
- 25/25 pairs screened successfully
- 13 long, 12 short with good confluence distribution
- 30 strategy signals detected (18 trend, 12 breakout)

**Key concern**: Zero mean reversion and hybrid signals suggest either:
- Market conditions not favoring these strategies, OR
- Thresholds too strict, OR
- Logic issue in detection

Recommend investigation of MR and hybrid thresholds before relying on those strategy signals.
