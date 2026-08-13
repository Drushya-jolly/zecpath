from screening_ai.hr_qn_generator import generate_questions


def test_question_generation():

    questions = generate_questions(
        "fresher",
        "technical"
    )

    assert len(questions) > 0