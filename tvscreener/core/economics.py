from enum import Enum

import pandas as pd

from tvscreener.core.base import Screener
from tvscreener.field.economics import EconomicsField
from tvscreener.util import get_url


class EconomicCategory(Enum):
    """Categories of economic indicators (values of EconomicsField.ECONOMIC_CATEGORY_ID)."""
    GDP = "gdp"
    LABOUR = "lbr"
    PRICES = "prce"
    MONEY = "mny"
    TRADE = "trd"
    GOVERNMENT = "gov"
    BUSINESS = "bsnss"
    CONSUMER = "cnsm"
    HOUSING = "hse"
    TAXES = "txs"
    HEALTH = "hlth"
    ENERGY = "enrg"
    CLIMATE = "clmt"


DEFAULT_ECONOMICS_FIELDS = [
    EconomicsField.NAME,
    EconomicsField.DESCRIPTION,
    EconomicsField.COUNTRY_CODE,
    EconomicsField.ECONOMIC_CATEGORY_ID,
    EconomicsField.CLOSE,
    EconomicsField.VALUE_UNIT_ID,
    EconomicsField.CURRENCY,
    EconomicsField.TIME,
    EconomicsField.CHANGE,
    EconomicsField.CHANGE_ABS,
]


class EconomicsScreener(Screener):
    """
    Economic indicator screener (GDP, unemployment, inflation, rates...) for 190+ countries.

    ``CLOSE`` is the latest value of the indicator and ``TIME`` the period it refers to.

    Example:
        >>> es = EconomicsScreener()
        >>> es.where(EconomicsField.COUNTRY_CODE == 'US')
        >>> es.where(EconomicsField.ECONOMIC_CATEGORY_ID == EconomicCategory.LABOUR)
        >>> df = es.get()
    """

    _field_type = EconomicsField

    def __init__(self):
        super().__init__()
        self.url = get_url("economics2")
        self.specific_fields = DEFAULT_ECONOMICS_FIELDS
        self.sort_by(EconomicsField.NAME, True)

    def get(self, print_request=False):
        """
        Get the economic indicators.

        Period timestamps (``TIME``) are converted to UTC datetimes.

        :param print_request: If True, prints the request URL and payload for debugging.
        :return: ScreenerDataFrame with one row per indicator
        """
        df = super().get(print_request)
        label = EconomicsField.TIME.label
        if label in df.columns:
            df[label] = pd.to_datetime(df[label], unit="s", utc=True)
        return df
