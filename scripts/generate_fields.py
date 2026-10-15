"""
Generate field enum entries from TradingView's scanner metainfo (#64).

For each market:
1. Read /{market}/metainfo.
2. Check which fields hold data on large samples of real symbols. The catalogue is
   partly generic, so a listed field is only added when it returns values.
3. Add the populated fields missing from the enum, with interval / historical flags
   derived from the '|interval' and '[n]' variants listed in metainfo.
4. Mark enum fields that return no data in any sample as deprecated.

Usage:
    python scripts/generate_fields.py report             # print the changes, write scripts/output/
    python scripts/generate_fields.py write              # update the existing enums
    python scripts/generate_fields.py write coin bond    # only some markets
    python scripts/generate_fields.py new economics2 EconomicsField tvscreener/field/economics.py
"""
import collections
import concurrent.futures
import csv
import datetime as dt
import json
import pathlib
import re
import sys
import time

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tvscreener.util import _format_timed_fields  # noqa: E402

SCANNER = "https://scanner.tradingview.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
    'Content-Type': 'application/json',
}
OUTPUT = ROOT / "scripts" / "output"

# Existing enums: module, class, scanner market, samples (sort field, rows), extra payload
MARKETS = {
    "stock": ("stock", "StockField", "global", [("market_cap_basic", 20000), ("Value.Traded", 20000)], {}),
    "crypto": ("crypto", "CryptoField", "crypto", [("24h_vol|5", 20000), ("market_cap_calc", 20000)],
               {"price_conversion": {"to_symbol": False}}),
    "forex": ("forex", "ForexField", "forex", [("name", 20000)], {}),
    "bond": ("bond", "BondField", "bond", [("volume", 20000), ("coupon", 20000)], {}),
    "futures": ("futures", "FuturesField", "futures", [("volume", 20000), ("open_interest", 20000)], {}),
    "coin": ("coin", "CoinField", "coin", [("market_cap_calc", 20000)], {"price_conversion": {"to_symbol": False}}),
}
NEW_MARKET_SAMPLES = [("name", 20000)]

COLUMN_CHUNK = 60
# Returned by every scanner but not listed in metainfo
IDENTITY_FIELDS = {"name": "text", "description": "text"}
HISTORY_RE = re.compile(r"\[\d+\]$")

# Metainfo type -> enum format, when the existing enum gives no majority
DEFAULT_FORMATS = {"text": "text", "bool": "bool", "percent": "percent", "time": "date", "time-yyyymmdd": "date",
                   "set": "text", "interface": "text", "map": "text"}

ACRONYMS = {"eps", "ebitda", "ebit", "fcf", "ipo", "roe", "roa", "roic", "ev", "ttm", "fq", "fy", "fh", "ntm", "dps",
            "bvps", "usd", "atr", "rsi", "adx", "di", "sma", "ema", "macd", "vwap", "vwma", "cfi", "dv", "ytm", "ytw",
            "id", "nvt", "tvl", "isin", "cusip", "etf", "uo", "ao", "cci", "mom", "oi", "pe", "ps", "pb"}
PERIOD_SUFFIX = {"fq": "FQ", "fy": "FY", "fh": "FH", "ttm": "TTM", "ntm": "NTM", "fwd": "Forward"}
PERF_PERIODS = {"5D": "5 Days", "W": "1 Week", "1M": "1 Month", "3M": "3 Months", "6M": "6 Months", "YTD": "Year to Date",
                "Y": "1 Year", "3Y": "3 Years", "5Y": "5 Years", "10Y": "10 Years", "All": "All Time"}


def post(path, payload, retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(SCANNER + path, headers=HEADERS, data=json.dumps(payload), timeout=180)
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError):
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))


def populated(market, columns, samples, extra):
    """
    Return {column: non-null count}. A quick pass on the first 2,000 rows of the first
    sample, then the columns still empty are checked on every full sample.
    """
    quick = _count(market, columns, [(samples[0][0], 2000)], extra)
    empty = [c for c in columns if not quick[c]]
    full = _count(market, empty, samples, extra)
    return quick + full


def _count(market, columns, samples, extra, workers=6):
    counts = collections.Counter({c: 0 for c in columns})

    def run(task):
        sort_by, rows, chunk = task
        payload = {"columns": chunk, "range": [0, rows], "sort": {"sortBy": sort_by, "sortOrder": "desc"}, **extra}
        data = post(f"/{market}/scan", payload).get("data") or []
        return chunk, [sum(1 for d in data if d["d"][j] not in (None, "", [], {})) for j in range(len(chunk))]

    tasks = [(sort_by, rows, columns[i:i + COLUMN_CHUNK])
             for sort_by, rows in samples for i in range(0, len(columns), COLUMN_CHUNK)]
    with concurrent.futures.ThreadPoolExecutor(workers) as pool:
        for chunk, values in pool.map(run, tasks):
            for col, n in zip(chunk, values):
                counts[col] += n
    print(f"    {market}: {len(columns)} columns x {len(samples)} sample(s) checked", flush=True)
    return counts


def metainfo(market):
    return {f["n"]: f for f in post(f"/{market}/metainfo", {})["fields"]}


def split_name(name):
    """'RSI|60' -> ('RSI', '60'); 'RSI[1]' -> ('RSI', None) with history; plain -> (name, None)."""
    base = HISTORY_RE.sub("", name)
    if "|" in base:
        base, interval = base.split("|", 1)
        return HISTORY_RE.sub("", base), interval
    return base, None


def humanize(api):
    if api.startswith("Candle."):
        return api
    m = re.match(r"Perf\.(\w+?)_abs$", api)
    if m and m.group(1) in PERF_PERIODS:
        return f"Performance {PERF_PERIODS[m.group(1)]} (Abs)"
    tokens = [t for t in re.split(r"[_.\-|]+", api) if t]
    suffix = None
    if tokens and tokens[-1].lower() in PERIOD_SUFFIX:
        suffix = PERIOD_SUFFIX[tokens.pop().lower()]
    words = []
    for t in tokens:
        low = t.lower()
        words.append(t.upper() if low in ACRONYMS else (t if any(c.isupper() for c in t[1:]) else t.capitalize()))
    label = " ".join(words)
    return f"{label} ({suffix})" if suffix else label


def member_name(api):
    name = re.sub(r"[^0-9A-Za-z]+", "_", api).strip("_").upper()
    return f"F_{name}" if name[:1].isdigit() else name


def load_enum(module, cls):
    import importlib
    mod = importlib.import_module(f"tvscreener.field.{module}")
    return list(getattr(mod, cls))


def request_name(field_name):
    return _format_timed_fields(field_name)


def format_majority(enum_fields, meta):
    votes = collections.defaultdict(collections.Counter)
    for f in enum_fields:
        if f.field_name in meta:
            votes[meta[f.field_name].get("t")][f.format] += 1
    return {t: c.most_common(1)[0][0] for t, c in votes.items()}


def plan_market(key, market, samples, extra, enum_fields):
    """Compute (additions, deprecations) for one market."""
    meta = metainfo(market)
    names = set(meta)
    intervals = collections.defaultdict(set)
    historical = set()
    for n in names:
        base, interval = split_name(n)
        if HISTORY_RE.search(n.split("|")[0]):
            historical.add(base)
        if interval:
            intervals[base].add(interval)

    existing = {f.field_name for f in enum_fields}
    existing_bases = {split_name(f.field_name.replace(".", "|", 1) if f.field_name.startswith(("change.", "change_abs.")) else f.field_name)[0]
                      for f in enum_fields} | existing

    # Candidates: bases listed in metainfo; fields only listed with an interval are added with it
    candidates = {}
    for n in names:
        if HISTORY_RE.search(n.split("|")[0]):
            continue
        base, interval = split_name(n)
        if base in names:
            if base not in existing_bases:
                candidates[base] = base
        elif interval and n not in existing and base not in existing_bases:
            candidates[n] = n
    for n in IDENTITY_FIELDS:
        if n not in existing_bases:
            candidates[n] = n
    candidates = sorted(candidates)

    # Population: candidates and existing fields on the same samples
    enum_requests = {}
    for f in enum_fields:
        if f.field_name.startswith("candlestick"):
            continue
        enum_requests[request_name(f.field_name)] = f
    counts = populated(market, candidates + sorted(enum_requests), samples, extra)

    formats = format_majority(enum_fields, meta)
    additions = []
    for api in candidates:
        if not counts[api]:
            continue
        base = split_name(api)[0] if api == split_name(api)[0] else api
        t = meta.get(api, meta.get(base, {})).get("t")
        additions.append({
            "market": key, "member": member_name(api), "label": humanize(api), "field": api,
            "format": IDENTITY_FIELDS.get(api) or formats.get(t) or DEFAULT_FORMATS.get(t, "float"),
            "interval": bool(intervals.get(api)) and api == base,
            "historical": api in historical,
            "non_null": counts[api], "type": t,
        })
    deprecations = [{"market": key, "member": f.name, "field": f.field_name}
                    for req, f in enum_requests.items() if counts[req] == 0 and not getattr(f, "deprecated", False)]
    return additions, deprecations


def dedupe(additions, enum_fields):
    names = {f.name for f in enum_fields}
    labels = {f.label for f in enum_fields}
    for a in additions:
        base_name, n = a["member"], 2
        while a["member"] in names:
            a["member"] = f"{base_name}_{n}"
            n += 1
        names.add(a["member"])
        if a["label"] in labels:
            a["label"] = f"{a['label']} ({a['field']})"
        labels.add(a["label"])


def entry_line(a):
    label = a["label"].replace("\\", "\\\\").replace("'", "\\'")
    return f"    {a['member']} = '{label}', '{a['field']}', '{a['format']}', {a['interval']}, {a['historical']}"


def write_market(module, cls, additions, deprecations):
    path = ROOT / "tvscreener" / "field" / f"{module}.py"
    lines = path.read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if l.startswith(f"class {cls}("))
    end = next((i for i in range(start + 1, len(lines)) if lines[i] and not lines[i][0].isspace()), len(lines))
    while lines[end - 1].strip() == "":
        end -= 1

    deprecated = {d["member"] for d in deprecations}
    member_re = re.compile(r"^    (\w+) = (.+?)\s*$")
    for i in range(start, end):
        m = member_re.match(lines[i])
        if m and m.group(1) in deprecated and m.group(2).count(",") == 4:
            lines[i] = f"    {m.group(1)} = {m.group(2)}, True"

    if additions:
        today = dt.date.today().strftime("%d/%m/%Y")
        block = ["", f"    # Added from {cls[:-5].lower()} metainfo by scripts/generate_fields.py ({today})"]
        block += [entry_line(a) for a in sorted(additions, key=lambda a: a["member"])]
        lines[end:end] = block
    path.write_text("\n".join(lines), encoding="utf-8")


def write_new(market, cls, path, additions):
    today = dt.date.today().strftime("%d/%m/%Y")
    body = [
        "from tvscreener.field import Field",
        "",
        "",
        f"class {cls}(Field):",
        '    """',
        f"    {cls} enum generated from /{market}/metainfo by scripts/generate_fields.py ({today}).",
        "",
        "    Only fields that returned data on real symbols are included.",
        "",
        "    Each field is defined as:",
        "    ENUM_NAME = 'Label', 'api_name', 'format_type', supports_interval, supports_history",
        '    """',
        "",
    ]
    body += [entry_line(a) for a in sorted(additions, key=lambda a: a["member"])]
    (ROOT / path).write_text("\n".join(body) + "\n", encoding="utf-8")


def save_report(additions, deprecations, suffix):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT / f"added_{suffix}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["market", "member", "label", "field", "format", "interval", "historical", "non_null", "type"])
        w.writeheader()
        w.writerows(additions)
    with open(OUTPUT / f"deprecated_{suffix}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["market", "member", "field"])
        w.writeheader()
        w.writerows(deprecations)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "report"
    only = sys.argv[2:] if mode in ("report", "write") else []
    if mode == "new":
        market, cls, path = sys.argv[2:5]
        additions, _ = plan_market(market, market, NEW_MARKET_SAMPLES, {}, [])
        dedupe(additions, [])
        save_report(additions, [], market)
        write_new(market, cls, path, additions)
        print(f"{cls}: {len(additions)} fields written to {path}")
        return

    all_add, all_dep = [], []
    for key, (module, cls, market, samples, extra) in MARKETS.items():
        if only and key not in only:
            continue
        enum_fields = load_enum(module, cls)
        additions, deprecations = plan_market(key, market, samples, extra, enum_fields)
        dedupe(additions, enum_fields)
        print(f"{key:8s} enum={len(enum_fields):5d} add={len(additions):4d} deprecate={len(deprecations):4d}", flush=True)
        all_add += additions
        all_dep += deprecations
        save_report(additions, deprecations, key)
        if mode == "write":
            write_market(module, cls, additions, deprecations)
    save_report(all_add, all_dep, "enums")


if __name__ == "__main__":
    main()
