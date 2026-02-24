"""
Technical Analysis helpers for computing recommendations based on indicators.

This module provides functions to calculate buy/sell/neutral recommendations
for various technical indicators such as ADX, Awesome Oscillator, and Bollinger Bands.
"""

from tvscreener.field import Rating


def _crosses_up(x1, x2, y1, y2):
    """
    Check if x crossed above y.

    :param x1: Current x value
    :param x2: Previous x value
    :param y1: Current y value
    :param y2: Previous y value
    :return: True if x crossed above y
    """
    return x1 > y1 and x2 < y2


def adx(adx_value, dminus, dplus, dminus_old, dplus_old):
    """
    Calculate ADX (Average Directional Index) recommendation.

    :param adx_value: Current ADX value
    :param dminus: Current -DI value
    :param dplus: Current +DI value
    :param dminus_old: Previous -DI value
    :param dplus_old: Previous +DI value
    :return: Rating enum (BUY, SELL, or NEUTRAL)
    """
    if _crosses_up(dplus, dplus_old, dminus, dminus_old) and adx_value > 20:
        return Rating.BUY
    elif _crosses_up(dminus, dminus_old, dplus, dplus_old) and adx_value > 20:
        return Rating.SELL
    return Rating.NEUTRAL


def _is_ao_bearish_cross(ao_value, ao_old_1, ao_old_2):
    """
    Check for AO bearish zero line cross.

    When AO crosses below the Zero Line, short term momentum is now falling faster
    than the long term momentum. This can present a bearish selling opportunity.
    """
    return ao_value < 0 < ao_old_1 and ao_old_2 > 0


def _is_ao_bullish_cross(ao_value, ao_old_1, ao_old_2):
    """
    Check for AO bullish zero line cross.

    When AO crosses above the Zero Line, short term momentum is now rising faster
    than the long term momentum. This can present a bullish buying opportunity.
    """
    return ao_value > 0 > ao_old_1 and ao_old_2 < 0


def _is_ao_bullish_saucer(ao_value, ao_old_1, ao_old_2):
    """
    Check for AO bullish saucer setup.

    A Bullish Saucer setup occurs when the AO is above the Zero Line. It entails
    two consecutive red bars (with the second bar being lower than the first bar)
    being followed by a green Bar.
    """
    return ao_value > 0 and ao_value > ao_old_1 and ao_old_1 < ao_old_2


def _is_ao_bearish_saucer(ao_value, ao_old_1, ao_old_2):
    """
    Check for AO bearish saucer setup.

    A Bearish Saucer setup occurs when the AO is below the Zero Line. It entails
    two consecutive green bars (with the second bar being higher than the first bar)
    being followed by a red bar.
    """
    return ao_value < 0 and ao_value < ao_old_1 and ao_old_1 > ao_old_2


def ao(ao_value, ao_old_1, ao_old_2):
    """
    Calculate Awesome Oscillator recommendation.

    :param ao_value: Current AO value
    :param ao_old_1: Previous AO value (1 period back)
    :param ao_old_2: Previous AO value (2 periods back)
    :return: Rating enum (BUY, SELL, or NEUTRAL)
    """
    if _is_ao_bullish_saucer(ao_value, ao_old_1, ao_old_2) or _is_ao_bullish_cross(
        ao_value, ao_old_1, ao_old_2
    ):
        return Rating.BUY
    elif _is_ao_bearish_saucer(ao_value, ao_old_1, ao_old_2) or _is_ao_bearish_cross(
        ao_value, ao_old_1, ao_old_2
    ):
        return Rating.SELL
    return Rating.NEUTRAL


def bb_lower(low_limit, close):
    """
    Calculate Bollinger Bands lower band recommendation.

    :param low_limit: Lower Bollinger Band value
    :param close: Current close price
    :return: Rating enum (BUY or NEUTRAL)
    """
    if close < low_limit:
        return Rating.BUY
    return Rating.NEUTRAL


def bb_upper(up_limit, close):
    """
    Calculate Bollinger Bands upper band recommendation.

    :param up_limit: Upper Bollinger Band value
    :param close: Current close price
    :return: Rating enum (SELL or NEUTRAL)
    """
    if close > up_limit:
        return Rating.SELL
    return Rating.NEUTRAL
