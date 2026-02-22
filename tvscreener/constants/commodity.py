from tvscreener.config.universe import AssetUniverse, IndicatorFields

DEFAULT_COMMODITY_PAIRS = [
    "GC=F",
    "SI=F",
    "CL=F",
    "NG=F",
    "HG=F",
    "HE=F",
    "ZC=F",
    "ZS=F",
    "ZW=F",
    "KC=F",
    "CT=F",
    "LBS=F",
    "OJ=F",
    "PA=F",
    "PL=F",
]

DEFAULT_COMMODITY_TIMEFRAMES = ["60", "240", "D"]

DEFAULT_COMMODITY_TF_WEIGHTS = {"60": 0.4, "240": 0.35, "D": 0.25}

COMMODITY_EXCHANGES = [
    "CME",
    "COMEX",
    "NYMEX",
    "CBOT",
    "ICE",
]

COMMODITY_UNIVERSE = AssetUniverse(
    name="commodity",
    pairs=DEFAULT_COMMODITY_PAIRS,
    timeframes=DEFAULT_COMMODITY_TIMEFRAMES,
    default_tf_weights=DEFAULT_COMMODITY_TF_WEIGHTS,
    fields=IndicatorFields(
        recommend_all="Recommend All|{tf}",
        recommend_ma="Recommend Ma|{tf}",
        recommend_osc="Recommend Other|{tf}",
        momentum="Stoch.K|{tf}",
    ),
    exchanges=COMMODITY_EXCHANGES,
    core_class_name="FuturesScreener",
    field_class_name="FuturesField",
)
COMMODITY_UNIVERSE.validate()
