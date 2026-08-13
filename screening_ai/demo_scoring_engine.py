from screening_ai.answer_engine import process_answer
from screening_ai.scoring_engine import screening_scoring_pipeline

answers = [

    process_answer(
        "Q1",
        "experience",
        "I have 3 years of experience in Python."
    ),

    process_answer(
        "Q2",
        "skills",
        "Python, SQL"
    ),

    process_answer(
        "Q3",
        "salary",
        "Maybe around 8 LPA."
    ),

    process_answer(
        "Q4",
        "availability",
        "I can join after 30 days."
    ),

    process_answer(
        "Q5",
        "experience",
        "I don't know."
    ),

    process_answer(
        "Q6",
        "experience",
        ""
    )

]

result = screening_scoring_pipeline(answers)

print(result)