from __future__ import annotations

import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import Literal

import pandas as pd

from tvscreener.constants.forex import (
    DEFAULT_FOREX_PAIRS,
    DEFAULT_TIMEFRAME_WEIGHTS,
    DEFAULT_TIMEFRAMES,
    EXCHANGE_PRIORITY,
    LIQUID_EXCHANGES,
)
from tvscreener.core.forex import ForexScreener
from tvscreener.exceptions import FilterConfigurationError, InvalidPairError
from tvscreener.field.forex import ForexField
from tvscreener.filter import RatingFilter, RocFilter, VolumeFilter
from tvscreener.lib.screeners.export_helpers import get_export_function, print_summary
from tvscreener.score import DEFAULT_SCORING_CONFIG, ScoringConfig, ScoringEngine

logger = logging.getLogger(__name__)

ContractType = Literal["spot", "cfd", "spreadbet", "all"]


@dataclass(frozen=True, slots=True)
class ForexScreenerConfig:
    rating_filters: tuple[RatingFilter, ...] = field(default_factory=tuple)
    roc_filter: RocFilter | None = None
    volume_filter: VolumeFilter | None = None
    preferred_exchanges: tuple[str, ...] = field(default_factory=lambda: tuple(LIQUID_EXCHANGES))
    contract_type: ContractType = "cfd"
    include_atr: bool = False
    include_rsi: bool = False
    scoring_config: ScoringConfig | None = None
    timeframe_weights: dict[str, float] = field(
        default_factory=lambda: dict(DEFAULT_TIMEFRAME_WEIGHTS)
    )


@dataclass
class ForexOpportunityScreener:
    pairs: list[str] = field(default_factory=lambda: DEFAULT_FOREX_PAIRS)
    timeframes: list[str] = field(default_factory=lambda: DEFAULT_TIMEFRAMES)
    config: ForexScreenerConfig = field(default_factory=ForexScreenerConfig)
    _cached_data: pd.DataFrame | None = field(init=False, default=None)

    def __post_init__(self) -> None:
        self._validate_pairs()
        self._validate_timeframes()
        self._engine = ScoringEngine(
            config=self.config.scoring_config or DEFAULT_SCORING_CONFIG,
            timeframes=self.timeframes,
            tf_weights=self.config.timeframe_weights,
        )

    def _validate_pairs(self) -> None:
        valid_pairs = DEFAULT_FOREX_PAIRS
        invalid = set(self.pairs) - set(valid_pairs)
        if invalid:
            raise InvalidPairError(f"Invalid forex pairs: {invalid}")

    def _validate_timeframes(self) -> None:
        valid_timeframes = DEFAULT_TIMEFRAMES
        invalid = set(self.timeframes) - set(valid_timeframes)
        if invalid:
            raise FilterConfigurationError(f"Invalid timeframes: {invalid}")

    def __repr__(self) -> str:
        return (
            f"ForexOpportunityScreener("
            f"pairs={len(self.pairs)}, "
            f"timeframes={self.timeframes}, "
            f"rating_filters={len(self.config.rating_filters)}, "
            f"roc_filter={self.config.roc_filter}, "
            f"volume_filter={self.config.volume_filter}, "
            f"contract_type={self.config.contract_type}, "
            f"preferred_exchanges={len(self.config.preferred_exchanges)})"
        )

    def get_opportunities(self, use_cache: bool = False) -> pd.DataFrame:
        if use_cache and self._cached_data is not None:
            logger.info("Returning cached data")
            return self._cached_data

        logger.info(f"Scanning {len(self.pairs)} pairs across {len(self.timeframes)} timeframes")

        all_data = []

        with ThreadPoolExecutor(max_workers=min(10, len(self.pairs))) as executor:
            futures = {executor.submit(self._fetch_pair_data, pair): pair for pair in self.pairs}

            for future in as_completed(futures):
                pair = futures[future]
                try:
                    pair_data = future.result()
                    if not pair_data.empty:
                        all_data.append(pair_data)
                except Exception as e:
                    logger.error(f"Error fetching {pair}: {e}")

        if not all_data:
            logger.warning("No data returned from API")
            return pd.DataFrame()

        df = pd.concat(all_data, ignore_index=True)

        df = self._apply_contract_type_filter(df)

        df = self._merge_duplicates(df)

        df = self._apply_rating_and_roc_filters(df)
        df = self._rank_opportunities(df)

        self._cached_data = df
        logger.info(f"Found {len(df)} opportunities")
        return df

    def _fetch_pair_data(self, pair: str) -> pd.DataFrame:
        fs = ForexScreener()
        fs.search(pair)

        select_fields = [
            ForexField.NAME,
            ForexField.PRICE,
            ForexField.AVERAGE_VOLUME_10D_CALC,
            ForexField.SUBTYPE,
        ]

        for tf in self.timeframes:
            select_fields.append(getattr(ForexField, f"RECOMMEND_ALL_{tf}"))
            select_fields.append(getattr(ForexField, f"RECOMMEND_MA_{tf}"))
            select_fields.append(getattr(ForexField, f"RECOMMEND_OTHER_{tf}"))
            select_fields.append(getattr(ForexField, f"ROC_{tf}"))

            if self.config.include_atr:
                select_fields.append(getattr(ForexField, f"ATR_{tf}"))
            if self.config.include_rsi:
                select_fields.append(getattr(ForexField, f"RSI_{tf}"))

        fs.select(*select_fields)

        try:
            df = fs.get()
            if df.empty:
                return pd.DataFrame()

            return df
        except Exception as e:
            logger.error(f"Error fetching {pair}: {e}")
            return pd.DataFrame()

    def _apply_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        return self._apply_rating_and_roc_filters(df)

    def _apply_rating_and_roc_filters(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        if self.config.volume_filter:
            df = self._apply_volume_filter(df, self.config.volume_filter)

        for rf in self.config.rating_filters:
            df = self._apply_rating_filter(df, rf)

        if self.config.roc_filter:
            df = self._apply_roc_filter(df, self.config.roc_filter)

        return df

    def _apply_contract_type_filter(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        contract_type = self.config.contract_type
        if contract_type == "all":
            return df

        subtype_col = "Subtype"
        if subtype_col in df.columns:
            if contract_type == "cfd":
                return df[df[subtype_col] == "cfd"].copy()
            elif contract_type == "spot":
                return df[df[subtype_col].isin(["", "spot"])].copy()
            elif contract_type == "spreadbet":
                return df[df[subtype_col] == "spreadbet"].copy()

        return df

    def _apply_volume_filter(self, df: pd.DataFrame, vf: VolumeFilter | None) -> pd.DataFrame:
        if df.empty:
            return df

        if vf is None:
            return df

        volume_col = "Average Volume (10 day Calc)"
        if volume_col in df.columns and vf.min_volume is not None:
            return df[df[volume_col] >= vf.min_volume].copy()

        return df

    def _merge_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        VALID_PAIRS = DEFAULT_FOREX_PAIRS
        VALID_PAIRS_SET = set(VALID_PAIRS)

        df = df.copy()

        # Vectorized extraction (hot path): keep behavior consistent with prior get_base_pair/get_exchange.
        names = (df["Name"] if "Name" in df.columns else pd.Series("", index=df.index)).fillna("")
        names = names.astype(str).str.upper()

        pairs_alt = "|".join(re.escape(p) for p in VALID_PAIRS)
        base_pair_match = names.str.extract(
            rf"^(?P<p1>{pairs_alt})(?=$|[._])|_(?P<p2>{pairs_alt})\.",
            expand=True,
        )
        base_pair = base_pair_match["p1"].fillna(base_pair_match["p2"])
        df["_base_pair"] = base_pair.fillna(names.where(names.str.len() < 6, names.str.slice(0, 6)))

        symbols = (
            df["Symbol"] if "Symbol" in df.columns else pd.Series("", index=df.index)
        ).fillna("")
        symbols = symbols.astype(str)
        has_exchange = symbols.str.contains(":", regex=False)
        df["_exchange"] = symbols.str.split(":", n=1).str[0].where(has_exchange, "")

        df["_is_canonical"] = names.isin(VALID_PAIRS_SET).astype(int)

        df["_exchange_score"] = df["_exchange"].map(EXCHANGE_PRIORITY).fillna(999).astype(int)

        df["_volume"] = df.get("Average Volume (10 day Calc)", pd.Series([0] * len(df))).fillna(0)

        df["_priority"] = list(
            zip(df["_is_canonical"], df["_exchange_score"], -df["_volume"], strict=False)
        )

        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(
            columns=[
                "_priority",
                "_exchange",
                "_is_canonical",
                "_exchange_score",
                "_volume",
            ],
            errors="ignore",
        )

        return df

    def _apply_rating_filter(self, df: pd.DataFrame, rf: RatingFilter) -> pd.DataFrame:
        if df.empty:
            return df

        rating_type_col = {
            "all": "Recommend All",
            "ma": "Recommend Ma",
            "oscillator": "Recommend Other",
        }

        col_prefix = rating_type_col.get(rf.rating_type)
        if not col_prefix:
            return df

        rating_cols = [c for c in df.columns if c.startswith(col_prefix + "|")]
        if not rating_cols:
            return df

        mask = df[rating_cols].fillna(-999) >= rf.threshold
        return df[mask.any(axis=1)].copy()

    def _apply_roc_filter(self, df: pd.DataFrame, roc: RocFilter) -> pd.DataFrame:
        if df.empty:
            return df

        for tf in self.timeframes:
            col = f"Roc|{tf}"
            if col in df.columns:
                if roc.min_roc is not None:
                    df = df[df[col] >= roc.min_roc].copy()
                if roc.max_roc is not None:
                    df = df[df[col] <= roc.max_roc].copy()

        return df

    def _rank_opportunities(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        df = self._engine.rank_opportunities(df)

        return df

    def _get_data(self) -> pd.DataFrame:
        if self._cached_data is not None:
            return self._cached_data
        return self.get_opportunities()

    def export(self, path: str, format_name: str, **kwargs) -> None:
        get_export_function(format_name)(
            self._get_data,
            path,
            **kwargs,
            logger=logger,
            label="opportunities",
        )

    def print_summary(self) -> None:
        def _render(df: pd.DataFrame, console, Table) -> None:
            table = Table(title="Forex Opportunities")
            table.add_column("Pair", style="cyan", no_wrap=True)
            table.add_column("Price", style="white", justify="right")
            table.add_column("Rating", style="green", justify="right")
            table.add_column("ROC %", style="yellow", justify="right")

            for _, row in df.head(20).iterrows():
                name = row.get("_base_pair", row.get("Name", "N/A"))
                price = row.get("Price", 0)
                rating = row.get("RATING_SCORE", 0)
                roc = row.get("ROC_AVG", 0)

                table.add_row(
                    name,
                    f"{price:.5f}" if price else "N/A",
                    f"{rating:.2f}",
                    f"{roc:.2f}%" if roc else "N/A",
                )

            console.print(table)
            console.print(f"\n[dim]Showing top 20 of {len(df)} opportunities[/dim]")

        print_summary(
            self._get_data,
            empty_rich_message="No opportunities found",
            render_rich=_render,
        )
