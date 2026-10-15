import importlib.util
import pathlib
import warnings

import pytest

from tvscreener import StockScreener, StockField, CoinField, CoinScreener

ROOT = pathlib.Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("generate_fields", ROOT / "scripts" / "generate_fields.py")
generate_fields = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generate_fields)


class TestDeprecatedFields:

    def test_flag(self):
        assert StockField.DIVIDEND_YIELD_FORWARD.deprecated
        assert not StockField.PRICE.deprecated
        assert StockField.RSI2.with_interval('60').deprecated is False

    def test_select_warns(self):
        with pytest.warns(DeprecationWarning, match="DIVIDEND_YIELD_FORWARD"):
            StockScreener().select(StockField.NAME, StockField.DIVIDEND_YIELD_FORWARD)

    def test_where_warns(self):
        with pytest.warns(DeprecationWarning):
            StockScreener().where(StockField.DIVIDEND_YIELD_FORWARD > 1)
        with pytest.warns(DeprecationWarning):
            StockScreener().where((StockField.DIVIDEND_YIELD_FORWARD > 1) | (StockField.PRICE > 1))

    def test_working_fields_do_not_warn(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            StockScreener().select(StockField.NAME, StockField.PRICE).where(StockField.PRICE > 1)

    def test_select_all_skips_deprecated(self):
        fields = CoinScreener().select_all().specific_fields
        assert CoinField.VOLUME not in fields
        assert all(not f.deprecated for f in fields)

    def test_dividend_yield_fy_alias_points_to_working_field(self):
        assert StockField.DIVIDEND_YIELD_FY.field_name == "dividends_yield_fy"
        assert not StockField.DIVIDEND_YIELD_FY.deprecated


class TestNewFields:

    @pytest.mark.parametrize("member, api", [
        ("PRICE_EARNINGS_FWD", "price_earnings_fwd"),
        ("EBITDA_ESTIMATE_NTM", "ebitda_estimate_ntm"),
        ("CANDLE_PIERCING_BULLISH", "Candle.Piercing.Bullish"),
        ("PERF_Y_ABS", "Perf.Y_abs"),
        ("IPO_OFFER_PRICE", "ipo_offer_price"),
    ])
    def test_stock(self, member, api):
        assert StockField[member].field_name == api

    def test_candle_patterns_accept_intervals(self):
        assert StockField.CANDLE_PIERCING_BULLISH.with_interval('60').field_name == "Candle.Piercing.Bullish|60"

    def test_coin_derivatives(self):
        assert CoinField.FUNDING_RATE.field_name == "funding_rate"
        assert CoinField.OPEN_INTEREST_CHANGE_PERCENT_24H.field_name == "open_interest_change_percent_24h"


class TestGeneratorHelpers:

    @pytest.mark.parametrize("api, label", [
        ("capital_expenditures_estimate_fq", "Capital Expenditures Estimate (FQ)"),
        ("price_earnings_fwd", "Price Earnings (Forward)"),
        ("Perf.Y_abs", "Performance 1 Year (Abs)"),
        ("Candle.DojiStar.Bullish", "Candle.DojiStar.Bullish"),
        ("eps_estimate_ntm", "EPS Estimate (NTM)"),
    ])
    def test_humanize(self, api, label):
        assert generate_fields.humanize(api) == label

    @pytest.mark.parametrize("api, member", [
        ("Perf.Y_abs", "PERF_Y_ABS"), ("24h_vol_cmc", "F_24H_VOL_CMC"), ("Candle.Piercing.Bullish", "CANDLE_PIERCING_BULLISH"),
    ])
    def test_member_name(self, api, member):
        assert generate_fields.member_name(api) == member

    @pytest.mark.parametrize("name, result", [
        ("RSI", ("RSI", None)), ("RSI|60", ("RSI", "60")), ("RSI[1]", ("RSI", None)), ("RSI[1]|60", ("RSI", "60")),
    ])
    def test_split_name(self, name, result):
        assert generate_fields.split_name(name) == result
