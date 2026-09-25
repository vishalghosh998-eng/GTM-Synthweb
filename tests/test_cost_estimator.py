from src.cost_estimator import estimate_linear

def test_unknown_cost_is_explicit():
    result=estimate_linear(10, None, None)
    assert result.unknowns

def test_linear_estimate():
    result=estimate_linear(10, 0.1, 0.2)
    assert result.low == 1.0
    assert result.high == 2.0
