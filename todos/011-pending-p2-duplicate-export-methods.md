---
status: pending
priority: p2
issue_id: "011"
tags: [architecture, dry, forex-strategy]
dependencies: []
---

## Problem Statement

`forex_strategy.py` and `forex_opportunity.py` have nearly identical `to_csv()`, `to_json()`, and `print_summary()` methods. This violates DRY and creates maintenance burden.

## Findings

- **Location:** 
  - `forex_strategy.py:273-316` - to_csv, to_json, print_summary
  - `forex_opportunity.py:268-315` - identical methods
- **Evidence:** Both classes have:
```python
def to_csv(self, path: str, include_index: bool = False) -> None:
    df = self.scan()  # or get_opportunities()
    df.to_csv(path, index=include_index)
    logger.info(f"Saved {len(df)} signals/opportunities to {path}")
```

## Proposed Solutions

### Option A: Extract to Mixin (Recommended)
```python
class ExportMixin:
    def to_csv(self, path: str, include_index: bool = False) -> None:
        df = self._get_dataframe()
        df.to_csv(path, index=include_index)
        logger.info(f"Saved {len(df)} results to {path}")
    
    def _get_dataframe(self) -> pd.DataFrame:
        raise NotImplementedError
```
- **Pros:** Reusable, clear contract
- **Cons:** Requires _get_dataframe abstraction
- **Effort:** Medium
- **Risk:** Low

### Option B: Standalone Functions
```python
def export_to_csv(df: pd.DataFrame, path: str, label: str) -> None:
    df.to_csv(path)
    logger.info(f"Saved {len(df)} {label} to {path}")
```
- **Pros:** Simple, no inheritance
- **Cons:** Less encapsulated
- **Effort:** Low
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] DRY violation eliminated
- [ ] No duplicate code in to_csv/to_json/print_summary
- [ ] All tests pass

## Work Log

### 2026-02-22 - Initial Review

**By:** pattern-recognition-specialist agent

**Actions:**
- Identified duplicate methods across two files

**Learnings:**
- Both classes evolved separately with similar export needs
