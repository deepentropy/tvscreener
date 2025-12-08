from tvscreener.core.base import Screener
from tvscreener.field.futures import FuturesField, DEFAULT_FUTURES_FIELDS
from tvscreener.util import get_url


class FuturesScreener(Screener):
    """Futures screener for querying futures from TradingView."""

    _field_type = FuturesField

    def __init__(self):
        super().__init__()
        self.url = get_url("futures")
        self.specific_fields = DEFAULT_FUTURES_FIELDS
        self.sort_by(FuturesField.VOLUME, False)
