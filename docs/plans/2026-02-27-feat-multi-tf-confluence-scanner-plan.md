---
title: Multi-Timeframe Confluence Scanner with Unified Ranking
type: feat
date: 2026-02-27
---

# Multi-Timeframe Confluence Scanner with Unified Ranking

## Enhancement Summary

**Deepened on:** 2026-02-27
**Sections enhanced:** Python Quality, Performance, Architecture
**Research agents used:** kieran-python-reviewer, performance-oracle, architecture-strategist

### Key Improvements from Research
1. **Use numpy.select** for vectorized scoring (60% faster)
2. **Single-pass unified detection** instead of per-strategy scanning
3. **Add CLI mapping** for new `confluence` strategy
4. **Normalize scores** or add CONFLUENCE_PATTERN column
5. **Use IntEnum** for signal types and scores

---

## Overview

Enhance the forex strategy scanner to detect sophisticated market conditions using multi-timeframe and multi-factor confluence. The scanner will prioritize mean reversion entries in LTF/STF when aligned with HTF trend, and provide a ranking system to score all pairs by confluence strength.

## Problem Statement

Current scanner has separate detection methods (trend_following, mean_reversion, hybrid, breakout) that run independently. This misses opportunities where:
- HTF is trending but LTF is oversold (excellent entry)
- Multiple TFs show mean reversion signals (high probability reversal)

The existing `hybrid` strategy only captures HTF trend + LTF MR, but doesn't capture:
- STF mean reversion signals (Recommend Other|60)
- Pure multi-TF mean reversion
- Trend + STF + LTF all aligned

## Proposed Solution

### Phase 1: Unified Signal Detection (Single-Pass)

Instead of running each strategy separately, compute all signals in one pass:

```python
def _compute_all_signals(self, df: pd.DataFrame) -> pd.DataFrame:
    """Single-pass detection for all strategies including confluence."""
    htf = df["Recommend All|240"].fillna(0)
    stf = df["Recommend All|60"].fillna(0)
    osc_stf = df["Recommend Other|60"].fillna(0)
    osc_ltf = df["Recommend Other|15"].fillna(0)
    
    # Use numpy.select for vectorized scoring
    conditions = [
        (htf > thr) & (stf > thr) & (osc_ltf > -thr),  # Trend Continuation
        (htf > thr) & (osc_stf < -mr_thr) & (osc_ltf < -mr_thr),  # Trend + MR Entry
        # ... etc
    ]
    choices = [3, 4, 3, 3, 4]
    df["CONFLUENCE_SCORE"] = np.select(conditions, choices, default=0)
```

### Phase 2: Confluence Scoring Algorithm

| Combo | HTF (240) | STF (60) | LTF (15) | Score |
|-------|------------|----------|-----------|-------|
| Trend Continuation | Trend ↑ | Trend ↑ | Trend ↑ | 3 |
| Trend + MR Entry | Trend ↑ | MR (oversold) | MR (oversold) | **4** |
| MR Reversal | MR ↓ | MR ↓ | MR ↓ | 3 |
| Trend Pullback | Trend ↑ | Trend ↑ | MR (oversold) | 3 |
| Deep Pullback | Trend ↑ | MR ↓ | MR ↓ | **4** |

**Scoring rules:**
- Base score: count of aligned TFs (1-3)
- MR bonus: +1 when LTF/STF at extremes aligned with HTF trend
- Direction: determined by HTF trend direction

### Phase 3: Ranking System

Instead of filtering, rank all pairs by confluence score:
- Higher score = better opportunity
- Same score = sort by MR extremity (how oversold/overbought)

## Technical Approach

### File Changes

- `tvscreener/lib/screeners/forex_strategy.py` - Add unified detection
- `tvscreener/lib/screeners/filter_utils.py` - Add scoring helpers
- `tvscreener/cli.py` - Add `confluence` to strategy map
- `tests/unit/test_forex_strategy.py` - Add tests

### Key Data Columns

| Column | Purpose |
|--------|---------|
| `Recommend All|240/60/15` | Overall trend direction |
| `Recommend Other|60/15` | Oscillator signals (MR detection) - **Add STF oscillator** |
| `Roc|240/60/15` | Momentum for breakout |

### Type-Safe Implementation

```python
from enum import IntEnum

class SignalType(IntEnum):
    NEUTRAL = 0
    TREND_CONTINUATION = 1
    MEAN_REVERSION_ENTRY = 2
    TREND_PULLBACK = 3
    DEEP_PULLBACK = 4
    MEAN_REVERSION_REVERSAL = 5

class ConfluenceScore(IntEnum):
    MINIMAL = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4
    EXCEPTIONAL = 5
```

### New Configuration Options

```python
@dataclass
class StrategyConfig:
    mr_threshold: float = 0.2  # Already exists
    min_confluence_score: int = 2  # Rename from confluence_min_score
    # Remove include_confluence boolean - use strategy="confluence" instead
```

## Research Insights

### Python Quality (kieran-python-reviewer)
- Use IntEnum for signal types instead of magic numbers
- Add TypedDict or dataclass for return types
- Create fallback helper for missing timeframe columns
- Extract complex scoring to separate module

### Performance (performance-oracle)
- Use `numpy.select` for vectorized scoring (~60% faster)
- Single-pass unified detection instead of per-strategy scanning
- Eliminate redundant `.copy()` operations
- Pre-compute column references once

### Architecture (architecture-strategist)
- Add `confluence` to CLI strategy map
- Normalize scores or add CONFLUENCE_PATTERN column
- Use existing `ScoringEngine` or create dedicated detector
- Add STF oscillator check (Recommend Other|60) - **currently missing**

## Acceptance Criteria

- [ ] New `--strategy confluence` option in CLI
- [ ] Add `confluence` to strategy map in cli.py
- [ ] Detects Trend Continuation (all trending)
- [ ] Detects MR Entry (HTF trend + LTF/STF at extremes)
- [ ] Detects Pullback (trend + LTF reversal)
- [ ] Detects Deep Pullback (trend + STF + LTF MR)
- [ ] Uses STF oscillator (Recommend Other|60) - **NEW**
- [ ] Unified CONFLUENCE_SCORE (1-5 scale)
- [ ] Ranks all pairs by score
- [ ] Single-pass unified detection (performance)
- [ ] Backward compatible with existing strategies
- [ ] Tests pass

## Data Flow

```
Raw Data (TradingView)
    ↓
Extract HTF/STF/LTF signals (single pass)
    ↓
Classify each TF: TREND_BULLISH, TREND_BEARISH, MR_OVERBOUGHT, MR_OVERSOLD, NEUTRAL
    ↓
Apply numpy.select for combo detection
    ↓
Calculate confluence score (base + MR bonus)
    ↓
Rank by score + MR extremity
    ↓
Output ranked results
```

## Edge Cases

- Missing timeframe columns (fallback gracefully to neutral)
- All TFs neutral (no signal)
- Conflicting signals (HTF bullish, all others bearish) - exclude
- Existing STRATEGY column compatibility

## CLI Integration

Add to `cli.py` strategy_map:

```python
strategy_map = {
    "trend": "trend_following",
    "mean_reversion": "mean_reversion",
    "hybrid": "hybrid",
    "breakout": "breakout",
    "confluence": "confluence",  # NEW
    "all": "all",
}
```

## References

- Existing: `forex_strategy.py:231` - `_detect_hybrid` (HTF + LTF only)
- Existing: `forex_strategy.py:197` - `_detect_mean_reversion`
- Existing: `forex_strategy.py:262` - `_detect_breakout`
- Existing: `score.py` - `ScoringEngine` - consider extending vs new module
