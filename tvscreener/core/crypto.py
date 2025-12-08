from tvscreener.core.base import Screener, default_sort_crypto
from tvscreener.field.crypto import CryptoField, DEFAULT_CRYPTO_FIELDS
from tvscreener.util import get_url


class CryptoScreener(Screener):
    """Crypto screener for querying cryptocurrencies from TradingView."""

    _field_type = CryptoField

    def __init__(self):
        super().__init__()
        subtype = "crypto"
        self.markets = {subtype}  # Fixed: set literal instead of set(string)
        self.url = get_url(subtype)
        self.specific_fields = DEFAULT_CRYPTO_FIELDS  # Use default fields (set to CryptoField for all 3000+ fields)
        self.sort_by(default_sort_crypto, False)
        self.add_misc("price_conversion", {"to_symbol": False})
