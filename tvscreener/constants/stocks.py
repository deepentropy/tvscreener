from tvscreener.config.universe import AssetUniverse, IndicatorFields

DEFAULT_STOCK_PAIRS = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META",
    "NVDA",
    "TSLA",
    "BRK.B",
    "JPM",
    "JNJ",
    "V",
    "PG",
    "MA",
    "UNH",
    "HD",
    "DIS",
    "BAC",
    "ADBE",
    "CRM",
    "NFLX",
]

DEFAULT_STOCK_TIMEFRAMES = ["60", "240", "D"]

DEFAULT_STOCK_TF_WEIGHTS = {"60": 0.4, "240": 0.35, "D": 0.25}

STOCK_EXCHANGES = [
    "NASDAQ",
    "NYSE",
    "AMEX",
]

STOCK_UNIVERSE = AssetUniverse(
    name="stocks",
    pairs=DEFAULT_STOCK_PAIRS,
    timeframes=DEFAULT_STOCK_TIMEFRAMES,
    default_tf_weights=DEFAULT_STOCK_TF_WEIGHTS,
    fields=IndicatorFields(
        recommend_all="Recommend All|{tf}",
        recommend_ma="Recommend Ma|{tf}",
        recommend_osc="Recommend Other|{tf}",
        momentum="Rsi|{tf}",
    ),
    exchanges=STOCK_EXCHANGES,
    core_class_name="StockScreener",
    field_class_name="StockField",
)
STOCK_UNIVERSE.validate()
