from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal

import numpy as np
import pandas as pd

from tvscreener.constants.forex import DEFAULT_FOREX_PAIRS
from tvscreener.lib.screeners.export_helpers import get_export_function, print_summary
from tvscreener.lib.screeners.filter_utils import (
    apply_atr_filter,
    apply_ma_rating_filter,
    apply_volume_filter,
    detect_mean_reversion_signals,
)
from tvscreener.lib.screeners.forex_opportunity import ForexOpportunityScreener, ForexScreenerConfig

logger = logging.getLogger(__name__)

StrategyType = Literal["trend_following", "mean_reversion", "breakout", "hybrid", "all"]
Direction = Literal["long", "short", "all"]


@dataclass(frozen=True, slots=True)
class StrategyConfig:
    min_confluence: int = 1
    include_strategies: tuple[StrategyType, ...] = ("all",)
    direction: Direction = "all"
    trend_threshold: float = 0.0
    mr_threshold: float = 0.2
    min_roc: float | None = None
    min_volume: float | None = None
    max_atr: float | None = None
    min_ma_rating: float | None = None
    mean_reversion_signals: tuple[str, ...] = ()
    contract_type: Literal["spot", "cfd", "spreadbet", "all"] = "cfd"
    include_atr_fields: bool = False
    include_rsi_fields: bool = False


@dataclass
class ForexStrategyScanner:
    pairs: list[str] = field(default_factory=lambda: DEFAULT_FOREX_PAIRS)
    timeframes: list[str] = field(default_factory=lambda: ["240", "60", "15"])
    config: StrategyConfig = field(default_factory=StrategyConfig)
    _screener: ForexOpportunityScreener = field(init=False)
    _cached_results: pd.DataFrame | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        include_atr = self.config.include_atr_fields or self.config.max_atr is not None
        include_rsi = self.config.include_rsi_fields or bool(self.config.mean_reversion_signals)
        self._screener = ForexOpportunityScreener(
            pairs=self.pairs,
            timeframes=self.timeframes,
            config=ForexScreenerConfig(
                contract_type=self.config.contract_type,
                include_atr=include_atr,
                include_rsi=include_rsi,
            ),
        )

    def scan(self, use_cache: bool = False) -> pd.DataFrame:
        """Scan selected strategies and return combined results."""
        if use_cache and self._cached_results is not None:
            logger.info("Returning cached scan results")
            return self._cached_results

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
        combined = apply_volume_filter(combined, self.config.min_volume)
        combined = apply_atr_filter(combined, self.config.max_atr)
        combined = apply_ma_rating_filter(combined, self.config.min_ma_rating)
        combined = detect_mean_reversion_signals(combined, self.config.mean_reversion_signals)

        self._cached_results = combined
        return combined

    def _get_data_or_fetch(self, raw_data: pd.DataFrame | None) -> pd.DataFrame:
        """Fetch data if not provided, or return empty DataFrame if already empty."""
        if raw_data is None:
            raw_data = self._screener.get_opportunities()
        if raw_data.empty:
            return pd.DataFrame()
        return raw_data

    def scan_trend_following(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """HTF + STF confluence - trend alignment across timeframes."""
        raw_data = self._get_data_or_fetch(raw_data)
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_trend_following(raw_data)

    def scan_mean_reversion(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """LTF oscillator extremes - overbought/oversold."""
        raw_data = self._get_data_or_fetch(raw_data)
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_mean_reversion(raw_data)

    def scan_hybrid(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """HTF trend + LTF mean reversion."""
        raw_data = self._get_data_or_fetch(raw_data)
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_hybrid(raw_data)

    def scan_breakout(self, raw_data: pd.DataFrame | None = None) -> pd.DataFrame:
        """Multi-TF momentum alignment."""
        raw_data = self._get_data_or_fetch(raw_data)
        if raw_data.empty:
            return pd.DataFrame()
        return self._detect_breakout(raw_data)

    def _detect_trend_following(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect trend following setups: HTF + STF both bullish or both bearish."""
        htf_col = "Recommend All|240"
        stf_col = "Recommend All|60"

        if htf_col not in df.columns or stf_col not in df.columns:
            return pd.DataFrame()

        htf_trend = df[htf_col].fillna(0)
        stf_trend = df[stf_col].fillna(0)

        long_mask = (htf_trend > self.config.trend_threshold) & (
            stf_trend > self.config.trend_threshold
        )
        short_mask = (htf_trend < -self.config.trend_threshold) & (
            stf_trend < -self.config.trend_threshold
        )

        result = df.loc[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "trend_following"
        result["HTF_TREND"] = htf_trend[long_mask | short_mask].values
        result["STF_TREND"] = stf_trend[long_mask | short_mask].values

        result = self._add_confluence_and_direction(result)

        return result

    def _detect_mean_reversion(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect mean reversion: LTF oscillator extremes."""
        ltf_col = "Recommend Other|15"

        if ltf_col not in df.columns:
            return pd.DataFrame()

        osc_value = df[ltf_col].fillna(0)

        long_mask = osc_value < -self.config.mr_threshold
        short_mask = osc_value > self.config.mr_threshold

        result = df.loc[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "mean_reversion"
        result["LTF_MOMENTUM"] = osc_value[long_mask | short_mask].values
        result["MR_STRENGTH"] = result["LTF_MOMENTUM"].abs()
        result["DIRECTION"] = np.where(
            result["LTF_MOMENTUM"] < -self.config.mr_threshold, "long", "short"
        )
        result["CONFLUENCE_SCORE"] = 1
        result = result.sort_values("MR_STRENGTH", ascending=False)

        return result

    def _detect_hybrid(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect hybrid: HTF trend + LTF mean reversion."""
        htf_col = "Recommend All|240"
        ltf_col = "Recommend Other|15"

        if htf_col not in df.columns or ltf_col not in df.columns:
            return pd.DataFrame()

        htf_trend = df[htf_col].fillna(0)
        ltf_osc = df[ltf_col].fillna(0)

        long_mask = (htf_trend > self.config.trend_threshold) & (
            ltf_osc < -self.config.mr_threshold
        )
        short_mask = (htf_trend < -self.config.trend_threshold) & (
            ltf_osc > self.config.mr_threshold
        )

        result = df.loc[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "hybrid"
        result["HTF_TREND"] = htf_trend[long_mask | short_mask].values
        result["LTF_MOMENTUM"] = ltf_osc[long_mask | short_mask].values
        result["DIRECTION"] = np.where(result["HTF_TREND"] > 0, "long", "short")
        result["CONFLUENCE_SCORE"] = 2

        return result

    def _detect_breakout(self, df: pd.DataFrame) -> pd.DataFrame:
        """Detect breakout: Multi-TF momentum alignment."""
        roc_cols = [f"Roc|{tf}" for tf in self.timeframes]

        available_roc_cols = [c for c in roc_cols if c in df.columns]
        if not available_roc_cols:
            return pd.DataFrame()

        roc_values = df[available_roc_cols].fillna(0)

        if self.config.min_roc is not None:
            long_mask = (roc_values > self.config.min_roc).all(axis=1)
            short_mask = (roc_values < -self.config.min_roc).all(axis=1)
        else:
            long_mask = (roc_values > 0).all(axis=1)
            short_mask = (roc_values < 0).all(axis=1)

        result = df.loc[long_mask | short_mask].copy()

        if result.empty:
            return pd.DataFrame()

        result["STRATEGY"] = "breakout"

        for col in available_roc_cols:
            tf = col.split("|")[-1]
            result[f"ROC_{tf}"] = result[col]

        result["DIRECTION"] = np.where(result[available_roc_cols[0]] > 0, "long", "short")
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
            df["DIRECTION"] = np.where(htf > 0, "long", "short")

        return df

    def _apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply config filters to results."""
        if df.empty:
            return df

        if self.config.direction != "all":
            df = df[df["DIRECTION"] == self.config.direction].copy()

        if self.config.min_confluence > 0:
            df = df[df["CONFLUENCE_SCORE"] >= self.config.min_confluence].copy()

        return df

    def _get_results(self) -> pd.DataFrame:
        if self._cached_results is not None:
            return self._cached_results
        return self.scan(use_cache=True)

    def export(self, path: str, format_name: str, **kwargs) -> None:
        get_export_function(format_name)(
            self._get_results,
            path,
            **kwargs,
            logger=logger,
            label="signals",
        )

    def print_summary(self) -> None:
        def _render(df: pd.DataFrame, console, Table) -> None:
            for strategy in df["STRATEGY"].unique():
                strategy_df = df[df["STRATEGY"] == strategy]

                table = Table(title=f"Strategy: {strategy}")
                table.add_column("Pair", style="cyan")
                table.add_column("Direction", style="green")
                table.add_column("Confluence", justify="right")

                for _, row in strategy_df.iterrows():
                    table.add_row(
                        row.get("_base_pair", row.get("Name", row.get("PAIR", "N/A"))),
                        row["DIRECTION"],
                        str(row.get("CONFLUENCE_SCORE", "N/A")),
                    )

                console.print(table)

            console.print(f"\n[dim]Total signals: {len(df)}[/dim]")

        print_summary(
            self._get_results,
            empty_rich_message="No signals found",
            render_rich=_render,
        )
