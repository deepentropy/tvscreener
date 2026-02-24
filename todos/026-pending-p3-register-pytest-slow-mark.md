---
status: complete
priority: p3
issue_id: "026"
tags: [tests, tooling]
dependencies: []
---

## Problem Statement

Functional tests use `@pytest.mark.slow` but the mark is not registered, producing warnings.

## Findings

- `tests/functional/test_forex_screener.py:7` uses `@pytest.mark.slow` (also at lines 14, 23, 31).
- No `pytest.ini` / `pyproject.toml` pytest config was added to define the `slow` marker.

## Proposed Solutions

### Option A: Register marker in pytest config (Recommended)

- Add `pytest.ini` (or `[tool.pytest.ini_options]` in `pyproject.toml`) with `markers = ["slow: ..."]`.

## Recommended Action

Option A.

## Acceptance Criteria

- [ ] `uv run pytest` emits no unknown-mark warnings
