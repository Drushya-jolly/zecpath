from screening_ai.behavior_report import generate_behavior_report


def test_behavior():

    result = generate_behavior_report(

        "I am confident and experienced in Python.",

        5

    )

    assert "confidence" in result

    assert "sentiment" in result

    assert "behavior_flags" in result

    assert result["communication_strength"] in [

        "Strong",

        "Moderate",

        "Weak"

    ]