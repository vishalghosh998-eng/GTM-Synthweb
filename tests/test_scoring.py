from src.scoring import score_dimensions

def test_unknown_is_zero():
    assert score_dimensions({"icp_fit": 100, "service_fit": None}, {"icp_fit": 20, "service_fit": 20}) == 20

def test_weighted_score():
    assert score_dimensions({"icp_fit": 50, "service_fit": 50}, {"icp_fit": 20, "service_fit": 20}) == 20
