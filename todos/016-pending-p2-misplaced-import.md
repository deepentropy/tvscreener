---
status: complete
priority: p2
issue_id: "016"
tags: [code-quality, import]
dependencies: []
---

## Problem Statement

Import statement placed in middle of file after module-level constant declaration. Violates Python import conventions and is confusing.

## Findings

- **Location:** `tvscreener/cli.py:24`
```python
UNIVERSE_MAP: dict[str, AssetUniverse] = {}

from tvscreener.config.universe import FOREX_UNIVERSE  # <-- HERE

UNIVERSE_MAP["forex"] = FOREX_UNIVERSE
```

## Proposed Solutions

### Option A: Move to Top of File
```python
from tvscreener.config.universe import FOREX_UNIVERSE

UNIVERSE_MAP: dict[str, AssetUniverse] = {}
UNIVERSE_MAP["forex"] = FOREX_UNIVERSE
```
- **Effort:** Trivial
- **Risk:** None

## Recommended Action

<!-- To be filled during triage -->

## Acceptance Criteria

- [ ] All imports at top of file

## Work Log

### 2026-02-23 - Code Review
