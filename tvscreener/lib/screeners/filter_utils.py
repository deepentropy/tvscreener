from __future__ import annotations

from collections.abc import Sequence

import pandas as pd


def apply_volume_filter(df: pd.DataFrame, min_volume: float | None) -> pd.DataFrame:
    if min_volume is None or df.empty:
        return df

    vol_col = "Average Volume (10 day Calc)"
    if vol_col in df.columns:
        return df[df[vol_col] >= min_volume].copy()
    return df


def apply_atr_filter(df: pd.DataFrame, max_atr: float | None) -> pd.DataFrame:
    if max_atr is None or df.empty:
        return df

    atr_cols = [c for c in df.columns if c.startswith("ATR|")]
    if not atr_cols:
        return df

    df = df.copy()
    df["_atr_avg"] = df[atr_cols].mean(axis=1)
    result = df[df["_atr_avg"] <= max_atr].copy()
    return result.drop(columns=["_atr_avg"], errors="ignore")


def apply_ma_rating_filter(df: pd.DataFrame, min_ma_rating: float | None) -> pd.DataFrame:
    if min_ma_rating is None or df.empty:
        return df

    ma_cols = [c for c in df.columns if c.startswith("Recommend Ma|")]
    if not ma_cols:
        return df

    df = df.copy()
    df["_ma_avg"] = df[ma_cols].mean(axis=1)
    result = df[df["_ma_avg"] >= min_ma_rating].copy()
    return result.drop(columns=["_ma_avg"], errors="ignore")


def detect_mean_reversion_signals(df: pd.DataFrame, signals: Sequence[str]) -> pd.DataFrame:
    if not signals or df.empty:
        return df

    rsi_cols = [c for c in df.columns if c.startswith("RSI")]
    if not rsi_cols:
        return df

    df = df.copy()
    rsi_data = df[rsi_cols].fillna(50)

    if "rsi_oversold" in signals:
        df["rsi_oversold"] = (rsi_data < 30).any(axis=1).astype(int)
    if "rsi_overbought" in signals:
        df["rsi_overbought"] = (rsi_data > 70).any(axis=1).astype(int)

    return df
