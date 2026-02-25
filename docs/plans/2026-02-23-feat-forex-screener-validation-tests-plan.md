---
title: Add forex screener validation tests
type: feat
date: 2026-02-23
---

# Add Forex Screener Validation Tests

## Overview

Add validation tests to confirm the screener's filtering and ranking logic works correctly. Tests will cover both unit (mocked) and integration (real API) scenarios.

## Problem Statement

The forex screener has complex filtering and ranking logic that needs verification:
- Contract type filters (spot, cfd, spreadbet, all)
- Rating threshold filters
- ROC bounds filters  
- Deduplication logic
- Ranking order by composite score

Without tests, changes to filter logic could introduce bugs silently.

## Proposed Solution

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
# tests/unit/test_forex_scoring.py
import pandas as pd
from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener, ForexScreenerConfig

# Test contract type filter
class TestContractTypeFilter:
    def test_cfd_filter_excludes_spot(self):
        config = ForexScreenerConfig(contract_type="cfd")
        screener = ForexOpportunityScreener(pairs=["EURUSD"], config=config)
        
        mock_df = pd.DataFrame({
            "Name": ["EURUSD.1.CFJ", "EURUSD.2.DUB"],
            "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA"],
            "Subtype": ["cfd", ""],
            "Recommend All|15": [0.8, 0.5],
            "Recommend All|60": [0.7, 0.4],
            "Recommend All|240": [0.6, 0.3],
            "Roc|15": [1.5, 0.8],
            "Roc|60": [1.2, 0.5],
            "Roc|240": [0.9, 0.2],
            "Average Volume (10 day Calc)": [1000000, 500000],
        })
        
        result = screener._apply_contract_type_filter(mock_df)
        assert len(result) == 1
        assert result.iloc[0]["Subtype"] == "cfd"

# Test rating filter
class TestRatingFilter:
    def test_rating_threshold_inclusion(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD"])
        
        mock_df = pd.DataFrame({
            "Name": ["EURUSD"],
            "Recommend All|15": [0.8],
            "Recommend All|60": [0.7],
            "Recommend All|240": [0.6],
            "Roc|15": [1.5],
            "Roc|60": [1.2],
            "Roc|240": [0.9],
            "Average Volume (10 day Calc)": [1000000],
        })
        
        from tvscreener.filter import RatingFilter
        rf = RatingFilter(rating_type="all", threshold=0.5)
        result = screener._apply_rating_filter(mock_df, rf)
        assert "Recommend All|15" in result.columns

# Test deduplication
class TestDeduplication:
    def test_canonical_pair_selection(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD"])
        
        mock_df = pd.DataFrame({
            "Name": ["EURUSD.1.CFJ", "EURUSD.10.DUB", "GBPUSD.1.OANDA"],
            "Symbol": ["EURUSD:ICMARKETS", "EURUSD:OANDA", "GBPUSD:OANDA"],
            "Subtype": ["cfd", "cfd", "cfd"],
            "Recommend All|15": [0.8, 0.9, 0.7],
            "Recommend All|60": [0.7, 0.8, 0.6],
            "Recommend All|240": [0.6, 0.7, 0.5],
            "Roc|15": [1.5, 1.6, 1.4],
            "Roc|60": [1.2, 1.3, 1.1],
            "Roc|240": [0.9, 1.0, 0.8],
            "Average Volume (10 day Calc)": [1000000, 2000000, 800000],
        })
        
        result = screener._merge_duplicates(mock_df)
        assert len(result) == 2
        assert "EURUSD" in result["_base_pair"].values

# Test ranking
class TestRanking:
    def test_ensemble_score_ordering(self):
        screener = ForexOpportunityScreener(pairs=["EURUSD", "GBPUSD"])
        
        mock_df = pd.DataFrame({
            "Name": ["EURUSD", "GBPUSD"],
            "Symbol": ["EURUSD:OANDA", "GBPUSD:OANDA"],
            "Subtype": ["cfd", "cfd"],
            "Recommend All|15": [0.8, 0.3],
            "Recommend All|60": [0.7, 0.2],
            "Recommend All|240": [0.6, 0.1],
            "Recommend Ma|15": [0.8, 0.3],
            "Recommend Ma|60": [0.7, 0.2],
            "Recommend Ma|240": [0.6, 0.1],
            "Recommend Other|15": [0.8, 0.3],
            "Recommend Other|60": [0.7, 0.2],
            "Recommend Other|240": [0.6, 0.1],
            "Roc|15": [1.5, 0.5],
            "Roc|60": [1.2, 0.4],
            "Roc|240": [0.9, 0.3],
            "Average Volume (10 day Calc)": [1000000, 800000],
        })
        
        result = screener._rank_opportunities(mock_df)
        assert "ENSEMBLE_SCORE" in result.columns
        assert result.iloc[0]["ENSEMBLE_SCORE"] >= result.iloc[1]["ENSEMBLE_SCORE"]
```

## Acceptance Criteria

- [ ] Unit tests for contract type filter (spot, cfd, spreadbet, all)
- [ ] Unit tests for rating threshold filter
- [ ] Unit tests for ROC bounds filter
- [ ] Unit tests for deduplication logic
- [ ] Unit tests for ranking order
- [ ] Integration tests with real API for filters
- [ ] Integration tests with real API for ranking
- [ ] All 129 existing tests still pass

## Technical Considerations

- Use pytest style with class-based grouping
- Mock DataFrame creation inline (no fixtures needed)
- Test internal methods directly (`_apply_contract_type_filter`, `_rank_opportunities`, etc.)
- Use plain assertions

## Dependencies & Risks

- **Risk:** Real API integration tests may be flaky - mark with `@pytest.mark.slow`
- **Dependency:** None - all required imports already available
