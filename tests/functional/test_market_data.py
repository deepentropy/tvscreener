"""Live checks of the helpers built on TradingView's website APIs (network required)."""
import datetime as dt

from tvscreener import get_economic_calendar, get_forward_curve, get_yield_matrix, search_symbols, get_peers, \
    get_volatility_smile, get_documents, get_document, get_earnings_calls, get_news, get_article, \
    get_financials, get_corporate_events, get_seasonals, stream_quotes, OptionScreener


def test_economic_calendar():
    today = dt.date.today()
    df = get_economic_calendar(today - dt.timedelta(days=7), today, countries="US")
    assert len(df) > 0
    assert set(df["country"]) == {"US"}
    assert df["importance"].isin(["low", "medium", "high"]).all()


def test_forward_curve():
    df = get_forward_curve("CME_MINI:ES1!")
    assert len(df) > 3
    assert df["expiration"].is_monotonic_increasing
    assert df["symbol"].str.startswith("CME_MINI:ES").all()


def test_yield_matrix():
    df = get_yield_matrix(["US", "DE"], ["2Y", "10Y"])
    assert df.loc["US", "10Y"] > 0 and df.loc["DE", "2Y"] > 0


def test_search_and_peers():
    df = search_symbols("US0378331005")
    assert "NASDAQ:AAPL" in df["symbol"].values
    peers = get_peers("NASDAQ:AAPL", 5)
    assert len(peers) == 5 and "NASDAQ:AAPL" not in peers["symbol"].values


def test_volatility_smile():
    expirations = OptionScreener("NASDAQ:AAPL").get()["Expiration"]
    expiration = expirations.max()
    df = get_volatility_smile("NASDAQ:AAPL", expiration)
    assert len(df) > 5 and (df["iv"] > 0).all()


def test_documents_and_calls():
    docs = get_documents("NASDAQ:AAPL", category="call_transcript")
    assert len(docs) > 4
    assert len(get_document(docs["transcript_id"].iloc[0])) > 1000
    calls = get_earnings_calls("NASDAQ:AAPL")
    assert len(calls) >= 3


def test_news_filters_and_article():
    news = get_news("NASDAQ:AAPL", market="stock")
    assert len(news) > 0
    assert len(get_article(news["id"].iloc[0])) > 0


def test_financials():
    df = get_financials("NASDAQ:AAPL", "income", "FY")
    assert len(df) >= 10
    assert df.columns[1] == "Total revenue"
    assert df["Total revenue"].iloc[-1] > 1e11
    assert df.attrs["currency"] == "USD"
    quarterly = get_financials("NYSE:JPM", "balance_sheet", "FQ")
    assert len(quarterly) >= 16 and quarterly.index[-1].startswith("20")


def test_corporate_events_and_seasonals():
    events = get_corporate_events("NASDAQ:AAPL", ["dividends", "earnings"])
    assert len(events["dividends"]) > 4 and (events["dividends"]["amount"] > 0).all()
    assert events["earnings"]["reported"].any()
    seasonals = get_seasonals("NASDAQ:AAPL", 2020, 2024)
    assert seasonals.index.tolist() == [2020, 2021, 2022, 2023, 2024]
    assert seasonals.notna().all().all()


def test_stream_quotes():
    updates = list(stream_quotes("BINANCE:BTCUSDT", max_updates=5, duration=30))
    priced = [u for u in updates if u.get("price")]
    assert priced and priced[-1]["price"] > 0
    assert isinstance(priced[-1]["time"], dt.datetime)
