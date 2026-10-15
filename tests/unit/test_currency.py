import pytest

from tvscreener import StockScreener, CryptoScreener, Market


def test_set_currency_payload():
    ss = StockScreener().set_currency("EUR")
    assert ss._build_payload(["name"])["price_conversion"] == {"to_currency": "eur"}


def test_set_currency_keeps_existing_conversion():
    cs = CryptoScreener().set_currency("usd")
    assert cs.misc["price_conversion"] == {"to_symbol": False, "to_currency": "usd"}


@pytest.mark.parametrize("bad", ["euro", "us", "", None, "u$d"])
def test_set_currency_validates(bad):
    with pytest.raises(ValueError):
        StockScreener().set_currency(bad)


def test_set_markets_is_chainable():
    ss = StockScreener().set_markets(Market.JAPAN, Market.GERMANY).set_currency("jpy")
    assert ss.markets == [Market.JAPAN, Market.GERMANY]
