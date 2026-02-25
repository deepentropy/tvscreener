---
title: Forex Screener Validation Tests
date: 2026-02-23
status: brainstorm
tags: [testing, forex, validation, filters]
---

# Forex Screener Validation Tests

## What We're Building

Add validation tests to confirm the screener's filtering and ranking logic works correctly. Tests will cover both unit (mocked) and integration (real API) scenarios.

## Why This Approach

Based on repo research, existing tests in `test_forex_scoring.py` use direct DataFrame mocking to test scoring logic. We'll extend this pattern to cover:
- Filter correctness (contract type, rating thresholds, ROC bounds)
- Ranking order verification
- Both unit tests (fast, isolated) and integration tests (real API)

## Key Decisions

### Test Coverage

| Category | Tests |
|----------|-------|
| **Contract Type Filter** | spot, cfd, spreadbet, all |
| **Rating Filter** | min/max threshold inclusion |
| **ROC Filter** | min/max ROC bounds |
| **Deduplication** | canonical pair selection |
| **Ranking** | score ordering and direction |

### Test Structure

```
tests/unit/test_forex_scoring.py (extend)
├── TestContractTypeFilter
├── TestRatingFilter  
├── TestRocFilter
├── TestDeduplication
└── TestRanking

tests/functional/test_forex_screener.py (new)
├── TestIntegrationFilters
└── TestIntegrationRanking
```

### Mock Data Pattern

```python
# Unit test pattern
mock_df = pd.DataFrame({
    "Name": ["EURUSD.1.CFJ", "EURUSD.10.DUB"],
    "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
    "Subtype": ["cfd", "cfd"],
    "Recommend All|15": [0.8, 0.5],
    "Recommend All|60": [0.7, 0.4],
    "Recommend All|240": [0.6, 0.3],
    "Roc|15": [1.5, 0.8],
    "Roc|60": [1.2, 0.5],
    "Roc|240": [0.9, 0.2],
    "Average Volume (10 day Calc)": [1000000, 500000],
})
```

## Open Questions

1. **Should we add pytest fixtures?** - Currently no conftest.py; keep simple for now
2. **Integration test frequency?** - Consider @pytest.mark.slow for real API tests

## Next Steps

1. Create unit tests for each filter method
2. Create integration tests with real API
3. Verify all 129 existing tests still pass
