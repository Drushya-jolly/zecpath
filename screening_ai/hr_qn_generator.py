from screening_ai.hr_qn_bank import HR_QUESTION_BANK


def generate_questions(candidate_type, role_type):

    questions = []

    questions.extend(
        HR_QUESTION_BANK["introduction"][candidate_type]
    )

    questions.extend(
        HR_QUESTION_BANK["career_journey"][candidate_type]
    )

    questions.extend(
        HR_QUESTION_BANK["strengths_weaknesses"]["common"]
    )

    questions.extend(
        HR_QUESTION_BANK["teamwork"]["common"]
    )

    questions.extend(
        HR_QUESTION_BANK["career_goals"]["common"]
    )

    questions.extend(
        HR_QUESTION_BANK["availability"]["common"]
    )

    questions.extend(
        HR_QUESTION_BANK["role_based"][role_type]
    )

    return questions