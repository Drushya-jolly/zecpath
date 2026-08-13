from screening_ai.answer_engine import process_answer
from screening_ai.scoring_engine import screening_scoring_pipeline


def simulate_test():

    answers = [

        process_answer(
            "Q1",
            "experience",
            "I have 2 years of Python experience."
        ),

        process_answer(
            "Q2",
            "skills",
            "Python, SQL"
        ),

        process_answer(
            "Q3",
            "salary",
            "6 LPA"
        )

    ]

    result = screening_scoring_pipeline(answers)

    return result


if __name__ == "__main__":

    print(simulate_test())