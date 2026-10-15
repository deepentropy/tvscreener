from tvscreener.core.base import Screener
from tvscreener.field.index import IndexField
from tvscreener.util import get_url

DEFAULT_INDEX_FIELDS = [
    IndexField.NAME,
    IndexField.DESCRIPTION,
    IndexField.TYPE,
    IndexField.CLOSE,
    IndexField.CHANGE,
    IndexField.CHANGE_ABS,
    IndexField.CURRENCY,
    IndexField.EXCHANGE,
]


class IndexScreener(Screener):
    """
    Indices, commodity CFDs and crypto market-cap indices (TradingView ``/cfd`` scanner).

    Use the typespecs helpers to pick a group:

    - ``main_indices()``: main stock indices (e.g. SSE Composite)
    - ``cfds()``: index and commodity CFDs (TVC, OANDA...)
    - ``crypto_market_caps()``: CRYPTOCAP market-cap indices (TOTAL, BTC, ETH...)

    Example:
        >>> df = IndexScreener().cfds().get()
    """

    _field_type = IndexField

    def __init__(self):
        super().__init__()
        self.url = get_url("cfd")
        self.specific_fields = DEFAULT_INDEX_FIELDS
        self.sort_by(IndexField.NAME, True)

    def main_indices(self) -> 'IndexScreener':
        """Keep main stock indices."""
        self.where(IndexField.TYPESPECS.has('main'))
        return self

    def cfds(self) -> 'IndexScreener':
        """Keep index and commodity CFDs."""
        self.where(IndexField.TYPESPECS.has('cfd'))
        return self

    def crypto_market_caps(self) -> 'IndexScreener':
        """Keep crypto market-cap indices (CRYPTOCAP)."""
        self.where(IndexField.TYPESPECS.has('crypto'))
        return self
