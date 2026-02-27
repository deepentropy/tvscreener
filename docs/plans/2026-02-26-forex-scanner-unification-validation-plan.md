---
title: "Forex Scanner Unification & Validation"
type: refactor
date: 2026-02-26
---

# Forex Scanner Unification & Validation Plan

## Overview

Complete the forex scanner unification and add comprehensive validation tests to ensure both opportunity and strategy scanners work correctly with the new export architecture.

## Background

The forex scanner unification was partially completed:
- ✅ Added `get_export_function` helper to export_helpers.py
- ✅ Replaced duplicate export methods with unified `export()` method in ForexOpportunityScreener and ForexStrategyScanner
- ✅ Updated CLI to use new export flow

Remaining work:
- Continue optional architectural improvements (base class - YAGNI risk)
- Add validation tests for scanners

## Problem Statement

1. Export duplication removed, but need to validate both scanners still work correctly
2. No comprehensive tests for opportunity/strategy scanner filtering and ranking
3. Need to verify CLI integration works end-to-end

## Proposed Solution

### Phase 1: Validate Scanner Functionality

Create comprehensive tests to verify:

1. **Opportunity Scanner Tests** (`tests/unit/test_forex_opportunity.py`)
   - Filter application (volume, rating, ROC)
   - Scoring engine integration
   - Export method with new `export()` API

2. **Strategy Scanner Tests** (`tests/unit/test_forex_strategy.py`)
   - Strategy detection (trend, mean_reversion, breakout, hybrid)
   - Confluence scoring
   - Direction filtering
   - Export method with new `export()` API

3. **CLI Integration Tests** (`tests/unit/test_cli_scanners.py`)
   - Opportunity scan with output
   - Strategy scan with output
   - Metadata inclusion in exports

### Phase 2: Optional Architectural Improvements

Only if needed based on validation results:

- Abstract base class consideration (Approach B from brainstorm)
- CLI factory for scanner instantiation

## Research Insights

### Existing Test Patterns (from codebase analysis)

**From `tests/unit/test_forex_scoring.py` and `tests/unit/test_opportunity_helpers.py`:**

1. **Class-based test organization** - Group related tests in classes (`class TestScoringConfig`, `class TestEnsembleScoring`)
2. **Mock DataFrames** - Create test DataFrames with required columns matching TradingView screener format
3. **Direct scanner instantiation** - Test by creating scanner instances with config
4. **Internal method testing** - Call private methods like `_rank_opportunities()` directly
5. **tmp_path fixture** - Use pytest's tmp_path for file-based tests

### Mock DataFrame Requirements

**Opportunity Scanner columns:**
```python
pd.DataFrame({
    "Name": ["EURUSD"],
    "Symbol": ["EURUSD:OANDA"],
    "Recommend All|15": [0.8],
    "Recommend Ma|15": [0.6],
    "Recommend Other|15": [0.4],
    "Roc|15": [1.5],
})
```

**Strategy Scanner columns:**
```python
pd.DataFrame({
    "Name": ["EURUSD"],
    "Recommend All|240": [0.8],
    "Recommend All|60": [0.6],
    "Recommend Other|15": [-0.5],
    "Roc|240": [1.5],
    "Roc|60": [1.2],
    "Roc|15": [0.8],
})
```

### Edge Cases to Add

| Edge Case | Expected Behavior |
|-----------|-------------------|
| Empty DataFrame | Return empty DataFrame, no error |
| Negative volume filter | Filter out all rows |
| Null ratings | Treat as neutral (0) |
| Invalid export format | Raise ValueError with message |
| Missing required columns | Return empty or partial results |

### Test Fixtures to Consider

Add to `tests/conftest.py`:
- `sample_opportunity_df` - Mock DataFrame for opportunity scanner
- `sample_strategy_df` - Mock DataFrame for strategy scanner  
- `mock_config` - Reusable config objects

## Implementation Tasks

### Phase 1: Validation Tests

- [ ] Create `tests/unit/test_forex_opportunity.py`
  - [ ] Test volume filter (apply_volume_filter method)
  - [ ] Test rating filter (apply_rating_filter method)
  - [ ] Test ROC filter (apply_roc_filter method)
  - [ ] Test scoring engine integration (_rank_opportunities)
  - [ ] Test export() method with mock DataFrame
  - [ ] Test edge cases (empty DF, null values, negative filters)

- [ ] Create `tests/unit/test_forex_strategy.py`
  - [ ] Test trend_following detection
  - [ ] Test mean_reversion detection
  - [ ] Test breakout detection
  - [ ] Test hybrid detection
  - [ ] Test confluence scoring calculation
  - [ ] Test direction filter (long/short)
  - [ ] Test export() method with mock DataFrame
  - [ ] Test edge cases (no signals, invalid config)

- [ ] Create or update `tests/unit/test_cli_scanners.py`
  - [ ] Test opportunity CLI with CSV output
  - [ ] Test opportunity CLI with JSON output
  - [ ] Test opportunity CLI with Parquet output
  - [ ] Test opportunity CLI with XML output
  - [ ] Test strategy CLI with CSV output
  - [ ] Test strategy CLI with JSON output
  - [ ] Test strategy CLI with Parquet output
  - [ ] Test strategy CLI with XML output
  - [ ] Test metadata is included in CSV exports
  - [ ] Test metadata is included in JSON exports
  - [ ] Test invalid output format handling

### Phase 2: Optional Improvements (Conditional)

- [ ] Evaluate need for abstract base class
- [ ] Implement if validation reveals significant duplication

## Acceptance Criteria

- [ ] All new tests pass
- [ ] Existing tests still pass (161 tests)
- [ ] Export functionality verified for all formats (CSV, JSON, Parquet, XML)
- [ ] Metadata correctly included in exports
- [ ] Both opportunity and strategy scanners produce correct results
- [ ] Edge cases handled (empty DF, null values, invalid inputs)
- [ ] Test coverage for opportunity scanner filters > 80%
- [ ] Test coverage for strategy detection > 80%

### Test Coverage Targets

| Component | Current | Target |
|-----------|---------|--------|
| forex_opportunity.py | ~50% | 80% |
| forex_strategy.py | ~40% | 80% |
| export_helpers.py | ~60% | 80% |
| cli.py (scanner parts) | ~30% | 60% |

## Technical Details

### Files to Create/Modify

- `tests/unit/test_forex_opportunity.py` - New file
- `tests/unit/test_forex_strategy.py` - New file
- `tests/unit/test_cli_scanners.py` - New file (or augment existing)

### Test Patterns to Follow

**Organization:**
- Group tests in classes (e.g., `class TestVolumeFilter`, `class TestExportFunctionality`)
- Use descriptive test names: `test_filter_removes_below_threshold`

**Mock Data:**
- Create DataFrames with required TradingView columns
- Use meaningful test values (e.g., ratings from -2 to +2)

**See existing tests:**
- `tests/unit/test_opportunity_helpers.py` - CLI helpers, export metadata
- `tests/unit/test_cli_filters.py` - CLI filter testing patterns
- `tests/unit/test_forex_scoring.py` - Scanner internal methods
- `tests/functional/test_forex_screener.py` - Integration patterns

## Dependencies

- pytest (already in project)
- pandas (for DataFrame assertions)

## Timeline Estimate

- Phase 1: 2-3 hours
- Phase 2: 1-2 hours (if needed)

## References

- Brainstorm: `docs/brainstorms/2026-02-26-forex-scanner-unification-brainstorm.md`
- Related PR: Export unification completed
- Existing tests: `tests/unit/test_forex_scoring.py`, `tests/functional/test_forex_screener.py`
- CLI entry points: `tvscreener/cli.py:run_opportunity_scan`, `tvscreener/cli.py:run_strategy_scan`
- Export helpers: `tvscreener/lib/screeners/export_helpers.py:get_export_function`

## CLI Testing Approach

Use subprocess to test CLI:

```python
import subprocess

def test_cli_opportunity_csv_output(tmp_path):
    output = tmp_path / "output.csv"
    result = subprocess.run(
        ["uv", "run", "tvscreener-scan", 
         "--scanner", "opportunity",
         "--universe", "majors",
         "--output", str(output)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert output.exists()
    # Check CSV content
```
