# Trend Following Signal Improvements Plan

## Enhancement Summary

**Deepened on:** 2026-02-27
**Sections enhanced:** 4 (Python quality, Performance, Architecture, Simplicity)
**Research agents used:** kieran-python-reviewer, performance-oracle, architecture-strategist, code-simplicity-reviewer

### Key Improvements from Research
1. **Remove magnitude weighting** - Keep simple TF count (1-3), avoid over-engineering
2. **Threshold already exists** - Just change default from 0.0 to 0.2
3. **Use Enums for direction** - Prevent "long" vs "LONG" string errors
4. **Handle missing 15m gracefully** - Fallback to 2-TF behavior

### New Considerations Discovered
- `trend_threshold` CLI argument already exists - verify in code before adding
- 4 separate DIRECTION calculations scattered across methods need unification
- DataFrame column access pattern could be optimized

---

## Overview
Improve the trend following signal detection in ForexStrategyScanner to:
1. Use 3-TF alignment (240, 60, 15) instead of just 2-TF
2. Make confluence score meaningful (reflect alignment count, not just alignment)
3. Add configurable trend threshold to filter weak signals
4. Unify DIRECTION calculation across all strategies

## Problem Statement
- Current trend following only uses 2 of 3 available timeframes
- Confluence score always = 2 (meaningless - mask already ensures alignment)
- Hardcoded threshold = 0.0 allows weak signals through
- DIRECTION calculated in 4 different places (maintenance burden)

## Proposed Solution

### Phase 1: Enhance Trend Following Detection (Priority: HIGH)
- Modify `_detect_trend_following` to use all 3 TFs
- Add 15m (LTF) to the alignment check
- Score based on count of aligned TFs (1-3)
- **Handle missing 15m column gracefully** - fallback to 2-TF behavior

### Phase 2: Improve Confluence Scoring (Priority: HIGH)
- Make confluence reflect alignment count (1-3)
- **SIMPLIFIED: No magnitude weighting** - use simple count only
- Add 3-TF alignment bonus only (not weighted sums)

### Phase 3: Add Configurable Threshold (Priority: MEDIUM)
- **CLARIFIED**: `trend_threshold` already exists in CLI/config
- Just change default from 0.0 to 0.2 in `settings.py`
- Verify CLI argument wiring is correct

### Phase 4: Unify Direction Calculation (Priority: MEDIUM)
- Create single `calculate_direction()` method
- Replace all 4 DIRECTION calculation sites
- **Use Enum for direction** to prevent string errors

## Technical Approach

### File Changes
- `tvscreener/lib/screeners/forex_strategy.py` - Core detection logic
- `tvscreener/cli.py` - Verify threshold argument wiring
- `tvscreener/config/settings.py` - Change default threshold
- `tests/unit/test_forex_strategy.py` - Update tests

### Key Methods to Modify
```python
# forex_strategy.py
def _detect_trend_following(self, df: pd.DataFrame) -> pd.DataFrame:
    """Add trend following columns to DataFrame.
    
    Returns:
        DataFrame with added columns: trend_direction, tf_alignment, confluence
    """
    # Add 15m TF check (handle missing gracefully)
    # Calculate 3-TF confluence (simple count 1-3)

def _add_confluence_and_direction(self, df: pd.DataFrame) -> pd.DataFrame:
    """Unify direction calculation."""

class Direction(Enum):
    LONG = "long"
    SHORT = "short"
    FLAT = "flat"
```

### Performance Considerations
- Use vectorized NumPy operations for confluence scoring
- Avoid row-wise `.apply()` or `.iterrows()`
- Pre-compute trend columns once per scan

## Implementation Steps

1. **Add LTF column to trend detection** (Phase 1)
   - Check for `Recommend All|15` column
   - Add to alignment mask if present
   - Fallback to 2-TF if 15m missing

2. **Enhance confluence scoring** (Phase 2)
   - Score = count of aligned TFs (1-3)
   - No magnitude weighting (YAGNI)

3. **Update threshold default** (Phase 3)
   - Change `settings.py` default from 0.0 to 0.2
   - Verify CLI wiring works

4. **Unify direction calculation** (Phase 4)
   - Extract to helper method using Enum
   - Replace inline calculations

5. **Update tests**
   - Add 3-TF test cases
   - Test threshold filtering
   - Test direction calculation

## Acceptance Criteria
- [x] Trend following uses all 3 TFs (240, 60, 15) when available
- [x] Fallback to 2-TF when 15m column missing
- [x] Confluence score reflects alignment count (1-3)
- [x] Configurable threshold filters weak signals (default 0.2)
- [x] Single source of truth for DIRECTION using Enum
- [x] All existing tests pass
- [x] New test coverage for 3-TF scenarios

## Backward Compatibility
- Default threshold 0.0 maintains existing behavior (in StrategyConfig)
- Settings default change to 0.2 is new behavior for CLI users
- min_confluence=1 works with new 1-3 scoring range
- CLI argument remains optional

## Research Insights (Detailed)

### Python Quality (kieran-python-reviewer)
- Use Enum for Direction to prevent "long" vs "LONG" errors
- Add explicit type hints with return value documentation
- Extract magic numbers to constants

### Performance (performance-oracle)
- Vectorized operations already used correctly in codebase
- Threshold filtering already exists and is vectorized
- 3-TF change is O(n) - linear overhead

### Architecture (architecture-strategist)
- Handle missing 15m column gracefully
- Separate confluence (alignment) from strength (magnitude)
- Consider deprecation path for score changes

### Simplicity (code-simplicity-reviewer)
- **REMOVE magnitude weighting** - violates YAGNI
- Threshold feature already exists - just change default
- Keep scope minimal
