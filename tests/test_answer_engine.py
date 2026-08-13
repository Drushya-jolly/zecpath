from screening_ai.answer_engine import process_answer


def test_answer_processing():

    answer = "I have 2 years experience in Python and SQL."

    result = process_answer(
        "Q1",
        "experience",
        answer
    )

    assert result["structured_answer"]["experience_years"] == 2
    assert result["category"] == "experience"
    assert result["is_missing"] is False

def test_skill_extraction():

    answer = "Python, SQL and Django"

    result = process_answer(
        "Q2",
        "skills",
        answer
    )

    assert "Python" in result["structured_answer"]["skills"]