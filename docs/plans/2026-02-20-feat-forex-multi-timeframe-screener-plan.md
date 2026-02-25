---
title: Forex Multi-Timeframe Screener with Ratings & ROC
type: feat
date: 2026-02-20
---

## Enhancement Summary

**Deepened on:** 2026-02-20
**Sections enhanced:** Technical Approach, Dependencies, Implementation Phases, Acceptance Criteria

### Key Improvements
1. Added Rich library for colored CLI output (recommended for modern Python CLI)
2. Added async support consideration for faster multi-timeframe queries
3. Added proper type hints throughout the class
4. Added error handling and rate limiting considerations

### Technical Review (Kieran Python Reviewer - 8/10)
**Actionable improvements from review:**
1. Use `Literal` types for known string values (rating_type, operator)
2. Clarify the rating filter API - use dataclass-based configuration
3. Add exception types for error handling
4. Consider dataclass-based configuration for filters
5. Add `__repr__` for debugging
6. Add logging for debugging

### New Considerations Discovered
- TradingView API rate limits: streaming minimum 1.0 seconds between requests
- Use `with_interval()` method for dynamic timeframe fields
- Rating values: -1 (strong sell) to +1 (strong buy)
- Use dataclasses for filter configuration (recommended by reviewer)

---

# Forex Multi-Timeframe Screener with Ratings & ROC

## Overview

A modular Python class for screening forex majors/minors (~20 pairs) across multiple timeframes (15m, 1H, 4H), filtering by TradingView ratings and ranking by Rate of Change to identify trading opportunities.

## Problem Statement

Traders need a unified view of forex opportunities across multiple timeframes, combining:
- Multi-timeframe analysis (15m, 1H, 4H)
- TradingView rating signals (Overall, MA-based, Oscillators-based)
- Rate of Change momentum filtering/ranking

Currently, users must make multiple API calls and manually combine results.

## Proposed Solution

Create a reusable `ForexOpportunityScreener` class that:
1. Screens ~20 forex major + minor pairs
2. Fetches data across 3 timeframes (15m, 1H, 4H)
3. Filters by rating thresholds (Recommend.All, Recommend.MA, Recommend.OS)
4. Ranks by Rate of Change (positive → negative for long tops, short bottoms)
5. Outputs to CLI (colored) and CSV/JSON files

## Technical Approach

### Architecture

```
ForexOpportunityScreener (dataclass)
├── pairs: list[str]
├── timeframes: list[str]
├── config: ForexScreenerConfig
├── get_opportunities() -> pd.DataFrame
├── to_csv(path: str, include_index: bool = False)
├── to_json(path: str, orient: str = 'records')
└── __repr__() -> str

ForexScreenerConfig (dataclass)
├── rating_filters: list[RatingFilter]
├── roc_filter: RocFilter | None
└── technical_filters: list[TechnicalFilter]

RatingFilter (dataclass)
├── rating_type: Literal['all', 'ma', 'oscillator']
└── threshold: float

RocFilter (dataclass)
├── min_roc: float | None
└── max_roc: float | None
```

**Updated example usage:**
```python
from tvscreener.screeners.forex_opportunity import (
    ForexOpportunityScreener,
    ForexScreenerConfig,
    RatingFilter,
    RocFilter,
)

config = ForexScreenerConfig(
    rating_filters=[
        RatingFilter('all', 0.1),
        RatingFilter('ma', 0.1),
        RatingFilter('oscillator', 0.1),
    ],
    roc_filter=RocFilter(min_roc=0),
)

scanner = ForexOpportunityScreener(config=config)
df = scanner.get_opportunities()
scanner.to_csv('forex_opportunities.csv')
print(scanner)  # __repr__ for debugging
```

### Research Insights

**Best Practices:**
- Use `rich` library for colored CLI output - it's the modern standard for Python CLI tools
- Implement proper type hints throughout for IDE support and documentation
- Use dataclasses or Pydantic for configuration objects
- Add `__repr__` for debugging

**Performance Considerations:**
- TradingView API rate limits: minimum 1.0 seconds between streaming requests
- Consider `asyncio` for parallel fetching across timeframes (Phase 2 enhancement)
- Cache common field selections to reduce API overhead
- Target: < 10 seconds for full scan of 20 pairs × 3 timeframes

**CLI Design (from 2025-2026 best practices):**
- Use Click or Typer if CLI becomes complex; stick to simple print for MVP
- Include `--help` equivalent, `--output` flag for file export
- Use standard exit codes (0 success, 1 error)
- Progress bars for long operations

**Implementation Details:**
```python
from rich.console import Console
from rich.table import Table

console = Console()

def print_summary(df: pd.DataFrame) -> None:
    table = Table(title="Forex Opportunities")
    table.add_column("Pair", style="cyan")
    table.add_column("Rating", style="green")
    table.add_column("ROC", style="yellow")
    # ... add rows
    console.print(table)
```

**Edge Cases:**
- Handle API timeout with retry logic (3 attempts, exponential backoff)
- Handle empty results gracefully (no pairs match filters)
- Validate forex pair symbols against TradingView format
- Handle None values in ratings/ROC fields

**Exception types to define:**
```python
class ForexScreenerError(Exception):
    """Base exception for ForexOpportunityScreener."""
    pass

class InvalidPairError(ForexScreenerError):
    """Raised when forex pair symbol is invalid."""
    pass

class FilterConfigurationError(ForexScreenerError):
    """Raised when filter configuration is invalid."""
    pass

class RateLimitError(ForexScreenerError):
    """Raised when API rate limit is exceeded."""
    pass
```

**Logging:**
```python
import logging

logger = logging.getLogger(__name__)

def get_opportunities(self) -> pd.DataFrame:
    logger.info(f"Scanning {len(self.pairs)} pairs across {len(self.timeframes)} timeframes")
    # ... implementation
```

### Key Implementation Details

**Files to create:**
- `tvscreener/screeners/__init__.py` - Package init
- `tvscreener/screeners/forex_opportunity.py` - Main screener class with dataclasses
- `tvscreener/constants/forex.py` - Forex pairs and timeframe constants
- `tvscreener/exceptions.py` - Exception classes
- `examples/forex_opportunity_screen.py` - Usage example
- `tests/test_forex_opportunity.py` - Unit tests

**Forex pairs to include (majors + minors):**
```python
FOREX_MAJORS = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'USDCAD', 'AUDUSD', 'NZDUSD']
FOREX_MINORS = ['EURGBP', 'EURJPY', 'GBPJPY', 'EURCHF', 'AUDJPY', 'EURCAD', 
                'CADJPY', 'CHFJPY', 'NZDJPY', 'GBPAUD', 'EURAUD', 'AUDNZD',
                'EURNZD', 'GBPCAD', 'AUDCAD', 'GBPNZD', 'EURNOK', 'EURSEK']
PAIRS = MAJORS + MINORS  # ~20 pairs
```

**Timeframes:**
```python
TIMEFRAMES = ['15', '60', '240']  # 15m, 1H, 4H
```

**Rating fields (pre-baked in library):**
- `ForexField.RECOMMEND_ALL_15`, `_60`, `_240` - Overall rating
- `ForexField.RECOMMEND_MA_15`, `_60`, `_240` - Moving averages rating  
- `ForexField.RECOMMEND_OSCILLATOR_15`, `_60`, `_240` - Oscillators rating

**ROC field:**
- `ForexField.ROC_15`, `_60`, `_240` - Rate of Change per timeframe

**Example usage:**
```python
from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener

scanner = ForexOpportunityScreener()
scanner.set_rating_filter('all', threshold=0.1)   # Buy signals only
scanner.set_rating_filter('ma', threshold=0.1)
scanner.set_rating_filter('oscillator', threshold=0.1)
scanner.set_roc_filter(min_roc=0)  # Positive ROC only

df = scanner.get_opportunities()
scanner.to_csv('forex_opportunities.csv')
scanner.print_summary()
```

**Output columns:**
- NAME, PRICE
- RATING_ALL_15M, RATING_ALL_1H, RATING_ALL_4H
- RATING_MA_15M, RATING_MA_1H, RATING_MA_4H
- RATING_OSCILLATOR_15M, RATING_OSCILLATOR_1H, RATING_OSCILLATOR_4H
- ROC_15M, ROC_1H, ROC_4H
- FINAL_SCORE (computed ranking)

**Ranking algorithm (separate testable function):**
```python
def calculate_opportunity_score(
    ratings: dict[str, float],
    rocs: dict[str, float],
    timeframe_weights: dict[str, float] | None = None
) -> float:
    """Calculate composite score for ranking opportunities.
    
    Args:
        ratings: Dict of timeframe -> rating value
        rocs: Dict of timeframe -> ROC value
        timeframe_weights: Optional weights for each timeframe
        
    Returns:
        Composite score for sorting
    """
    weights = timeframe_weights or {'15': 0.5, '60': 0.3, '240': 0.2}
    # ... implementation
```

**Constants file:**
```python
# tvscreener/constants/forex.py
FOREX_MAJORS = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'USDCAD', 'AUDUSD', 'NZDUSD']
FOREX_MINORS = ['EURGBP', 'EURJPY', 'GBPJPY', 'EURCHF', 'AUDJPY', 'EURCAD', ...]
DEFAULT_TIMEFRAMES = ['15', '60', '240']
DEFAULT_TIMEFRAME_WEIGHTS = {'15': 0.5, '60': 0.3, '240': 0.2}
```

## Implementation Phases

### Phase 1: Core Class (MVP)
- [ ] Create `ForexOpportunityScreener` dataclass
- [ ] Create `ForexScreenerConfig`, `RatingFilter`, `RocFilter` dataclasses
- [ ] Create exception classes in `tvscreener/exceptions.py`
- [ ] Create constants in `tvscreener/constants/forex.py`
- [ ] Implement `get_opportunities()` with multi-timeframe fetch
- [ ] Implement `calculate_opportunity_score()` ranking function
- [ ] Add `__repr__` for debugging
- [ ] Add logging
- [ ] Add error handling (API timeouts, invalid pairs)
- [ ] Add retry logic (3 attempts, exponential backoff)
- [ ] CLI output with basic formatting

### Phase 2: Enhanced Filtering
- [ ] ROC filtering
- [ ] Combined rating filters (All + MA + OS)
- [ ] pandas-based post-filtering
- [ ] Add rate limiting (1.0s minimum between API calls)
- [ ] Consider async/await for parallel timeframe fetching
- [ ] Add context manager support (`__enter__`, `__exit__`)
- [ ] Configuration validation in `__post_init__`

### Phase 3: Output & Polish
- [ ] CSV/JSON export
- [ ] Rich CLI output with colors
- [ ] Summary statistics

### Phase 4: Testing & Docs
- [ ] Unit tests
- [ ] Mock API responses for testing
- [ ] Example script demonstrates full workflow
- [ ] Documentation
- [ ] Add type hints validation (mypy)
- [ ] Add linting (ruff)

## Acceptance Criteria

- [ ] Can screen 20 forex pairs across 3 timeframes in single call
- [ ] Filter by Recommend.All, Recommend.MA, Recommend.OS thresholds
- [ ] Rank opportunities by combined rating + ROC score
- [ ] Output sorted list (positive ROC first, negative last)
- [ ] CLI output with colored formatting
- [ ] Export to CSV and JSON files
- [ ] Unit tests passing
- [ ] Example script demonstrates full workflow
- [ ] Handles API timeouts gracefully (retry logic works)
- [ ] Handles empty results (no pairs match filters)
- [ ] Type hints pass mypy validation
- [ ] Code passes ruff linting

## Dependencies

- `tvscreener` (already installed)
- `pandas>=1.3.0` (already dependency)
- `rich` (for colored CLI output - recommended 2025-2026 standard)
- `typer` or `click` (optional - for CLI if needed)
- `asyncio` (built-in, for Phase 2 async enhancement)

**New dependency to add to `pyproject.toml` or `requirements.txt`:**
```toml
dependencies = [
    # ... existing
    "rich>=13.0.0",
]
```

## Success Metrics

- Single method call returns complete opportunity scan
- Results sorted by quality (best opportunities first)
- Both CLI and file output work correctly
- Performance: < 10 seconds for full scan

## References

- `tvscreener/core/forex.py` - ForexScreener base class
- `tvscreener/field/forex.py:1948-1970` - Rating field enums
- `tvscreener/field/forex.py:1648-1657` - ROC field enums
- `docs/screeners/forex.md` - Existing forex examples
- `docs/guide/time-intervals.md` - Multi-timeframe documentation

## Next Steps

→ `/workflows:work` to implement this plan
