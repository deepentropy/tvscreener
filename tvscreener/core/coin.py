from tvscreener.core.base import Screener
from tvscreener.field.coin import CoinField, DEFAULT_COIN_FIELDS
from tvscreener.util import get_url


class CoinScreener(Screener):
    """Coin screener for querying coins (CEX and DEX) from TradingView."""

    _field_type = CoinField

    def __init__(self):
        super().__init__()
        self.url = get_url("coin")
        self.specific_fields = DEFAULT_COIN_FIELDS
        self.sort_by(CoinField.MARKET_CAP, False)
        self.add_misc("price_conversion", {"to_symbol": False})
