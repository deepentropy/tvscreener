from tvscreener.config.universe import AssetUniverse, IndicatorFields

DEFAULT_CRYPTO_PAIRS = [
    "BTCUSD",
    "ETHUSD",
    "BNBUSD",
    "XRPUSD",
    "ADAUSD",
    "DOGEUSD",
    "SOLUSD",
    "DOTUSD",
    "MATICUSD",
    "LTCUSD",
    "AVAXUSD",
    "LINKUSD",
    "ATOMUSD",
    "UNIUSD",
    "XLMUSD",
]

DEFAULT_CRYPTO_TIMEFRAMES = ["60", "240", "D"]

DEFAULT_CRYPTO_TF_WEIGHTS = {"60": 0.4, "240": 0.35, "D": 0.25}

CRYPTO_EXCHANGES = [
    "BINANCE",
    "COINBASE",
    "KRAKEN",
    "FTX",
    "BYBIT",
]

CRYPTO_UNIVERSE = AssetUniverse(
    name="crypto",
    pairs=DEFAULT_CRYPTO_PAIRS,
    timeframes=DEFAULT_CRYPTO_TIMEFRAMES,
    default_tf_weights=DEFAULT_CRYPTO_TF_WEIGHTS,
    fields=IndicatorFields(
        recommend_all="Recommend All|{tf}",
        recommend_ma="Recommend Ma|{tf}",
        recommend_osc="Recommend Other|{tf}",
        momentum="MACD.macd|{tf}",
    ),
    exchanges=CRYPTO_EXCHANGES,
    core_class_name="CryptoScreener",
    field_class_name="CryptoField",
)
CRYPTO_UNIVERSE.validate()
