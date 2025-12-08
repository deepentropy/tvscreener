from tvscreener.core.base import Screener
from tvscreener.field.bond import BondField, DEFAULT_BOND_FIELDS
from tvscreener.util import get_url


class BondScreener(Screener):
    """Bond screener for querying bonds from TradingView."""

    _field_type = BondField

    def __init__(self):
        super().__init__()
        self.url = get_url("bond")
        self.specific_fields = DEFAULT_BOND_FIELDS
        self.sort_by(BondField.VOLUME, False)
