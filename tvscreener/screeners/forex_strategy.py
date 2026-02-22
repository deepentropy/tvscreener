from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal

import pandas as pd

from tvscreener.screeners.forex_opportunity import ForexOpportunityScreener
from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS

logger = logging.getLogger(__name__)

StrategyType = Literal["trend_following", "mean_reversion", "breakout", "hybrid", "all"]
Direction = Literal["long", "short", "all"]


@dataclass
class StrategyConfig:
    min_confluence: int = 1
    include_strategies: list[StrategyType] = field(default_factory=lambda: ["all"])
    direction: Direction = "all"
    trend_threshold: float = 0.0
    mr_threshold: float = 0.2
    min_roc: float | None = None


@dataclass
class ForexStrategyScanner:
    pairs: list[str] = field(default_factory=lambda: DEFAULT_FOREX_PAIRS)
    timeframes: list[str] = field(default_factory=lambda: ["240", "60", "15"])
    config: StrategyConfig = field(default_factory=StrategyConfig)

    def __post_init__(self) -> None:
        self._screener = ForexOpportunityScreener(
            pairs=self.pairs, timeframes=self.timeframes
        )

    def scan(self) -> pd.DataFrame:
        """Scan selected strategies and return combined results."""
        raw_data = self._screener.get_opportunities()

        if raw_data.empty:
            return pd.DataFrame()

        strategies_to_run = self.config.include_strategies
        if "all" in strategies_to_run:
            strategies_to_run = [
                "trend_following",
                "mean_reversion",
                "hybrid",
                "breakout",
            ]

        results = []

        if "trend_following" in strategies_to_run:
            trend_results = self.scan_trend_following(raw_data)
            if not trend_results.empty:
                results.append(trend_results)

        if "mean_reversion" in strategies_to_run:
            mr_results = self.scan_mean_reversion(raw_data)
            if not mr_results.empty:
                results.append(mr_results)

        if "hybrid" in strategies_to_run:
            hybrid_results = self.scan_hybrid(raw_data)
            if not hybrid_results.empty:
                results.append(hybrid_results)

        if "breakout" in strategies_to_run:
            breakout_results = self.scan_breakout(raw_data)
            if not breakout_results.empty:
                results.append(breakout_results)

        if not results:
            return pd.DataFrame()

        combined = pd.concat(results, ignore_index=True)

        combined = self._apply_filters(combined)

        return combined

    def scan_trend_following(
        self, raw_data: pd.DataFrame | None = None
    ) -> pd.DataFrame:
        """HTF + STF confluence - trend alignment across timeframes."""
        if raw_data is None:
            raw_data = self._screener.get_opportunities()
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_trend_following(raw_data)

    def scan_mean_reversion(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """LTF oscillator extremes - overbought/oversold."""
        if raw_data is None:
            raw_data = self._screener.get_opportunities()
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_mean_reversion(raw_data)

    def scan_hybrid(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """HTF trend + LTF mean reversion."""
        if raw_data is None:
            raw_data = self._screener.get_opportunities()
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_hybrid(raw_data)

    def scan_breakout(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """Multi-TF momentum alignment."""
        if raw_data is None:
            raw_data = self._screener.get_opportunities()
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_breakout(raw_data)

    def _detect_trend_following(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect trend following setups: HTF + STF both bullish or both bearish."""
        result = df.copy()

        htf_col = "Recommend All|240"
        stf_col = "Recommend All|60"

        if htf_col not in result.columns or stf_col not in result.columns:
            return pd.DataFrame()

        htf_trend = result[htf_col].fillna(0)
        stf_trend = result[stf_col].fillna(0)

        long_mask = (htf_trend > self.config.trend_threshold) & (
            stf_trend > self.config.trend_threshold
        )
        short_mask = (htf_trend < -self.config.trend_threshold) & (
            stf_trend < -self.config.trend_threshold
        )

        result = result[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "trend_following"
        result["HTF_TREND"] = htf_trend
        result["STF_TREND"] = stf_trend

        result = self._add_confluence_and_direction(result)

        return result

    def _detect_mean_reversion(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect mean reversion: LTF oscillator extremes."""
        result = df.copy()

        ltf_col = "Recommend Other|15"

        if ltf_col not in result.columns:
            return pd.DataFrame()

        osc_value = result[ltf_col].fillna(0)

        long_mask = osc_value < -self.config.mr_threshold
        short_mask = osc_value > self.config.mr_threshold

        result = result[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "mean_reversion"
        result["LTF_MOMENTUM"] = osc_value

        result["DIRECTION"] = result["LTF_MOMENTUM"].apply(
            lambda x: "long" if x < -self.config.mr_threshold else "short"
        )
        result["CONFLUENCE_SCORE"] = 1

        return result

    def _detect_hybrid(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect hybrid: HTF trend + LTF mean reversion."""
        result = df.copy()

        htf_col = "Recommend All|240"
        ltf_col = "Recommend Other|15"

        if htf_col not in result.columns or ltf_col not in result.columns:
            return pd.DataFrame()

        htf_trend = result[htf_col].fillna(0)
        ltf_osc = result[ltf_col].fillna(0)

        long_mask = (htf_trend > self.config.trend_threshold) & (
            ltf_osc < -self.config.mr_threshold
        )
        short_mask = (htf_trend < -self.config.trend_threshold) & (
            ltf_osc > self.config.mr_threshold
        )

        result = result[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "hybrid"
        result["HTF_TREND"] = htf_trend
        result["LTF_MOMENTUM"] = ltf_osc

        result["DIRECTION"] = result["HTF_TREND"].apply(
            lambda x: "long" if x > 0 else "short"
        )
        result["CONFLUENCE_SCORE"] = 2

        return result

    def _detect_breakout(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect breakout: Multi-TF momentum alignment."""
        result = df.copy()

        roc_cols = [f"Roc|{tf}" for tf in self.timeframes]

        available_roc_cols = [c for c in roc_cols if c in result.columns]
        if not available_roc_cols:
            return pd.DataFrame()

        roc_values = result[available_roc_cols].fillna(0)

        if self.config.min_roc is not None:
            long_mask = (roc_values > self.config.min_roc).all(axis=1)
            short_mask = (roc_values < -self.config.min_roc).all(axis=1)
        else:
            long_mask = (roc_values > 0).all(axis=1)
            short_mask = (roc_values < 0).all(axis=1)

        result = result[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "breakout"

        for col in available_roc_cols:
            if col not in result.columns:
                continue
            tf = col.split("|")[-1]
            result[f"ROC_{tf}"] = result[col]

        result["DIRECTION"] = result[available_roc_cols[0]].apply(
            lambda x: "long" if x > 0 else "short"
        )
        result["CONFLUENCE_SCORE"] = len(available_roc_cols)

        return result

    def _add_confluence_and_direction(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add confluence score and direction to results."""
        if df.empty:
            return df

        if "HTF_TREND" in df.columns and "STF_TREND" in df.columns:
            htf = df["HTF_TREND"].fillna(0)
            stf = df["STF_TREND"].fillna(0)

            aligned = ((htf > 0) & (stf > 0)) | ((htf < 0) & (stf < 0))
            df["CONFLUENCE_SCORE"] = aligned.astype(int) + 1
            df["DIRECTION"] = htf.apply(lambda x: "long" if x > 0 else "short")

        return df

    def _apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply config filters to results."""
        if df.empty:
            return df

        if self.config.direction != "all":
            df = df[df["DIRECTION"] == self.config.direction]

        if self.config.min_confluence > 0:
            df = df[df["CONFLUENCE_SCORE"] >= self.config.min_confluence]

        return df

    def to_csv(self, path: str, include_index: bool = False) -> None:
        df = self.scan()
        df.to_csv(path, index=include_index)
        logger.info(f"Saved {len(df)} signals to {path}")

    def to_json(self, path: str, orient: str = "records") -> None:
        df = self.scan()
        df.to_json(path, orient=orient, indent=2)
        logger.info(f"Saved {len(df)} signals to {path}")

    def print_summary(self) -> None:
        try:
            from rich.console import Console
            from rich.table import Table

            console = Console()
            results = self.scan()

            if results.empty:
                console.print("[yellow]No signals found[/yellow]")
                return

            for strategy in results["STRATEGY"].unique():
                strategy_df = results[results["STRATEGY"] == strategy]

                table = Table(title=f"Strategy: {strategy}")
                table.add_column("Pair", style="cyan")
                table.add_column("Direction", style="green")
                table.add_column("Confluence", justify="right")

                for _, row in strategy_df.iterrows():
                    table.add_row(
                        row.get("Name", row.get("PAIR", "N/A")),
                        row["DIRECTION"],
                        str(row.get("CONFLUENCE_SCORE", "N/A")),
                    )

                console.print(table)

            console.print(f"\n[dim]Total signals: {len(results)}[/dim]")

        except ImportError:
            df = self.scan()
            print(df.to_string())
