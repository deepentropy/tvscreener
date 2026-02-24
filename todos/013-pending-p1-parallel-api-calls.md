---
status: complete
priority: p1
issue_id: "013"
tags: [performance, api-calls]
dependencies: []
---

## Problem Statement

Forex pairs are fetched sequentially in a loop, causing 30+ sequential HTTP requests. With ~500ms per request, total latency is ~15 seconds.

## Findings

- **Location:** `tvscreener/lib/screeners/forex_opportunity.py:81-84`
- **Evidence:**
```python
for pair in self.pairs:
    pair_data = self._fetch_pair_data(pair)
```

## Proposed Solutions

### Option A: ThreadPoolExecutor (Recommended)
```python
from concurrent.futures import ThreadPoolExecutor

def get_opportunities(self) -> pd.DataFrame:
    with ThreadPoolExecutor(max_workers=5) as executor:
        all_data = list(executor.map(self._fetch_pair_data, self.pairs))
    all_data = [df for df in all_data if not df.empty]
```
- **Pros:** 5x faster, simple
- **Cons:** May hit API rate limits
- **Effort:** Medium
- **Risk:** Low

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] Parallel fetching implemented
- [ ] Latency reduced from ~15s to ~3s for 30 pairs

## Work Log

### 2026-02-23 - Code Review

**By:** Review agents

**Actions:**
- Identified sequential API calls as P1 performance issue

**Learnings:**
- ThreadPoolExecutor is safe for I/O-bound operations
