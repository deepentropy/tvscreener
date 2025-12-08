"""
Field presets for common use cases.

These presets provide curated lists of fields for specific analysis needs.
"""

from tvscreener.field.stock import StockField
from tvscreener.field.crypto import CryptoField
from tvscreener.field.forex import ForexField
from tvscreener.field.bond import BondField
from tvscreener.field.futures import FuturesField
from tvscreener.field.coin import CoinField


# =============================================================================
# STOCK FIELD PRESETS
# =============================================================================

# Basic price and change data
STOCK_PRICE_FIELDS = [
    StockField.NAME,
    StockField.DESCRIPTION,
    StockField.PRICE,
    StockField.CHANGE,
    StockField.CHANGE_PERCENT,
    StockField.HIGH,
    StockField.LOW,
    StockField.OPEN,
    StockField.PREMARKET_CHANGE,
    StockField.POSTMARKET_CHANGE,
]

# Volume metrics
STOCK_VOLUME_FIELDS = [
    StockField.NAME,
    StockField.VOLUME,
    StockField.AVERAGE_VOLUME_10_DAY,
    StockField.AVERAGE_VOLUME_30_DAY,
    StockField.AVERAGE_VOLUME_60_DAY,
    StockField.AVERAGE_VOLUME_90_DAY,
    StockField.RELATIVE_VOLUME,
]

# Market cap and valuation ratios
STOCK_VALUATION_FIELDS = [
    StockField.NAME,
    StockField.MARKET_CAPITALIZATION,
    StockField.PRICE_TO_EARNINGS_RATIO_TTM,
    StockField.PRICE_TO_BOOK_MRQ,
    StockField.PRICE_TO_SALES_FY,
    StockField.ENTERPRISE_VALUEEBITDA_TTM,
    StockField.ENTERPRISE_VALUE_MRQ,
]

# Dividend-related fields
STOCK_DIVIDEND_FIELDS = [
    StockField.NAME,
    StockField.DIVIDENDS_YIELD,
    StockField.DIVIDENDS_YIELD_CURRENT,
    StockField.DIVIDEND_YIELD_FORWARD,
    StockField.DIVIDEND_PAYOUT_RATIO_TTM,
    StockField.CONTINUOUS_DIVIDEND_GROWTH,
    StockField.CONTINUOUS_DIVIDEND_PAYOUT,
]

# Profitability ratios
STOCK_PROFITABILITY_FIELDS = [
    StockField.NAME,
    StockField.GROSS_MARGIN_TTM,
    StockField.OPERATING_MARGIN_TTM,
    StockField.NET_MARGIN_TTM,
    StockField.RETURN_ON_EQUITY_TTM,
    StockField.RETURN_ON_ASSETS_TTM,
    StockField.RETURN_ON_INVESTED_CAPITAL_TTM,
]

# Performance over time
STOCK_PERFORMANCE_FIELDS = [
    StockField.NAME,
    StockField.WEEKLY_PERFORMANCE,
    StockField.MONTHLY_PERFORMANCE,
    StockField.MONTH_PERFORMANCE_3,
    StockField.MONTH_PERFORMANCE_6,
    StockField.YTD_PERFORMANCE,
    StockField.YEARLY_PERFORMANCE,
]

# Technical indicators - oscillators
STOCK_OSCILLATOR_FIELDS = [
    StockField.NAME,
    StockField.RELATIVE_STRENGTH_INDEX_14,
    StockField.STOCHASTIC_PERCENTK_14_3_3,
    StockField.STOCHASTIC_PERCENTD_14_3_3,
    StockField.COMMODITY_CHANNEL_INDEX_20,
    StockField.AVERAGE_DIRECTIONAL_INDEX_14,
    StockField.AWESOME_OSCILLATOR,
    StockField.MOMENTUM_10,
    StockField.MACD_LEVEL_12_26,
    StockField.MACD_SIGNAL_12_26,
]

# Moving averages
STOCK_MOVING_AVERAGE_FIELDS = [
    StockField.NAME,
    StockField.SIMPLE_MOVING_AVERAGE_10,
    StockField.SIMPLE_MOVING_AVERAGE_20,
    StockField.SIMPLE_MOVING_AVERAGE_50,
    StockField.SIMPLE_MOVING_AVERAGE_100,
    StockField.SIMPLE_MOVING_AVERAGE_200,
    StockField.EXPONENTIAL_MOVING_AVERAGE_10,
    StockField.EXPONENTIAL_MOVING_AVERAGE_20,
    StockField.EXPONENTIAL_MOVING_AVERAGE_50,
    StockField.EXPONENTIAL_MOVING_AVERAGE_200,
]

# Earnings and EPS
STOCK_EARNINGS_FIELDS = [
    StockField.NAME,
    StockField.BASIC_EPS_TTM,
    StockField.EPS_DILUTED_TTM,
    StockField.EARNINGS_PER_SHARE_BASIC_TTM,
    StockField.NET_INCOME_FY,
    StockField.GROSS_PROFIT_FY,
]


# =============================================================================
# CRYPTO FIELD PRESETS
# =============================================================================

CRYPTO_PRICE_FIELDS = [
    CryptoField.NAME,
    CryptoField.DESCRIPTION,
    CryptoField.CHANGE,
    CryptoField.CHANGE_PERCENT,
    CryptoField.HIGH,
    CryptoField.LOW,
    CryptoField.OPEN,
]

CRYPTO_VOLUME_FIELDS = [
    CryptoField.NAME,
    CryptoField.VOLUME,
    CryptoField.VOLUME_24H_IN_USD,
    CryptoField.RELATIVE_VOLUME,
]

CRYPTO_PERFORMANCE_FIELDS = [
    CryptoField.NAME,
    CryptoField.WEEKLY_PERFORMANCE,
    CryptoField.MONTHLY_PERFORMANCE,
    CryptoField.MONTH_PERFORMANCE_3,
    CryptoField.MONTH_PERFORMANCE_6,
    CryptoField.YEARLY_PERFORMANCE,
]

CRYPTO_TECHNICAL_FIELDS = [
    CryptoField.NAME,
    CryptoField.RELATIVE_STRENGTH_INDEX_14,
    CryptoField.STOCHASTIC_PERCENTK_14_3_3,
    CryptoField.STOCHASTIC_PERCENTD_14_3_3,
    CryptoField.MACD_LEVEL_12_26,
    CryptoField.MACD_SIGNAL_12_26,
]


# =============================================================================
# FOREX FIELD PRESETS
# =============================================================================

FOREX_PRICE_FIELDS = [
    ForexField.NAME,
    ForexField.DESCRIPTION,
    ForexField.CHANGE,
    ForexField.CHANGE_PERCENT,
    ForexField.HIGH,
    ForexField.LOW,
    ForexField.OPEN,
]

FOREX_PERFORMANCE_FIELDS = [
    ForexField.NAME,
    ForexField.WEEKLY_PERFORMANCE,
    ForexField.MONTHLY_PERFORMANCE,
    ForexField.MONTH_PERFORMANCE_3,
    ForexField.MONTH_PERFORMANCE_6,
    ForexField.YEARLY_PERFORMANCE,
]

FOREX_TECHNICAL_FIELDS = [
    ForexField.NAME,
    ForexField.RELATIVE_STRENGTH_INDEX_14,
    ForexField.STOCHASTIC_PERCENTK_14_3_3,
    ForexField.STOCHASTIC_PERCENTD_14_3_3,
    ForexField.MACD_LEVEL_12_26,
    ForexField.MACD_SIGNAL_12_26,
]


# =============================================================================
# BOND FIELD PRESETS
# =============================================================================

BOND_BASIC_FIELDS = [
    BondField.NAME,
    BondField.CLOSE,
    BondField.CHANGE,
    BondField.VOLUME,
]

BOND_YIELD_FIELDS = [
    BondField.NAME,
    BondField.COUPON,
    BondField.CURRENT_YIELD,
    BondField.YIELD_TO_MATURITY,
]

BOND_MATURITY_FIELDS = [
    BondField.NAME,
    BondField.MATURITY_DATE,
    BondField.DAYS_TO_MATURITY,
    BondField.COUPON_FREQUENCY,
]


# =============================================================================
# FUTURES FIELD PRESETS
# =============================================================================

FUTURES_PRICE_FIELDS = [
    FuturesField.NAME,
    FuturesField.CLOSE,
    FuturesField.CHANGE,
    FuturesField.HIGH,
    FuturesField.LOW,
    FuturesField.VOLUME,
]

FUTURES_TECHNICAL_FIELDS = [
    FuturesField.NAME,
    FuturesField.RSI,
    FuturesField.MACD_MACD,
    FuturesField.MACD_SIGNAL,
    FuturesField.ADX,
]


# =============================================================================
# COIN FIELD PRESETS
# =============================================================================

COIN_PRICE_FIELDS = [
    CoinField.NAME,
    CoinField.CLOSE,
    CoinField.CHANGE,
    CoinField.HIGH,
    CoinField.LOW,
]

COIN_MARKET_FIELDS = [
    CoinField.NAME,
    CoinField.MARKET_CAP,
    CoinField.VOLUME,
]


# =============================================================================
# ALL PRESETS DICTIONARY
# =============================================================================

ALL_PRESETS = {
    # Stock
    'stock_price': STOCK_PRICE_FIELDS,
    'stock_volume': STOCK_VOLUME_FIELDS,
    'stock_valuation': STOCK_VALUATION_FIELDS,
    'stock_dividend': STOCK_DIVIDEND_FIELDS,
    'stock_profitability': STOCK_PROFITABILITY_FIELDS,
    'stock_performance': STOCK_PERFORMANCE_FIELDS,
    'stock_oscillators': STOCK_OSCILLATOR_FIELDS,
    'stock_moving_averages': STOCK_MOVING_AVERAGE_FIELDS,
    'stock_earnings': STOCK_EARNINGS_FIELDS,
    # Crypto
    'crypto_price': CRYPTO_PRICE_FIELDS,
    'crypto_volume': CRYPTO_VOLUME_FIELDS,
    'crypto_performance': CRYPTO_PERFORMANCE_FIELDS,
    'crypto_technical': CRYPTO_TECHNICAL_FIELDS,
    # Forex
    'forex_price': FOREX_PRICE_FIELDS,
    'forex_performance': FOREX_PERFORMANCE_FIELDS,
    'forex_technical': FOREX_TECHNICAL_FIELDS,
    # Bond
    'bond_basic': BOND_BASIC_FIELDS,
    'bond_yield': BOND_YIELD_FIELDS,
    'bond_maturity': BOND_MATURITY_FIELDS,
    # Futures
    'futures_price': FUTURES_PRICE_FIELDS,
    'futures_technical': FUTURES_TECHNICAL_FIELDS,
    # Coin
    'coin_price': COIN_PRICE_FIELDS,
    'coin_market': COIN_MARKET_FIELDS,
}


def get_preset(name: str) -> list:
    """
    Get a field preset by name.

    :param name: Preset name (e.g., 'stock_price', 'crypto_volume')
    :return: List of fields
    :raises KeyError: If preset name is not found

    Example:
        >>> from tvscreener.field.presets import get_preset
        >>> fields = get_preset('stock_valuation')
    """
    if name not in ALL_PRESETS:
        available = ', '.join(sorted(ALL_PRESETS.keys()))
        raise KeyError(f"Unknown preset: '{name}'. Available presets: {available}")
    return ALL_PRESETS[name]


def list_presets() -> list:
    """
    List all available preset names.

    :return: List of preset names

    Example:
        >>> from tvscreener.field.presets import list_presets
        >>> print(list_presets())
        ['stock_price', 'stock_volume', ...]
    """
    return list(ALL_PRESETS.keys())
