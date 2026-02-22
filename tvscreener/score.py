from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True, slots=True)
class ScoringConfig:
    """Configuration for scoring weights."""

    trend_weight: float = 0.4
    ma_weight: float = 0.3
    osc_weight: float = 0.2
    roc_weight: float = 0.1


DEFAULT_SCORING_CONFIG = ScoringConfig()


class ScoringEngine:
    """Memory-efficient scoring engine for opportunity screening.

    Provides public methods for calculating factor scores, ensemble scores,
    confluence levels, and trade directions.
    """

    __slots__ = ("config", "timeframes", "tf_weights")

    def __init__(
        self,
        config: ScoringConfig | None = None,
        timeframes: list[str] | None = None,
        tf_weights: dict[str, float] | None = None,
    ):
        self.config = config or DEFAULT_SCORING_CONFIG
        self.timeframes = timeframes or []
        self.tf_weights = tf_weights or {}

    def calculate_factor_scores(
        self,
        df: pd.DataFrame,
        factor_name: str,
        col_pattern: str,
        copy: bool = True,
    ) -> pd.DataFrame:
        """Calculate weighted factor scores across timeframes.

        Args:
            df: DataFrame with timeframe columns matching col_pattern
            factor_name: Name for the output score column (e.g., "TREND")
            col_pattern: Column pattern to match (e.g., "Recommend All|")
            copy: If True, copy DataFrame to avoid mutation (default True)

        Returns:
            DataFrame with added factor score column
        """
        if copy:
            df = df.copy()

        cols = [c for c in df.columns if col_pattern in c]
        if cols:
            weights = np.array([self.tf_weights.get(c.split("|")[-1], 0.33) for c in cols])
            weight_sum = weights.sum()
            if weight_sum == 0:
                df[f"{factor_name}_SCORE"] = 0.0
            else:
                values = df[cols].fillna(0).values
                df[f"{factor_name}_SCORE"] = (values * weights).sum(axis=1) / weight_sum
        else:
            df[f"{factor_name}_SCORE"] = 0.0

        return df

    def calculate_roc_score(self, df: pd.DataFrame, copy: bool = True) -> pd.DataFrame:
        """Calculate momentum (ROC) score across timeframes.

        Args:
            df: DataFrame with ROC columns
            copy: If True, copy DataFrame to avoid mutation

        Returns:
            DataFrame with added ROC_SCORE column
        """
        if copy:
            df = df.copy()

        roc_cols = [f"Roc|{tf}" for tf in self.timeframes if f"Roc|{tf}" in df.columns]
        if roc_cols:
            df["ROC_SCORE"] = df[roc_cols].mean(axis=1)
        else:
            df["ROC_SCORE"] = 0.0

        return df

    def calculate_ensemble_score(self, df: pd.DataFrame, copy: bool = True) -> pd.DataFrame:
        """Combine all factor scores into ensemble score using weights.

        Args:
            df: DataFrame with factor score columns
            copy: If True, copy DataFrame to avoid mutation

        Returns:
            DataFrame with added ENSEMBLE_SCORE and DIRECTION columns
        """
        if copy:
            df = df.copy()

        cfg = self.config
        df["ENSEMBLE_SCORE"] = (
            df["TREND_SCORE"].fillna(0) * cfg.trend_weight
            + df["MA_SCORE"].fillna(0) * cfg.ma_weight
            + df["OSC_SCORE"].fillna(0) * cfg.osc_weight
            + df["ROC_SCORE"].fillna(0) * cfg.roc_weight
        )

        df["DIRECTION"] = np.where(df["ENSEMBLE_SCORE"] > 0, "long", "short")

        return df

    def calculate_confluence(self, df: pd.DataFrame, copy: bool = True) -> pd.DataFrame:
        """Calculate timeframe confluence levels.

        Args:
            df: DataFrame with Recommend All columns per timeframe
            copy: If True, copy DataFrame to avoid mutation

        Returns:
            DataFrame with TF confluence columns and CONFLUENCE_LEVEL
        """
        if copy:
            df = df.copy()

        for tf in self.timeframes:
            col = f"Recommend All|{tf}"
            if col in df.columns:
                df[f"TF_{tf}_DIR"] = self.calculate_direction(df[col])

        tf_cols = [
            f"Recommend All|{tf}" for tf in self.timeframes if f"Recommend All|{tf}" in df.columns
        ]
        if tf_cols:
            tf_values = df[tf_cols].fillna(0)
            df["TF_CONFLUENCE_LONG"] = (tf_values > 0).sum(axis=1)
            df["TF_CONFLUENCE_SHORT"] = (tf_values < 0).sum(axis=1)
        else:
            df["TF_CONFLUENCE_LONG"] = 0
            df["TF_CONFLUENCE_SHORT"] = 0

        for factor in ["TREND", "MA", "OSC", "ROC"]:
            col = f"{factor}_SCORE"
            if col in df.columns:
                df[f"{factor}_DIR"] = self.calculate_direction(df[col])

        factor_dir_cols = [
            f"{factor}_DIR"
            for factor in ["TREND", "MA", "OSC", "ROC"]
            if f"{factor}_DIR" in df.columns
        ]
        if factor_dir_cols:
            df["FACTOR_BULLISH_COUNT"] = (df[factor_dir_cols] == "bullish").sum(axis=1)
            df["FACTOR_BEARISH_COUNT"] = (df[factor_dir_cols] == "bearish").sum(axis=1)
        else:
            df["FACTOR_BULLISH_COUNT"] = 0
            df["FACTOR_BEARISH_COUNT"] = 0

        if "DIRECTION" not in df.columns:
            df["DIRECTION"] = np.where(df.get("ENSEMBLE_SCORE", 0) > 0, "long", "short")

        df["TOTAL_CONFLUENCE"] = np.where(
            df["DIRECTION"] == "long",
            df["TF_CONFLUENCE_LONG"] + df["FACTOR_BULLISH_COUNT"],
            df["TF_CONFLUENCE_SHORT"] + df["FACTOR_BEARISH_COUNT"],
        )

        df["CONFLUENCE_LEVEL"] = np.select(
            [
                df["TOTAL_CONFLUENCE"] >= 5,
                df["TOTAL_CONFLUENCE"] >= 3,
                df["TOTAL_CONFLUENCE"] >= 1,
            ],
            ["strong", "medium", "weak"],
            default="none",
        )

        return df

    def calculate_direction(self, series: pd.Series) -> pd.Series:
        """Calculate direction (bullish/bearish/neutral) from values.

        Args:
            series: Series of numeric values

        Returns:
            Series with direction labels
        """
        return pd.Series(
            np.where(series > 0, "bullish", np.where(series < 0, "bearish", "neutral")),
            index=series.index,
        )

    def rank_opportunities(self, df: pd.DataFrame) -> pd.DataFrame:
        """Full ranking pipeline: scores, ensemble, confluence, sorting.

        Args:
            df: DataFrame with raw opportunity data

        Returns:
            DataFrame with all scoring columns, sorted by ensemble score
        """
        if df.empty:
            return df

        df = df.copy()

        df = self.calculate_factor_scores(df, "TREND", "Recommend All|", copy=False)
        df = self.calculate_factor_scores(df, "MA", "Recommend Ma|", copy=False)
        df = self.calculate_factor_scores(df, "OSC", "Recommend Other|", copy=False)

        df = self.calculate_roc_score(df, copy=False)

        df = self.calculate_ensemble_score(df, copy=False)

        df = self.calculate_confluence(df, copy=False)

        df["RATING_SCORE"] = df.get("ENSEMBLE_SCORE", 0.0)
        df["ROC_AVG"] = df.get("ROC_SCORE", 0.0)

        df = df.sort_values(by=["ENSEMBLE_SCORE"], ascending=[False])

        return df
