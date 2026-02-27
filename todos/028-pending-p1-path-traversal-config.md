---
status: pending
priority: p1
issue_id: "028"
tags: [security, path-traversal, cli]
dependencies: []
---

# Fix Path Traversal in Config Save/Load

## Problem Statement

The `--save-config` and `--load-config` CLI arguments accept file paths without validation, allowing path traversal attacks via `../../../../etc/passwd`.

## Findings

- **Location:** `tvscreener/cli.py:167-173` (_maybe_save_opportunity_config) and `cli.py:219-230` (_maybe_load_opportunity_config)
- **Issue:** No path validation before file operations
- **Code:** Uses user-supplied paths directly in `open()` calls
- **Impact:** Arbitrary file read/write on the filesystem

## Proposed Solutions

### Option 1: Validate Path is Within Allowed Directory

**Approach:** Resolve both the target path and allowed directory, then verify the resolved path starts with allowed directory.

**Pros:**
- Prevents all path traversal variants
- Works with symlinks

**Cons:**
- More code to maintain

**Effort:** 30 minutes

**Risk:** Low

---

### Option 2: Use os.path.basename Only

**Extract just the filename and ignore directories:

**Approach:** Use only the basename of the path provided.

**Pros:**
- Simple fix

**Cons:**
- Breaks legitimate nested paths

**Effort:** 10 minutes

**Risk:** Low

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `tvscreener/cli.py:167-173`
- `tvscreener/cli.py:219-230`

## Acceptance Criteria

- [ ] Path traversal attempts are rejected
- [ ] Legitimate config paths work
- [ ] Security tests added

## Work Log

### 2026-02-25 - Security Review Discovery

**By:** Claude Code (Security Sentinel)

**Actions:**
- Identified path traversal vulnerability in config save/load
- Found both save and load are vulnerable

**Learnings:**
- Same issue exists in output file handling (lines 256-269, 335-348)
