---
title: Forex Strategy Scanner with Multi-Timeframe Confluence
type: feat
date: 2026-02-20
---

# Forex Strategy Scanner with Multi-Timeframe Confluence

## Enhancement Summary

**Deepened on:** 2026-02-20
**Sections enhanced:** Strategy Definitions, API Design, Implementation Details

### Key Improvements
1. Added threshold parameters for strategy configuration
2. Added KISS principle - reuse existing ForexOpportunityScreener
3. Added CLI output pattern following existing print_summary()
4. Added error handling for API failures

---

## Overview

Scan forex majors/minors (27 pairs) for strategy-specific opportunities using multi-timeframe confluence detection. Identify trend following and mean reversion setups across HTF/STF/LTF combinations.

## Base Universe

### Forex Pairs

| Category | Count | Pairs |
|----------|-------|-------|
| Majors | 7 | EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD |
| Minors | 20 | EURGBP, EURJPY, GBPJPY, EURCHF, AUDJPY, EURCAD, CADJPY, CHFJPY, NZDJPY, GBPAUD, EURAUD, AUDNZD, EURNZD, GBPCAD, AUDCAD, GBPNZD, EURNOK, EURSEK |
| **Total** | **27** | |

### Timeframe Hierarchy

| Role | Timeframe | Label | Purpose |
|------|-----------|-------|---------|
| HTF (High) | 240 | 4H | Primary trend direction |
| STF (Signal) | 60 | 1H | Secondary confirmation |
| LTF (Entry) | 15 | 15m | Entry timing / mean reversion |

## Strategy Definitions

### 1. Trend Following (HTF + STF Confluence)

**Logic**: Higher timeframe trend aligns with signal timeframe trend

| Condition | Long Setup | Short Setup |
|-----------|------------|-------------|
| HTF (4H) | Recommend.All\|240 > 0 | Recommend.All\|240 < 0 |
| STF (1H) | Recommend.All\|60 > 0 | Recommend.All\|60 < 0 |

**Confluence Levels:**
- Strong (3/3): HTF + STF + MA aligned
- Medium (2/3): HTF + STF aligned
- Weak (1/3): Only one TF aligned

### 2. Mean Reversion (LTF Extremes)

**Logic**: Oscillators at extreme readings suggest reversal

| Condition | Long (Oversold) | Short (Overbought) |
|-----------|-----------------|-------------------|
| Oscillator | Recommend.Other\|15 < -1 | Recommend.Other\|15 > 1 |

**Extended Zones:**
- Strong oversold: < -2
- Oversold: -1 to -2
- Neutral: -1 to 1
- Overbought: 1 to 2
- Strong overbought: > 2

### 3. Hybrid: Trend + Mean Reversion

**Logic**: Trade with HTF trend, enter on LTF mean reversion

| Variant | HTF (4H) | LTF (15m) | Direction |
|---------|-----------|-----------|-----------|
| Trend + MR Long | Recommend.All\|240 > 0 | Recommend.Other\|15 < -1 | Long |
| Trend + MR Short | Recommend.All\|240 < 0 | Recommend.Other\|15 > 1 | Short |

### 4. Breakout Confluence

**Logic**: Multiple timeframes showing momentum

| Condition | Long | Short |
|-----------|------|-------|
| HTF | ROC\|240 > 0 | ROC\|240 < 0 |
| STF | ROC\|60 > 0 | ROC\|60 < 0 |
| LTF | ROC\|15 > 0 | ROC\|15 < 0 |

## Data Requirements

### TradingView Fields

| Field | Timeframes | Purpose |
|-------|------------|---------|
| Recommend.All | 15, 60, 240 | Overall technical consensus |
| Recommend.MA | 15, 60, 240 | Moving average alignment |
| Recommend.Other | 15, 60, 240 | Oscillator readings |
| Roc | 15, 60, 240 | Rate of change momentum |

### Data Fetching

```python
# Fetch all required fields for all timeframes
FIELDS = [
    "Name",
    "Symbol", 
    "Price",
    "Recommend All|15", "Recommend All|60", "Recommend All|240",
    "Recommend Ma|15", "Recommend Ma|60", "Recommend Ma|240",
    "Recommend Other|15", "Recommend Other|60", "Recommend Other|240",
    "Roc|15", "Roc|60", "Roc|240",
]
```

## Output Schema

### DataFrame Columns

| Column | Type | Description |
|--------|------|-------------|
| `PAIR` | str | Currency pair (e.g., EURUSD) |
| `EXCHANGE` | str | Exchange with best volume |
| `PRICE` | float | Current price |
| `HTF_TREND` | int | 4H recommendation (-5 to +5) |
| `STF_TREND` | int | 1H recommendation (-5 to +5) |
| `LTF_MOMENTUM` | int | 15m oscillator (-5 to +5) |
| `HTF_ROC` | float | 4H rate of change |
| `STF_ROC` | float | 1H rate of change |
| `LTF_ROC` | float | 15m rate of change |
| `STRATEGY` | str | trend_following, mean_reversion, breakout, hybrid |
| `CONFLUENCE_SCORE` | int | 0-3 aligned timeframes |
| `DIRECTION` | str | long, short, neutral |
| `SIGNAL_STRENGTH` | str | strong, medium, weak |

## API Design

### Class Structure

```python
from dataclasses import dataclass, field
from typing import Literal

StrategyType = Literal["trend_following", "mean_reversion", "breakout", "hybrid", "all"]
Direction = Literal["long", "short", "all"]

@dataclass
class StrategyConfig:
    min_confluence: int = 2
    min_signal_strength: str = "weak"  # "strong", "medium", "weak"
    include_strategies: list[StrategyType] = field(default_factory=lambda: ["all"])
    direction: Direction = "all"
    # Threshold parameters
    trend_threshold: float = 0.0  # Recommend.All must be >0 or <0
    mr_threshold: float = 1.0    # Mean reversion extreme threshold
    min_roc: float | None = None  # Minimum ROC for breakout

@dataclass
class ForexStrategyScanner:
    pairs: list[str] = field(default_factory=lambda: DEFAULT_FOREX_PAIRS)
    timeframes: list[str] = field(default_factory=lambda: ["240", "60", "15"])
    config: StrategyConfig = field(default_factory=StrategyConfig)
    
    def __post_init__(self):
        # Reuse existing screener for data fetching (KISS)
        from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener
        self._screener = ForexOpportunityScreener(
            pairs=self.pairs,
            timeframes=self.timeframes
        )
    
    def scan(self) -> pd.DataFrame:
        """Scan all strategies and return combined results"""
    
    def scan_trend_following(self) -> pd.DataFrame:
        """HTF + STF confluence"""
    
    def scan_mean_reversion(self) -> pd.DataFrame:
        """LTF oscillator extremes"""
    
    def scan_breakout(self) -> pd.DataFrame:
        """Multi-TF momentum alignment"""
    
    def scan_hybrid(self) -> pd.DataFrame:
        """HTF trend + LTF mean reversion"""
    
    def to_csv(self, path: str) -> None:
        """Export results to CSV"""
    
    def to_json(self, path: str) -> None:
        """Export results to JSON"""
```

### Usage Example

```python
from tvscreener.screeners.forex_strategy import ForexStrategyScanner

# Initialize scanner with all 27 pairs
scanner = ForexStrategyScanner()

# Scan for all strategies
results = scanner.scan()

# Filter to specific strategy
trend_results = scanner.scan_trend_following()

# Filter by direction
long_only = results[results["DIRECTION"] == "long"]

# Strong signals only
strong = results[results["SIGNAL_STRENGTH"] == "strong"]

# Export
scanner.to_csv("forex_strategies.csv")
```

## Implementation Details

### KISS: Reuse Existing Components

**YAGNI**: Don't over-engineer. Reuse existing ForexOpportunityScreener:

```python
from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener

class ForexStrategyScanner:
    """Scanner that reuses existing screener for data fetching."""
    
    def __init__(self, pairs=None, timeframes=None):
        self._screener = ForexOpportunityScreener(
            pairs=pairs or DEFAULT_FOREX_PAIRS,
            timeframes=timeframes or ["240", "60", "15"]
        )
    
    def scan(self) -> pd.DataFrame:
        """Fetch data and apply strategy logic."""
        raw_data = self._screener.get_opportunities()
        # Apply strategy filters...
        return strategy_data
```

### Score Calculation

```python
def calculate_confluence(df: pd.DataFrame) -> pd.DataFrame:
    """Count aligned timeframes"""
    df["HTF_ALIGNED"] = ((df["HTF_TREND"] > 0) & (df["STF_TREND"] > 0)) | \
                        ((df["HTF_TREND"] < 0) & (df["STF_TREND"] < 0))
    df["STF_ALIGNED"] = df["HTF_ALIGNED"]
    df["LTF_EXTREME"] = (df["LTF_MOMENTUM"] > 1) | (df["LTF_MOMENTUM"] < -1)
    
    df["CONFLUENCE_SCORE"] = df["HTF_ALIGNED"].astype(int) + \
                             df["STF_ALIGNED"].astype(int) + \
                             df["LTF_EXTREME"].astype(int)
    return df
```

### Signal Strength

```python
def get_signal_strength(row) -> str:
    """Determine signal strength from scores"""
    if row["CONFLUENCE_SCORE"] >= 3 and abs(row["HTF_TREND"]) >= 3:
        return "strong"
    elif row["CONFLUENCE_SCORE"] >= 2:
        return "medium"
    else:
        return "weak"
```

### CLI Output (Follow Existing Pattern)

```python
def print_summary(self) -> None:
    """Rich CLI output - follow existing ForexOpportunityScreener pattern."""
    try:
        from rich.console import Console
        from rich.table import Table
        
        console = Console()
        results = self.scan()
        
        # Group by strategy
        for strategy in results["STRATEGY"].unique():
            strategy_df = results[results["STRATEGY"] == strategy]
            
            table = Table(title=f"Strategy: {strategy}")
            table.add_column("Pair", style="cyan")
            table.add_column("Direction", style="green")
            table.add_column("Confluence", justify="right")
            table.add_column("Strength", justify="right")
            
            for _, row in strategy_df.iterrows():
                table.add_row(
                    row["PAIR"],
                    row["DIRECTION"],
                    str(row["CONFLUENCE_SCORE"]),
                    row["SIGNAL_STRENGTH"]
                )
            
            console.print(table)
    except ImportError:
        print(results.to_string())
```

### Error Handling

```python
def scan(self) -> pd.DataFrame:
    """Scan with graceful error handling."""
    try:
        raw_data = self._screener.get_opportunities()
    except Exception as e:
        logger.error(f"Failed to fetch data: {e}")
        return pd.DataFrame()
    
    if raw_data.empty:
        logger.warning("No data returned")
        return pd.DataFrame()
    
    # Apply strategies...
    return results
```

## Acceptance Criteria

### Must Have
- [x] Implement ForexStrategyScanner class
- [x] Support all 27 major/minor pairs
- [x] Support 3 timeframes: 4H, 1H, 15m
- [x] Implement scan_trend_following()
- [x] Implement scan_mean_reversion() 
- [x] Implement scan_hybrid()
- [x] Calculate confluence score (0-3)
- [x] Determine direction (long/short)
- [x] Export to CSV
- [x] Export to JSON

### Should Have
- [x] Implement scan_breakout()
- [x] Signal strength classification
- [x] Rich CLI output with tables
- [x] Filter by min_confluence
- [x] Filter by direction

### Could Have
- [ ] Backtest-ready signal export
- [ ] Performance metrics per strategy
- [ ] Historical signal tracking

## Dependencies

- **Existing**: ForexOpportunityScreener, ForexField, DEFAULT_FOREX_PAIRS
- **New**: forex_strategy.py module in screeners/

## File Structure

```
tvscreener/
└── screeners/
    ├── __init__.py
    ├── forex_opportunity.py  (existing)
    └── forex_strategy.py     (new)
```

## References

- Composite scoring: `tvscreener/screeners/forex_opportunity.py`
- Timeframe constants: `tvscreener/constants/forex.py`
- Field definitions: `tvscreener/field/forex.py`
