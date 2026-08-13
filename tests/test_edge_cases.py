from screening_ai.robust_flow import detect_edge_case


def test_missing():

    assert detect_edge_case("", 1.0) == "missing"


def test_poor_audio():

    assert detect_edge_case("hello", 0.4) == "poor_audio"