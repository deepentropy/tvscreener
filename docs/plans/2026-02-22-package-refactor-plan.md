---
date: 2026-02-22
topic: refactoring
status: completed
---

# Package Refactoring Plan

## Overview

Refactor the `tvscreener` package to follow KISS, DRY, SOLID, YAGNI principles by separating CLI from core library code.

## Research Findings

Based on best practices from Python Packaging Guide, Click, and Clean Architecture:

### Recommended Patterns

1. **src/ layout** - All importable code under `src/`
2. **Thin CLI** - CLI should only parse args and delegate (50-100 lines)
3. **Explicit re-exports** - In `__init__.py` for backward compatibility
4. **Use Click or Typer** - For cleaner CLI decorators (optional)
5. **Deprecation warnings** - Before removing old import paths

## Goals

1. **Separate CLI from library** - CLI should be a thin layer on top of core functionality
2. **Keep screeners at top level** - Expose screeners in main package `__init__.py`
3. **Extend, not replace** - Build on existing code, don't rewrite
4. **Clean imports** - No circular dependencies, clear module boundaries

## Current Structure

```
tvscreener/
├── __init__.py           # Exports all screeners, fields, etc.
├── cli.py                # CLI entry point (THICK - contains business logic)
├── score.py              # Scoring engine
├── filter.py             # Filter classes
├── beauty.py             # Table formatting
├── config/
│   └── universe.py       # AssetUniverse config
├── constants/            # Forex, stocks, etc.
├── core/                 # Screener base classes
├── field/               # Field enums
├── mcp/                 # MCP server
├── screeners/           # NEW: Strategy & opportunity screeners
│   ├── __init__.py
│   ├── forex_opportunity.py
│   └── forex_strategy.py
└── util.py              # Utilities
```

## Problems

1. **CLI is too thick** - Contains scan logic that should be in screeners
2. **Screeners buried** - `screeners/` subpackage not exported from main `__init__.py`
3. **Mixed concerns** - CLI mixes arg parsing, business logic, and output formatting

## Proposed Structure

```
tvscreener/
├── __init__.py           # Exports: screeners, fields, filters, beauty
├── cli.py                # THIN: Only arg parsing + delegation to screeners
├── lib/                  # NEW: Core library code
│   ├── __init__.py       # Re-exports from submodules
│   ├── score.py
│   ├── filter.py
│   ├── beauty.py
│   ├── config/
│   │   └── universe.py
│   ├── constants/
│   │   ├── __init__.py
│   │   ├── forex.py
│   │   ├── stocks.py
│   │   ├── commodity.py
│   │   └── crypto.py
│   ├── core/
│   │   └── ...
│   ├── field/
│   │   └── ...
│   ├── mcp/
│   │   └── ...
│   ├── screeners/
│   │   ├── __init__.py   # Exports: ForexOpportunityScreener, ForexStrategyScanner
│   │   ├── forex_opportunity.py
│   │   └── forex_strategy.py
│   └── util.py
└── cli/                  # NEW: CLI package
    ├── __init__.py       # Re-exports CLI functions
    └── main.py           # Entry point
```

## Phase 1: Create Parallel Structure

### 1.1 Alternative: Consider src/ Layout

For cleaner separation (from Python Packaging Guide):

```
tvscreener/
├── pyproject.toml
└── src/
    └── tvscreener/
        ├── __init__.py       # Re-exports
        ├── cli.py            # Thin CLI
        └── lib/              # Core library
            ├── __init__.py
            ├── screeners/
            ├── score.py
            └── ...
```

**Pros:** Cleanest separation, avoids accidental local imports
**Cons:** Requires updating all import paths

### 1.2 Recommended: Keep Flat, Add cli/ Subpackage

For minimal changes (recommended for this project):

```
tvscreener/
├── __init__.py           # Re-exports EVERYTHING for backward compat
├── cli/
│   ├── __init__.py       # Re-exports
│   └── main.py           # Thin entry point
├── lib/                  # Core (move core modules here)
│   ├── __init__.py
│   ├── screeners/
│   └── ...
└── (keep root modules for backward compat)
```

### 1.3 Create `tvscreener/lib/` directory

```
tvscreener/lib/
├── __init__.py
├── score.py          # Copy from root
├── filter.py         # Copy from root
├── beauty.py         # Copy from root
├── util.py           # Copy from root
├── config/
│   ├── __init__.py
│   └── universe.py
├── constants/
│   ├── __init__.py
│   ├── forex.py
│   ├── stocks.py
│   ├── commodity.py
│   └── crypto.py
├── core/
│   └── ...           # All core modules
├── field/
│   └── ...           # All field modules
├── mcp/
│   └── ...           # All mcp modules
└── screeners/
    ├── __init__.py
    ├── forex_opportunity.py
    └── forex_strategy.py
```

### 1.2 Update imports in screeners

```python
# Before (tvscreener/screeners/forex_strategy.py)
from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener

# After
from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener
```

---

## Phase 2: Thin the CLI

### 2.1 Extract business logic from `cli.py`

Current `cli.py` (~200 lines) contains:
- Arg parsing ✅ (keep)
- **Scan logic** ❌ (move to screeners)
- Output formatting ✅ (keep in CLI)
- Universe handling ✅ (keep in CLI)

**Target CLI (~80 lines):**

```python
# tvscreener/cli/main.py
from argparse import ArgumentParser
from tvscreener.lib.screeners import ForexOpportunityScreener, ForexStrategyScanner

def run_opportunity_scan(args):
    screener = ForexOpportunityScreener(...)
    df = screener.get_opportunities()
    # ... formatting

def run_strategy_scan(args):
    scanner = ForexStrategyScanner(...)
    df = scanner.scan()
    # ... formatting

def main():
    parser = ArgumentParser()
    # ... args
    if args.scanner == "opportunity":
        run_opportunity_scan(args)
    else:
        run_strategy_scan(args)
```

### 2.2 Update entry point

```toml
# pyproject.toml
[project.scripts]
tvscreener-scan = "tvscreener.cli.main:main"
```

---

## Phase 3: Clean Up Exports

### 3.1 Main `__init__.py`

```python
# tvscreener/__init__.py
# Re-export from lib for backward compatibility
from tvscreener.lib.screeners import ForexOpportunityScreener, ForexStrategyScanner
from tvscreener.lib import score, filter, beauty, util
from tvscreener.lib.field import *
from tvscreener.lib.core import StockScreener, ForexScreener, etc.

__all__ = [
    # Screeners
    "ForexOpportunityScreener",
    "ForexStrategyScanner",
    # ... existing exports
]
```

---

## Phase 4: Deprecate Old Imports (Optional)

### 4.1 Add deprecation warnings

Keep old import paths working with warnings:

```python
# tvscreener/score.py (old location - keep for backward compat)
import warnings

def ScoringEngine(*args, **kwargs):
    warnings.warn(
        "tvscreener.score is deprecated. Use tvscreener.lib.score instead.",
        DeprecationWarning,
        stacklevel=2
    )
    from tvscreener.lib.score import ScoringEngine
    return ScoringEngine(*args, **kwargs)
```

### 4.2 Alternative: Use `__getattr__` for lazy deprecation

```python
# tvscreener/__init__.py
def __getattr__(name):
    if name == "ScoringEngine":
        import warnings
        warnings.warn(
            "tvscreener.ScoringEngine moved to tvscreener.lib.score",
            DeprecationWarning,
            stacklevel=2
        )
        return getattr(__import__("tvscreener.lib.score"), name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
```

---

## Key Best Practices Applied

| File | Action |
|------|--------|
| `tvscreener/lib/` | Create - move core code here |
| `tvscreener/cli/` | Create - thin CLI |
| `tvscreener/__init__.py` | Update exports |
| `tvscreener/screeners/` | Move to `lib/screeners/` |
| `pyproject.toml` | Update entry points |
| `tvscreener/cli.py` | Keep for backward compat or remove |

---

## Backward Compatibility

1. **Keep old imports working** - Use `__init__.py` re-exports
2. **Update entry point** - `tvscreener-scan` points to new CLI
3. **No breaking changes** - Users can import from both old and new paths

---

## Success Criteria

- [ ] CLI is thin (< 100 lines)
- [ ] Screeners exported from main package
- [ ] Clear separation: `lib/` vs `cli/`
- [ ] All imports work (backward compatible)
- [ ] All tests pass

---

## Effort Estimate

| Phase | Effort |
|-------|--------|
| Phase 1: Create lib/ structure | 30 min |
| Phase 2: Thin CLI | 20 min |
| Phase 3: Clean exports | 10 min |
| Phase 4: Deprecations (optional) | 15 min |
| **Total** | **~75 min** |

---

## Key Best Practices Applied

| Principle | How Applied |
|-----------|-------------|
| **KISS** | Simple flat structure, minimal changes |
| **DRY** | Re-exports in `__init__.py`, no duplication |
| **SOLID** | CLI depends on lib, not vice versa (DIP) |
| **YAGNI** | Only create structure that's needed now |

### References

- [Python Packaging User Guide - src layout](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Click documentation](https://click.palletsprojects.com/)
- [Clean Architecture in Python](https://github.com/nens/clean-python)
