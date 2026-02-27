---
status: pending
priority: p1
issue_id: "030"
tags: [mcp, agent, cli-parity]
dependencies: []
---

# Add MCP Agent Tools for Opportunity/Strategy Scanners

## Problem Statement

PR #48 adds substantial new CLI functionality (filters, scoring weights, config management, export formats), but NONE of these features are exposed via MCP agent tools. Agents cannot access the opportunity scanner, strategy scanner, or any new CLI arguments. This is a complete action parity failure.

## Findings

- **Location:** `mcp/tools.py` (entire file)
- **Issue:** MCP server only exposes generic stock/crypto/forex screeners - zero parity with CLI's opportunity and strategy modes
- **Missing capabilities (18 total):**
  - Opportunity scanner tool
  - Strategy scanner tool
  - --save-config / --load-config tools
  - Export tools (CSV, JSON, Parquet, XML)
  - All filter arguments (--min-volume, --max-atr, --min-ma-rating)
  - All scoring weight arguments

## Proposed Solutions

### Option 1: Add Dedicated MCP Tools for Each Scanner

**Approach:** Create new MCP tools: `scan_opportunities`, `scan_strategies`, `save_config`, `load_config`, `export_results`.

**Pros:**
- Full feature parity
- Clear agent interface

**Cons:**
- More code to maintain
- May have overlapping functionality

**Effort:** 4-6 hours

**Risk:** Low

---

### Option 2: Extend Existing Tools with Mode Parameter

**Approach:** Add `mode` parameter to existing tools to switch between generic and opportunity/strategy modes.

**Pros:**
- Less code duplication

**Cons:**
- More complex tool signatures
- Harder to document

**Effort:** 3-4 hours

**Risk:** Medium

---

## Recommended Action

[To be filled during triage]

## Technical Details

**Affected files:**
- `mcp/tools.py` - needs new tools
- `mcp/server.py` - needs registration
- `tvscreener/cli.py` - functions already exist, need wrapping

## Acceptance Criteria

- [ ] Opportunity scanner accessible via MCP
- [ ] Strategy scanner accessible via MCP
- [ ] Config save/load accessible via MCP
- [ ] All export formats accessible via MCP
- [ ] All CLI arguments accessible via MCP
- [ ] Documentation updated

## Work Log

### 2026-02-25 - Agent-Native Review Discovery

**By:** Claude Code (Agent-Native Reviewer)

**Actions:**
- Mapped all 18 CLI capabilities to agent tools
- Found zero parity between CLI and MCP

**Learnings:**
- This is a systemic issue - future CLI features must include MCP parity
