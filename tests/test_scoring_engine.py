from screening_ai.answer_engine import process_answer
from screening_ai.scoring_engine import score_answer


def test_scoring():

    answer = process_answer(
        "Q1",
        "experience",
        "I have 2 years of experience."
    )

    result = score_answer(answer)

    assert result["final_score"] > 70
    assert result["decision"] == "Pass"