import sys

from tvscreener import cli


class DummySettings:
    default_universe = "majors"
    default_timeframes = "240,60,15"
    contract_type = "cfd"
    min_volume = None
    max_atr = None
    min_ma_rating = None
    min_confluence = 2
    trend_threshold = 0.0
    mr_threshold = 0.2
    min_roc = None


def test_cli_filter_args_take_precedence(monkeypatch):
    monkeypatch.setattr(cli, "load_settings", lambda config: DummySettings())

    captured = {}

    def fake_strategy_scan(args):
        captured["min_confluence"] = args.min_confluence
        captured["trend_threshold"] = args.trend_threshold
        captured["mr_threshold"] = args.mr_threshold
        captured["min_roc"] = args.min_roc
        return 0

    monkeypatch.setattr(cli, "run_strategy_scan", fake_strategy_scan)
    monkeypatch.setattr(cli, "run_opportunity_scan", lambda args: 0)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "tvscreener.cli",
            "--min-confluence",
            "5",
            "--trend-threshold",
            "0.5",
            "--mr-threshold",
            "0.7",
            "--min-roc",
            "0.3",
        ],
    )

    exit_code = cli.main()

    assert exit_code == 1  # no results, so main returns 1
    assert captured == {
        "min_confluence": 5.0,
        "trend_threshold": 0.5,
        "mr_threshold": 0.7,
        "min_roc": 0.3,
    }
