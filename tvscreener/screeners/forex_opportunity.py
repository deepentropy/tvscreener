from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal

import numpy as np
import pandas as pd

from tvscreener.core.forex import ForexScreener
from tvscreener.field.forex import ForexField

from tvscreener.constants.forex import (
    DEFAULT_FOREX_PAIRS,
    DEFAULT_TIMEFRAME_WEIGHTS,
    DEFAULT_TIMEFRAMES,
    EXCHANGE_PRIORITY,
    LIQUID_EXCHANGES,
    TIMEFRAME_LABELS,
)
from ..exceptions import (
    FilterConfigurationError,
    InvalidPairError,
)

logger = logging.getLogger(__name__)

RatingType = Literal["all", "ma", "oscillator"]
ContractType = Literal["spot", "cfd", "spreadbet", "all"]


@dataclass
class RatingFilter:
    rating_type: RatingType
    threshold: float


@dataclass
class RocFilter:
    min_roc: float | None = None
    max_roc: float | None = None


@dataclass
class VolumeFilter:
    min_volume: float | None = None


@dataclass
class ScoringConfig:
    trend_weight: float = 0.4
    ma_weight: float = 0.3
    osc_weight: float = 0.2
    roc_weight: float = 0.1


DEFAULT_SCORING_CONFIG = ScoringConfig()


@dataclass
class ForexScreenerConfig:
    rating_filters: list[RatingFilter] = field(default_factory=list)
    roc_filter: RocFilter | None = None
    volume_filter: VolumeFilter | None = None
    preferred_exchanges: list[str] = field(default_factory=lambda: LIQUID_EXCHANGES)
    contract_type: ContractType = "cfd"
    scoring_config: ScoringConfig | None = None


@dataclass
class ForexOpportunityScreener:
    pairs: list[str] = field(default_factory=lambda: DEFAULT_FOREX_PAIRS)
    timeframes: list[str] = field(default_factory=lambda: DEFAULT_TIMEFRAMES)
    config: ForexScreenerConfig = field(default_factory=ForexScreenerConfig)

    def __post_init__(self) -> None:
        self._validate_pairs()
        self._validate_timeframes()

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

    def get_opportunities(self) -> pd.DataFrame:
        logger.info(
            f"Scanning {len(self.pairs)} pairs across {len(self.timeframes)} timeframes"
        )

        all_data = []
        for pair in self.pairs:
            pair_data = self._fetch_pair_data(pair)
            if not pair_data.empty:
                all_data.append(pair_data)

        if not all_data:
            logger.warning("No data returned from API")
            return pd.DataFrame()

        df = pd.concat(all_data, ignore_index=True)

        df = self._apply_contract_type_filter(df)

        df = self._merge_duplicates(df)

        df = self._apply_rating_and_roc_filters(df)
        df = self._rank_opportunities(df)

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
            tf_label = TIMEFRAME_LABELS.get(tf, tf)
            select_fields.append(getattr(ForexField, f"RECOMMEND_ALL_{tf}"))
            select_fields.append(getattr(ForexField, f"RECOMMEND_MA_{tf}"))
            select_fields.append(getattr(ForexField, f"RECOMMEND_OTHER_{tf}"))
            select_fields.append(getattr(ForexField, f"ROC_{tf}"))

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
                return df[df[subtype_col] == ""].copy()
            elif contract_type == "spreadbet":
                return df[df[subtype_col] == "spreadbet"].copy()

        return df

    def _apply_volume_filter(self, df: pd.DataFrame, vf: VolumeFilter) -> pd.DataFrame:
        if df.empty:
            return df

        volume_col = "Average Volume (10 day Calc)"
        if volume_col in df.columns and vf.min_volume is not None:
            return df[df[volume_col] >= vf.min_volume].copy()

        return df

    def _merge_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df

        VALID_PAIRS = [
            "EURUSD",
            "GBPUSD",
            "USDJPY",
            "USDCHF",
            "USDCAD",
            "AUDUSD",
            "NZDUSD",
            "EURGBP",
            "EURJPY",
            "GBPJPY",
            "EURCHF",
            "AUDJPY",
            "EURCAD",
            "CADJPY",
            "CHFJPY",
            "NZDJPY",
            "GBPAUD",
            "EURAUD",
            "AUDNZD",
            "EURNZD",
            "GBPCAD",
            "AUDCAD",
            "GBPNZD",
            "EURNOK",
            "EURSEK",
        ]

        def get_exchange(symbol: str) -> str:
            if ":" in symbol:
                return symbol.split(":")[0]
            return ""

        def is_canonical(name: str) -> bool:
            name = name.upper()
            return name in VALID_PAIRS

        def get_base_pair(name: str) -> str:
            if not name:
                return ""
            name = name.upper()
            for pair in VALID_PAIRS:
                if (
                    name == pair
                    or name.startswith(pair + ".")
                    or name.startswith(pair + "_")
                    or "_" + pair + "." in name
                ):
                    return pair
            if len(name) >= 6:
                return name[:6]
            return name

        def get_priority(row) -> tuple:
            exchange = get_exchange(row["Symbol"])
            name = row["Name"]

            canonical_score = 0 if is_canonical(name) else 1
            exchange_score = EXCHANGE_PRIORITY.get(exchange, 999)
            volume = row.get("Average Volume (10 day Calc)", 0) or 0

            return (canonical_score, exchange_score, -volume)

        df = df.copy()
        df["_base_pair"] = df["Name"].apply(get_base_pair)
        df["_priority"] = df.apply(get_priority, axis=1)
        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(columns=["_base_pair", "_priority"], errors="ignore")

        return df

        def get_exchange(symbol: str) -> str:
            if ":" in symbol:
                return symbol.split(":")[0]
            return ""

        def get_base_pair(name: str) -> str:
            if not name:
                return ""
            name = name.upper()
            valid_pairs = [
                "EURUSD",
                "GBPUSD",
                "USDJPY",
                "USDCHF",
                "USDCAD",
                "AUDUSD",
                "NZDUSD",
                "EURGBP",
                "EURJPY",
                "GBPJPY",
                "EURCHF",
                "AUDJPY",
                "EURCAD",
                "CADJPY",
                "CHFJPY",
                "NZDJPY",
                "GBPAUD",
                "EURAUD",
                "AUDNZD",
                "EURNZD",
                "GBPCAD",
                "AUDCAD",
                "GBPNZD",
                "EURNOK",
                "EURSEK",
            ]
            for pair in valid_pairs:
                if name.startswith(pair):
                    return pair
            if len(name) >= 6:
                return name[:6]
            return name

        def get_priority(exchange: str) -> int:
            return EXCHANGE_PRIORITY.get(exchange, 999)

        df = df.copy()
        df["_exchange"] = df["Symbol"].apply(get_exchange)
        df["_base_pair"] = df["Name"].apply(get_base_pair)
        df["_priority"] = df["_exchange"].apply(get_priority)

        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(columns=["_exchange", "_base_pair", "_priority"])

        return df

        def get_exchange(symbol: str) -> str:
            if ":" in symbol:
                return symbol.split(":")[0]
            return ""

        def get_base_pair(name: str) -> str:
            if not name:
                return ""
            name = name.upper()
            valid_pairs = [
                "EURUSD",
                "GBPUSD",
                "USDJPY",
                "USDCHF",
                "USDCAD",
                "AUDUSD",
                "NZDUSD",
                "EURGBP",
                "EURJPY",
                "GBPJPY",
                "EURCHF",
                "AUDJPY",
                "EURCAD",
                "CADJPY",
                "CHFJPY",
                "NZDJPY",
                "GBPAUD",
                "EURAUD",
                "AUDNZD",
                "EURNZD",
                "GBPCAD",
                "AUDCAD",
                "GBPNZD",
                "EURNOK",
                "EURSEK",
            ]
            for pair in valid_pairs:
                if name.startswith(pair):
                    return pair
            return name[:6]

        def get_priority(exchange: str) -> int:
            return EXCHANGE_PRIORITY.get(exchange, 999)

        df = df.copy()
        df["_exchange"] = df["Symbol"].apply(get_exchange)
        df["_base_pair"] = df["Name"].apply(get_base_pair)
        df["_priority"] = df["_exchange"].apply(get_priority)

        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(columns=["_exchange", "_base_pair", "_priority"])

        return df

        def get_exchange(symbol: str) -> str:
            if ":" in symbol:
                return symbol.split(":")[0]
            return ""

        def get_base_pair(name: str) -> str:
            if not name:
                return ""
            name = name.upper()
            suffixes = [
                "_LMAX",
                "_W",
                "_I",
                "_P",
                ".ONE",
                ".PRO.OTMS",
                ".SML.ONE",
                ".1",
                ".10",
                ".100",
                ".1000",
            ]
            for suffix in suffixes:
                if name.endswith(suffix):
                    name = name[: -len(suffix)]
                    break
            suffixes_2 = [
                ".CMJ",
                ".CMT",
                ".CSM",
                ".CFJ",
                ".CJT",
                ".DBM",
                ".MINI",
                ".CFD",
                ".CSD",
                ".DUB",
            ]
            for suffix in suffixes_2:
                if name.endswith(suffix):
                    name = name[: -len(suffix)]
                    break
            return name

        def get_priority(exchange: str) -> int:
            return EXCHANGE_PRIORITY.get(exchange, 999)

        df = df.copy()
        df["_exchange"] = df["Symbol"].apply(get_exchange)
        df["_base_pair"] = df["Name"].apply(get_base_pair)
        df["_priority"] = df["_exchange"].apply(get_priority)

        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(columns=["_exchange", "_base_pair", "_priority"])

        return df

        def get_exchange(symbol: str) -> str:
            if ":" in symbol:
                return symbol.split(":")[0]
            return ""

        def get_base_pair(name: str) -> str:
            if not name:
                return ""
            name = name.upper()
            for suffix in ["_LMAX", "_W", ".1", ".10"]:
                if name.endswith(suffix):
                    name = name[: -len(suffix)]
            return name

        def get_priority(exchange: str) -> int:
            return EXCHANGE_PRIORITY.get(exchange, 999)

        df = df.copy()
        df["_exchange"] = df["Symbol"].apply(get_exchange)
        df["_base_pair"] = df["Name"].apply(get_base_pair)
        df["_priority"] = df["_exchange"].apply(get_priority)

        df = df.sort_values(by="_priority")
        df = df.drop_duplicates(subset=["_base_pair"], keep="first")

        df = df.drop(columns=["_exchange", "_base_pair", "_priority"])

        return df

    def _apply_rating_filter(self, df: pd.DataFrame, rf: RatingFilter) -> pd.DataFrame:
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

        scoring_config = self.config.scoring_config or DEFAULT_SCORING_CONFIG
        tf_weights = DEFAULT_TIMEFRAME_WEIGHTS

        factor_cols = [
            ("TREND", "Recommend All|"),
            ("MA", "Recommend Ma|"),
            ("OSC", "Recommend Other|"),
        ]

        for factor_name, col_pattern in factor_cols:
            cols = [c for c in df.columns if col_pattern in c]
            if cols:
                weights = np.array(
                    [tf_weights.get(c.split("|")[-1], 0.33) for c in cols]
                )
                values = df[cols].fillna(0).values
                df[f"{factor_name}_SCORE"] = (values * weights).sum(
                    axis=1
                ) / weights.sum()
            else:
                df[f"{factor_name}_SCORE"] = 0.0

        roc_cols = [f"Roc|{tf}" for tf in self.timeframes if f"Roc|{tf}" in df.columns]
        if roc_cols:
            df["ROC_SCORE"] = df[roc_cols].mean(axis=1)
        else:
            df["ROC_SCORE"] = 0.0

        df["ENSEMBLE_SCORE"] = (
            df["TREND_SCORE"].fillna(0) * scoring_config.trend_weight
            + df["MA_SCORE"].fillna(0) * scoring_config.ma_weight
            + df["OSC_SCORE"].fillna(0) * scoring_config.osc_weight
            + df["ROC_SCORE"].fillna(0) * scoring_config.roc_weight
        )

        df["DIRECTION"] = df["ENSEMBLE_SCORE"].apply(
            lambda x: "long" if x > 0 else "short"
        )

        df["RATING_SCORE"] = df.get("ENSEMBLE_SCORE", 0.0)
        df["ROC_AVG"] = df.get("ROC_SCORE", 0.0)

        df = df.sort_values(by=["ENSEMBLE_SCORE"], ascending=[False])

        return df

    def to_csv(self, path: str, include_index: bool = False) -> None:
        df = self.get_opportunities()
        df.to_csv(path, index=include_index)
        logger.info(f"Saved {len(df)} opportunities to {path}")

    def to_json(self, path: str, orient: str = "records") -> None:
        df = self.get_opportunities()
        df.to_json(path, orient=orient, indent=2)
        logger.info(f"Saved {len(df)} opportunities to {path}")

    def print_summary(self) -> None:
        try:
            from rich.console import Console
            from rich.table import Table

            console = Console()
            df = self.get_opportunities()

            if df.empty:
                console.print("[yellow]No opportunities found[/yellow]")
                return

            table = Table(title="Forex Opportunities")

            table.add_column("Pair", style="cyan", no_wrap=True)
            table.add_column("Price", style="white", justify="right")
            table.add_column("Rating", style="green", justify="right")
            table.add_column("ROC %", style="yellow", justify="right")

            for _, row in df.head(20).iterrows():
                name = row.get("Name", "N/A")
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

        except ImportError:
            df = self.get_opportunities()
            print(df.to_string())
