---
date: 2026-02-26
topic: forex-scanner-unification
status: planned
---

# Forex Scanner Unification Plan

## Enhancement Summary

**Deepened on:** 2026-02-26  
**Sections enhanced:** 5  
**Research agents used:** code-simplicity-reviewer, architecture-strategist

### Key Improvements
1. **Simplified approach**: Eliminated abstract base class (YAGNI - composition already works)
2. **ExportMixin with abstract properties**: Recommended pattern with type safety
3. **Kept configs separate**: Confirmed by both reviewers - different domains
4. **Quick wins prioritized**: Single export method vs mixin first

---

## What We're Building

Unify the ForexOpportunityScreener and ForexStrategyScanner by:
1. Creating shared ExportMixin for exports (quick win)
2. Eliminating duplicate code (35-45 LOC)
3. Maintaining separation but ensuring consistent interfaces

## Current Architecture Analysis

### Component Comparison

| Component | ForexOpportunityScreener | ForexStrategyScanner |
|-----------|--------------------------|----------------------|
| **Config** | ForexScreenerConfig (9 fields) | StrategyConfig (12 fields) |
| **Data Fetch** | Own implementation (lines 129-161) | Delegates to OpportunityScreener (line 76) |
| **Filtering** | Rating, ROC, Volume filters (lines 166-297) | Strategy filters + filter_utils (lines 300-321) |
| **Ranking/Scoring** | ScoringEngine.rank_opportunities | Strategy detection (lines 162-283) |
| **Exports** | to_csv, to_json, to_parquet, to_xml (lines 312-404) | Identical methods (lines 318-407) |

### Code Duplication Stats

- **Export methods**: ~45 lines duplicated (~95% identical)
- **Config overlap**: Only `contract_type`, `include_atr`, `include_rsi` (2 fields out of 21)
- **Relationship**: Composition (StrategyScanner *has-a* OpportunityScreener)

---

## Research Insights

### Code Simplicity Review

**Finding: Plan Creates Solutions for Non-Problems**

The code-simplicity-reviewer concluded:

> "The ~45 lines of export duplication is not worth adding two new classes and an abstract base class hierarchy."

**Key Recommendations:**
1. **Don't create ExportMixin** - Just add a single export method that delegates to helpers
2. **Don't create abstract base class** - Composition already works correctly
3. **Don't unify configs** - Only 2 overlapping fields, not worth abstraction

**Proposed Simplification:**
```python
# Single unified export method instead of 4 duplicates:
def export(self, path: str, format: str, **kwargs) -> None:
    export_func = getattr(module, f"export_to_{format}")
    export_func(self._get_data(), path, logger=logger, label=self.label, **kwargs)
```

### Architecture Review

**Finding: Mixin Pattern Recommended (with Abstract Properties)**

The architecture-strategist recommends proceeding with:

> "Proceed with ExportMixin - The plan correctly identifies real duplication"

**Recommended Pattern:**
```python
from abc import ABC, abstractproperty

class ExportMixin(ABC):
    """Mixin providing standardized export functionality."""
    
    @abstractproperty
    def _data_getter(self) -> Callable[[], pd.DataFrame]:
        """Subclass must provide callable that returns DataFrame."""
        pass
    
    @abstractproperty
    def _export_label(self) -> str:
        """Subclass must provide label for logging."""
        pass
    
    def to_csv(self, path: str, include_index: bool = False, *,
                metadata: dict[str, Any] | None = None) -> None:
        export_to_csv(
            self._data_getter,
            path,
            include_index,
            logger=self._logger,
            label=self._export_label,
            metadata=metadata,
        )
```

**Benefits:**
- Enforces contract via ABC
- Eliminates duplicate method bodies
- Maintains LSP compliance

---

## Implementation Plan

### Phase 1: Quick Win - Unified Export Method (Recommended First)

**Approach:** Instead of creating a mixin, add single export method to each class that delegates to helpers.

**Steps:**
1. Add `label` property to ForexOpportunityScreener → returns "opportunities"
2. Add `label` property to ForexStrategyScanner → returns "signals"
3. Create single `export(path, format, **kwargs)` method in both classes
4. Remove duplicate to_csv, to_json, to_parquet, to_xml methods
5. Update CLI call sites

**Files affected:**
- `tvscreener/lib/screeners/forex_opportunity.py`
- `tvscreener/lib/screeners/forex_strategy.py`
- `tvscreener/cli.py` (if needed)

**LOC reduction:** ~35-45 lines

### Phase 2: Optional - Extract ExportMixin (If More Scanners Emerge)

**When to do:** Only if new scanner types need export functionality.

**Steps:**
1. Create `tvscreener/lib/screeners/mixins.py`
2. Define ExportMixin with abstract properties
3. Refactor both scanners to use mixin
4. Add tests

### Phase 3: Don't Do - Abstract Base Class

**Decision:** Skip - composition already works correctly.

**Rationale:**
- Classes serve different purposes (filtering vs strategy detection)
- StrategyScanner already composes OpportunityScreener
- Abstract base class would force unwanted coupling

### Phase 4: Don't Do - Config Unification

**Decision:** Skip - only 2 overlapping fields.

**Rationale:**
- `contract_type`, `include_atr`, `include_rsi` are already handled via composition
- Config objects represent different domains
- Adding base class adds indirection without benefit

---

## Implementation Details

### File: tvscreener/lib/screeners/forex_opportunity.py

**Add after line 311 (_get_data method):**

```python
@property
def label(self) -> str:
    """Label for export methods and logging."""
    return "opportunities"

def export(self, path: str, format: str, **kwargs) -> None:
    """Unified export method."""
    from tvscreener.lib.screeners import export_helpers
    export_func = getattr(export_helpers, f"export_to_{format}")
    export_func(self._get_data, path, logger=logger, label=self.label, **kwargs)
```

**Remove lines 312-404** (old export methods)

### File: tvscreener/lib/screeners/forex_strategy.py

**Add after line 313 (_get_results method):**

```python
@property
def label(self) -> str:
    """Label for export methods and logging."""
    return "signals"

def export(self, path: str, format: str, **kwargs) -> None:
    """Unified export method."""
    from tvscreener.lib.screeners import export_helpers
    export_func = getattr(export_helpers, f"export_to_{format}")
    export_func(self._get_results, path, logger=logger, label=self.label, **kwargs)
```

**Remove lines 318-407** (old export methods)

---

## Edge Cases

1. **Invalid format string**: Raise ValueError with valid formats list
2. **Empty DataFrame**: export_helpers already handles this
3. **Metadata not provided**: Pass None, export_helpers handles gracefully
4. **File write permission errors**: Let exception propagate with helpful message

---

## Acceptance Criteria

- [ ] Both scanners have single `export()` method
- [ ] CLI still works with --output flag for both scanners
- [ ] Tests pass (existing + new for export)
- [ ] LOC reduced by ~35-45 lines
- [ ] No regression in functionality
- [ ] Ruff linting passes
- [ ] Type checking passes

---

## Testing Strategy

1. **Unit tests**: Test export method with mock DataFrame
2. **Integration tests**: Run both scanners with --output to CSV/JSON/Parquet
3. **Edge cases**: Empty DataFrame, invalid format

---

## Dependencies

- Phase 1 has no dependencies - can start immediately
- Phase 2 depends on Phase 1 completion

---

## Timeline Estimate

- Phase 1: 30-45 minutes
- Phase 2 (if needed): 1-2 hours
- Testing: 30 minutes

---

## References

- [Real Python: Mixin Classes](https://realpython.com/python-mixin/)
- [Python Mixins Best Practices](https://leocon.dev/blog/2025/06/understanding-python-mixins)
- [StackOverflow: Dataclass Mixins](https://stackoverflow.com/questions/79296865)

---

## Open Questions Resolved

| Question | Resolution |
|----------|------------|
| Should StrategyScanner inherit from OpportunityScreener? | No - composition is correct |
| Create abstract base class? | No - YAGNI violation |
| Unify configs? | No - different domains |

---

## Next Steps

1. Start Phase 1 implementation
2. Run tests after each change
3. Verify CLI still works end-to-end

## Implementation Tasks

- [x] Replace duplicate export helpers in `ForexOpportunityScreener` with overridable `export()`
- [x] Replace duplicate export helpers in `ForexStrategyScanner` with overridable `export()`
- [x] Update CLI output handling to call the new `export()` method with format-specific args
- [x] Add an export resolver helper (`get_export_function`) so formats stay centralized
