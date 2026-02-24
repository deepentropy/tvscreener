import pandas as pd

from tvscreener.score import ScoringEngine


def test_calculate_confluence_infers_direction_without_ensemble_score():
    engine = ScoringEngine(timeframes=["15"], tf_weights={"15": 1.0})

    df = pd.DataFrame({"Recommend All|15": [1.0, -1.0]})
    result = engine.calculate_confluence(df)

    assert result["DIRECTION"].tolist() == ["long", "short"]
