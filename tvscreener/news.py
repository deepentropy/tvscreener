import json
import re
from datetime import datetime, timezone

import pandas as pd
import requests

NEWS_URL = "https://news-mediator.tradingview.com/public/news-flow/v2/news"
STORY_URL = "https://news-mediator.tradingview.com/public/news/v1/story"
ARTICLE_BASE_URL = "https://www.tradingview.com"
REQUEST_TIMEOUT = 30

REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Origin': 'https://www.tradingview.com',
    'Referer': 'https://www.tradingview.com/',
}


def get_news(symbol=None, lang="en", provider=None, market=None, sector=None, corp_activity=None,
             country=None, priority=None):
    """
    Get news headlines from TradingView (up to 200, newest first).

    Filters are combined with AND, and each takes one value.

    :param symbol: TradingView symbol (e.g. "NASDAQ:AAPL", "BINANCE:BTCUSDT"). If None, returns global news.
    :param lang: Language code (default "en")
    :param provider: News provider id, e.g. "reuters", "dow-jones", "business_wire", "tradingview", "zacks"
    :param market: "stock", "etf", "crypto", "forex", "index", "futures", "bond", "corp_bond" or "economic"
    :param sector: Stock sector, e.g. "Electronic Technology", "Finance"
    :param corp_activity: Corporate activity: "ipo", "earnings", "earnings_calls", "dividends", "share_buybacks",
        "strategy_business_products", "mergers_and_acquisitions", "management", "insider_trading",
        "ownership_changes", "esg", "recommendation" (analyst ratings) or "credit_ratings"
    :param country: ISO country code of the market, e.g. "US", "GB"
    :param priority: "flash", "important", "top_stories" or "key_facts"
    :return: DataFrame with columns: id, title, published, provider, related_symbols, story_path, urgency
    """
    filters = {"lang": lang, "symbol": symbol, "provider": provider, "market": market, "sector": sector,
               "corp_activity": corp_activity, "market_country": country.upper() if country else None,
               "priority": priority}
    params = {
        # The API rejects filters that are not in alphabetical order
        "filter": sorted(f"{key}:{value}" for key, value in filters.items() if value),
        "client": "overview",
        "streaming": "false",
        "user_prostatus": "non_pro",
    }

    response = requests.get(
        NEWS_URL,
        params=params,
        headers=REQUEST_HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    data = response.json()

    rows = []
    for item in data.get("items", []):
        related = [s["symbol"] for s in item.get("relatedSymbols", [])]
        rows.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "published": datetime.fromtimestamp(item["published"], tz=timezone.utc),
            "provider": item.get("provider", {}).get("name"),
            "related_symbols": related,
            "story_path": item.get("storyPath"),
            "urgency": item.get("urgency"),
        })

    return pd.DataFrame(rows, columns=["id", "title", "published", "provider", "related_symbols", "story_path",
                                       "urgency"])


def get_article(story):
    """
    Fetch the full article text of a TradingView news story.

    :param story: Story ``id`` from get_news() (e.g. "DJN_DN20261015001560:0"), read from TradingView's
        news API; or its ``story_path`` / URL (e.g. "/news/reuters.com,2026:newsml_..."), read from the web page
    :return: Article text as string. Paywalled stories return their summary.
    :raises requests.HTTPError: If the story does not exist
    """
    if not story.startswith(("/", "http")):
        response = requests.get(STORY_URL, params={"id": story, "lang": "en"}, headers=REQUEST_HEADERS,
                                timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        return _ast_to_text(data.get("ast_description")) or data.get("short_description") or ""

    story_path = story
    if story_path.startswith("http"):
        url = story_path
    else:
        url = f"{ARTICLE_BASE_URL}{story_path}"

    response = requests.get(url, headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    # Extract article body from the HTML
    # TradingView wraps article content in a <div class="body-..."> with paragraphs
    html = response.text
    body = _extract_article_body(html)
    return body


def _extract_article_body(html):
    """Extract article text from TradingView news page HTML."""
    # Strategy 1: Extract from HTML <p> tags in the body div (most articles)
    body_match = re.search(r'class="body-\w+[^"]*">(.*)', html, re.DOTALL)
    if body_match:
        body_html = body_match.group(1)
        paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', body_html, re.DOTALL)
        # Need at least 2 paragraphs to be a real article (not nav junk)
        if len(paragraphs) >= 2:
            lines = []
            for p in paragraphs:
                text = re.sub(r'<[^>]+>', '', p).strip()
                if text:
                    lines.append(text)
            if lines:
                return "\n\n".join(lines)

    # Strategy 2: Extract from embedded JSON ast_description (paywalled articles)
    return _extract_from_ast(html)


def _extract_from_ast(html):
    """Extract article text from TradingView's embedded JSON AST."""
    idx = html.find('"ast_description":{')
    if idx < 0:
        return ""

    start = idx + len('"ast_description":')
    depth = 0
    for i, c in enumerate(html[start:start + 20000]):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        if depth == 0:
            try:
                ast = json.loads(html[start:start + i + 1])
                return _ast_to_text(ast)
            except json.JSONDecodeError:
                return ""
    return ""


_BLOCK_NODES = {"root", "list"}


def _ast_to_text(node):
    """Recursively extract text from a TradingView AST node, one block (paragraph, list item) per line block."""
    if isinstance(node, str):
        return node
    if not isinstance(node, dict):
        return ""
    params = node.get("params") or {}
    if node.get("type") == "symbol":
        return params.get("text") or params.get("symbol") or ""
    if node.get("type") == "url":
        return params.get("linkText") or params.get("url") or ""
    texts = [_ast_to_text(c) for c in node.get("children", [])]
    if node.get("type") in _BLOCK_NODES:
        return "\n\n".join(t.strip() for t in texts if t and t.strip())
    return "".join(texts)
