"""
Beautification module for styling TradingView screener data.

This module provides styling functionality to reproduce TradingView's visual style
with colored ratings and formatted values.

Key visual elements:
- Rating columns with colored text and directional arrows
- Percent change columns with green/red coloring
- Number formatting with K, M, B suffixes
- Missing values displayed as "--"
"""

from typing import Type

import pandas as pd

from tvscreener.field import Field, Rating
from tvscreener.util import millify, _is_nan
import tvscreener.ta as ta

# Visual indicators for ratings
BUY_CHAR = "↑ B"
SELL_CHAR = "↓ S"
NEUTRAL_CHAR = "- N"

# TradingView color scheme
COLOR_RED_NEGATIVE = "color:rgb(255, 23, 62);"
COLOR_GREEN_POSITIVE = "color:rgb(0, 169, 127);"
COLOR_BLUE_BUY = "color:rgb(41, 98, 255);"
COLOR_RED_SELL = "color:rgb(255, 74, 104);"
COLOR_GRAY_NEUTRAL = "color:rgb(157, 178, 189);"


def beautify(df, specific_fields: Type[Field]):
    """
    Apply TradingView-style formatting to a screener DataFrame.

    This function transforms raw screener data into a styled representation
    matching TradingView's visual design with colored ratings, formatted
    percentages, and abbreviated numbers.

    :param df: ScreenerDataFrame with raw data
    :param specific_fields: Field enum class (StockField, ForexField, CryptoField)
    :return: pandas Styler object with TradingView styling applied

    Example usage:
        >>> screener = StockScreener()
        >>> df = screener.get()
        >>> styled = beautify(df, StockField)
        >>> styled  # Display styled output in Jupyter
    """
    beautifier = Beautify(df, specific_fields)
    return beautifier.styled_df


def _get_recommendation(rating):
    """Convert numeric rating to Rating enum."""
    if rating < 0:
        return Rating.SELL
    elif rating == 0:
        return Rating.NEUTRAL
    return Rating.BUY


def _percent_colors(value):
    """Return color style based on positive/negative percentage value."""
    if isinstance(value, str) and value.startswith("-"):
        return COLOR_RED_NEGATIVE
    return COLOR_GREEN_POSITIVE


def _rating_colors(value):
    """Return color style based on rating indicator."""
    if not isinstance(value, str):
        return COLOR_GRAY_NEUTRAL
    if value.endswith(BUY_CHAR):
        return COLOR_BLUE_BUY
    elif value.endswith(SELL_CHAR):
        return COLOR_RED_SELL
    return COLOR_GRAY_NEUTRAL


def _rating_letter(rating: Rating):
    """Convert Rating enum to visual indicator string."""
    if rating == Rating.BUY or rating == Rating.STRONG_BUY:
        return BUY_CHAR
    elif rating == Rating.SELL or rating == Rating.STRONG_SELL:
        return SELL_CHAR
    return NEUTRAL_CHAR


class Beautify:
    """
    Handles the beautification of screener DataFrames with TradingView styling.

    This class applies formatting and coloring to different column types based
    on their field definitions.
    """

    def __init__(self, df, specific_fields: Type[Field]):
        """
        Initialize the beautifier with a DataFrame and field definitions.

        :param df: ScreenerDataFrame with raw data
        :param specific_fields: Field enum class (StockField, ForexField, CryptoField)
        """
        # Create a copy and set technical column names
        if hasattr(df, 'set_technical_columns'):
            df.set_technical_columns(only=True)
        self.df = df.copy()
        self.styled_df = self.df.style

        for field in specific_fields:
            if field.field_name in self.df.columns:
                self._format_column(field)

    def _format_column(self, field: Field):
        """Apply appropriate formatting based on field format type."""
        fmt = field.format
        if fmt == 'bool':
            self._to_bool(field)
        elif fmt == 'rating':
            self._rating(field)
        elif fmt == 'round':
            self._round(field)
        elif fmt == 'percent':
            self._percent(field)
        elif field.has_recommendation():
            self._recommendation(field)
        elif fmt == 'computed_recommendation':
            self._computed_recommendation(field)
        elif fmt == 'currency':
            self._round(field)
            self._number_group(field)
        elif fmt == 'number_group':
            self._replace_nan(field)
            self._number_group(field)

    def _rating(self, field: Field):
        """Format rating column with label text."""
        self.df[field.field_name] = self.df[field.field_name].apply(
            lambda x: Rating.find(x).label
        )

    def _recommendation(self, field: Field):
        """Format recommendation column with value and colored rating indicator."""
        rec_field = field.get_rec_field()
        self.df[field.field_name] = self.df.apply(
            lambda x: f"{x[field.field_name]} {_rating_letter(_get_recommendation(x[rec_field]))}"
            if not _is_nan(x[field.field_name]) else "--",
            axis=1
        )
        # Use map instead of deprecated applymap
        self.styled_df = self.styled_df.map(
            _rating_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

    def _number_group(self, field: Field):
        """Format number with K/M/B/T suffixes."""
        self.df[field.field_name] = self.df[field.field_name].apply(
            lambda x: millify(x) if x != "--" and not _is_nan(x) else "--"
        )

    def _percent(self, field: Field):
        """Format percentage column with coloring."""
        self.df[field.field_name] = self.df[field.field_name].apply(
            lambda x: f"{x:.2f}%" if not _is_nan(x) else "--"
        )
        # Use map instead of deprecated applymap
        self.styled_df = self.styled_df.map(
            _percent_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

    def _round(self, field: Field):
        """Round numeric values to 2 decimal places."""
        self.df[field.field_name] = self.df[field.field_name].apply(
            lambda x: round(x, 2) if not _is_nan(x) else "--"
        )

    def _replace_nan(self, field: Field):
        """Replace NaN values with 0."""
        self.df[field.field_name] = self.df[field.field_name].fillna(0)

    def _to_bool(self, field: Field):
        """Convert string boolean to Python boolean."""
        self.df[field.field_name] = self.df[field.field_name].apply(
            lambda x: x == 'true'
        ).astype(bool)

    def _computed_recommendation(self, field: Field):
        """Format computed recommendation columns (ADX, AO, Bollinger Bands)."""
        field_name = field.field_name

        if field_name == "ADX":
            self._format_adx(field)
        elif field_name == "AO":
            self._format_ao(field)
        elif field_name == "BB.lower":
            self._format_bb_lower(field)
        elif field_name == "BB.upper":
            self._format_bb_upper(field)

    def _format_adx(self, field: Field):
        """Format ADX column with recommendation."""
        required_cols = ['ADX', 'ADX-DI', 'ADX+DI', 'ADX-DI[1]', 'ADX+DI[1]']
        self.df[field.field_name] = self.df.apply(
            lambda x: f"{x[field.field_name]} {_rating_letter(ta.adx(x['ADX'], x['ADX-DI'], x['ADX+DI'], x['ADX-DI[1]'], x['ADX+DI[1]']))}"
            if all(col in x.index for col in required_cols) and not _is_nan(x[field.field_name])
            else str(x[field.field_name]) if not _is_nan(x[field.field_name]) else "--",
            axis=1
        )
        self.styled_df = self.styled_df.map(
            _rating_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

    def _format_ao(self, field: Field):
        """Format Awesome Oscillator column with recommendation."""
        required_cols = ['AO', 'AO[1]', 'AO[2]']
        self.df[field.field_name] = self.df.apply(
            lambda x: f"{x[field.field_name]} {_rating_letter(ta.ao(x['AO'], x['AO[1]'], x['AO[2]']))}"
            if all(col in x.index for col in required_cols) and not _is_nan(x[field.field_name])
            else str(x[field.field_name]) if not _is_nan(x[field.field_name]) else "--",
            axis=1
        )
        self.styled_df = self.styled_df.map(
            _rating_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

    def _format_bb_lower(self, field: Field):
        """Format Bollinger Bands lower band column with recommendation."""
        self.df[field.field_name] = self.df.apply(
            lambda x: f"{x[field.field_name]} {_rating_letter(ta.bb_lower(x[field.field_name], x['close']))}"
            if 'close' in x.index and not _is_nan(x[field.field_name]) and not _is_nan(x['close'])
            else str(x[field.field_name]) if not _is_nan(x[field.field_name]) else "--",
            axis=1
        )
        self.styled_df = self.styled_df.map(
            _rating_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

    def _format_bb_upper(self, field: Field):
        """Format Bollinger Bands upper band column with recommendation."""
        self.df[field.field_name] = self.df.apply(
            lambda x: f"{x[field.field_name]} {_rating_letter(ta.bb_upper(x[field.field_name], x['close']))}"
            if 'close' in x.index and not _is_nan(x[field.field_name]) and not _is_nan(x['close'])
            else str(x[field.field_name]) if not _is_nan(x[field.field_name]) else "--",
            axis=1
        )
        self.styled_df = self.styled_df.map(
            _rating_colors, subset=pd.IndexSlice[:, [field.field_name]]
        )

