from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from tvscreener.config.universe import AssetUniverse
from tvscreener.filter import RatingFilter, RocFilter, VolumeFilter
from tvscreener.score import ScoringConfig


@dataclass
class ScreenerConfig:
    """Universal screener configuration."""

    rating_filters: list[RatingFilter] = field(default_factory=list)
    roc_filter: RocFilter | None = None
    volume_filter: VolumeFilter | None = None
    preferred_exchanges: list[str] = field(default_factory=list)
    scoring_config: ScoringConfig | None = None


class BaseOpportunityScreener(ABC):
    """Abstract base for asset-agnostic opportunity screening.

    Subclasses implement the abstract methods to handle asset-specific
    data fetching and filtering.
    """

    def __init__(self, universe: AssetUniverse, config: ScreenerConfig):
        self.universe = universe
        self.config = config
        self._screener = None

    @abstractmethod
    def get_opportunities(self) -> pd.DataFrame:
        """Get filtered and ranked opportunities.

        Returns:
            DataFrame with scored and sorted opportunities
        """
        ...

    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        """Fetch raw market data for all pairs.

        Returns:
            DataFrame with raw market data
        """
        ...

    def apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply configured filters to data.

        Args:
            df: DataFrame to filter

        Returns:
            Filtered DataFrame
        """
        if df.empty:
            return df

        if self.config.volume_filter:
            df = self._apply_volume_filter(df, self.config.volume_filter)

        for rf in self.config.rating_filters:
            df = self._apply_rating_filter(df, rf)

        if self.config.roc_filter:
            df = self._apply_roc_filter(df, self.config.roc_filter)

        return df

    def rank_opportunities(self, df: pd.DataFrame) -> pd.DataFrame:
        """Rank opportunities by score.

        Override this in subclasses to customize scoring behavior.

        Args:
            df: DataFrame to rank

        Returns:
            DataFrame with score columns
        """
        from tvscreener.score import ScoringEngine, DEFAULT_SCORING_CONFIG

        engine = ScoringEngine(
            config=self.config.scoring_config or DEFAULT_SCORING_CONFIG,
            timeframes=self.universe.timeframes,
            tf_weights=self.universe.default_tf_weights,
        )
        return engine.rank_opportunities(df)

    def _apply_volume_filter(self, df: pd.DataFrame, vf: VolumeFilter) -> pd.DataFrame:
        """Apply volume filter."""
        if df.empty:
            return df

        volume_col = "Average Volume (10 day Calc)"
        if volume_col in df.columns and vf.min_volume is not None:
            return df[df[volume_col] >= vf.min_volume].copy()

        return df

    def _apply_rating_filter(self, df: pd.DataFrame, rf: RatingFilter) -> pd.DataFrame:
        """Apply rating filter."""
        rating_cols = {
            "all": f"Recommend All|{rf.threshold}",
            "ma": f"Recommend Ma|{rf.threshold}",
            "oscillator": f"Recommend Other|{rf.threshold}",
        }

        col = rating_cols[rf.rating_type]
        if col in df.columns:
            return df[df[col] >= rf.threshold].copy()
        return df

    def _apply_roc_filter(self, df: pd.DataFrame, roc: RocFilter) -> pd.DataFrame:
        """Apply ROC filter."""
        if df.empty:
            return df

        for tf in self.universe.timeframes:
            col = f"Roc|{tf}"
            if col in df.columns:
                if roc.min_roc is not None:
                    df = df[df[col] >= roc.min_roc].copy()
                if roc.max_roc is not None:
                    df = df[df[col] <= roc.max_roc].copy()

        return df

    def to_csv(self, path: str, include_index: bool = False) -> None:
        """Save opportunities to CSV."""
        df = self.get_opportunities()
        df.to_csv(path, index=include_index)

    def to_json(self, path: str, orient: str = "records") -> None:
        """Save opportunities to JSON."""
        df = self.get_opportunities()
        df.to_json(path, orient=orient, indent=2)

    def print_summary(self) -> None:
        """Print opportunities summary to console."""
        try:
            from rich.console import Console
            from rich.table import Table

            console = Console()
            df = self.get_opportunities()

            if df.empty:
                console.print("[yellow]No opportunities found[/yellow]")
                return

            table = Table(title="Opportunities")

            table.add_column("Symbol", style="cyan", no_wrap=True)
            table.add_column("Price", style="white", justify="right")
            table.add_column("Score", style="green", justify="right")

            for _, row in df.head(20).iterrows():
                name = row.get("Name", row.get("Symbol", "N/A"))
                price = row.get("Price", 0)
                score = row.get("RATING_SCORE", 0)

                table.add_row(
                    name,
                    f"{price:.5f}" if price else "N/A",
                    f"{score:.2f}" if score else "N/A",
                )

            console.print(table)
            console.print(f"\n[dim]Showing top 20 of {len(df)} opportunities[/dim]")

        except ImportError:
            df = self.get_opportunities()
            print(df.to_string())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"universe={self.universe.name}, "
            f"pairs={len(self.universe.pairs)})"
        )
