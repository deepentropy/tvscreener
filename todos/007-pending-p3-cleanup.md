---
status: pending
priority: p3
issue_id: "007"
tags: [code-review, cleanup]
dependencies: []
---

## Problem Statement

Dead commented code in filter.py and unused ExtraFilter.__init__ method.

## Findings

1. filter.py:160-161 - Commented-out name() method
2. filter.py:45-46 - ExtraFilter.__init__ sets field_name but nothing uses it

## Proposed Solutions

### Option A: Clean up (Recommended)
- Remove commented code
- Remove or simplify ExtraFilter.__init__
- **Pros**: Cleaner code
- **Cons**: None
- **Effort**: Small
- **Risk**: Low

## Recommended Action
[To be filled during triage]

## Acceptance Criteria
- [ ] Remove dead commented code in filter.py

## Work Log
- 2026-02-22: Identified during code review
