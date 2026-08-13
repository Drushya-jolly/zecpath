from screening_ai.improved_intent import improved_intent_classification


def test_intent():

    result = improved_intent_classification(

        "I worked as a Python developer for two years."

    )

    assert result == "experience"