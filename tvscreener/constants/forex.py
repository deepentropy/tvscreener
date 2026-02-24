FOREX_MAJORS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "USDCHF",
    "USDCAD",
    "AUDUSD",
    "NZDUSD",
]

FOREX_MINORS = [
    "EURGBP",
    "EURJPY",
    "GBPJPY",
    "EURCHF",
    "AUDJPY",
    "EURCAD",
    "CADJPY",
    "CHFJPY",
    "NZDJPY",
    "GBPAUD",
    "EURAUD",
    "AUDNZD",
    "EURNZD",
    "GBPCAD",
    "AUDCAD",
    "GBPNZD",
]

DEFAULT_FOREX_PAIRS = FOREX_MAJORS + FOREX_MINORS

DEFAULT_TIMEFRAMES = ["15", "60", "240"]

TIMEFRAME_LABELS = {
    "15": "15m",
    "60": "1H",
    "240": "4H",
}

DEFAULT_TIMEFRAME_WEIGHTS = {"15": 0.5, "60": 0.3, "240": 0.2}

LIQUID_EXCHANGES = [
    "OANDA",
    "ICMARKETS",
    "IG",
    "FOREXCOM",
    "PEPPERSTONE",
    "FXOPEN",
    "BLACKBULL",
]

EXCHANGE_PRIORITY = {exchange: idx for idx, exchange in enumerate(LIQUID_EXCHANGES)}

CONTRACT_TYPES = ["spot", "cfd", "spreadbet"]
