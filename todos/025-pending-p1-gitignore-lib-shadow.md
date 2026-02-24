---
status: complete
priority: p1
issue_id: "025"
tags: [repo-hygiene, bug]
dependencies: []
---

## Problem Statement

Repo-level `.gitignore` ignores `lib/`, which can cause `tvscreener/lib/...` to be untracked and create a "works locally" shadow-code path.

## Findings

- `.gitignore:19-20` includes `lib/` and `lib64/`.
- Active code is currently under `tvscreener/lib/screeners/...` (e.g., `tvscreener/lib/screeners/forex_opportunity.py`).

## Proposed Solutions

### Option A: Unignore project `tvscreener/lib/` (Recommended)

- Add `!/tvscreener/lib/` (and optionally `!/tvscreener/lib/**`) to `.gitignore`.

### Option B: Move code out of `tvscreener/lib/`

- Rename to a non-ignored path and update imports.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] `git status` shows changes under `tvscreener/lib/` as tracked
- [ ] CI/other machines see the same code paths
