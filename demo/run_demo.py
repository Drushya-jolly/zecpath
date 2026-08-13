from screening_ai.report_generator import generate_screening_report


def run_demo():

    candidate_id = "C1001"
    job_id = "J2001"

    answers = [

        {
            "question_id": "Q1",
            "category": "experience",
            "original_answer": "I have 3 years experience in Python.",
            "structured_answer": {
                "experience_years": 3
            },
            "is_missing": False,
            "is_vague": False
        },

        {
            "question_id": "Q2",
            "category": "skills",
            "original_answer": "Python SQL Django",
            "structured_answer": {
                "skills": [
                    "Python",
                    "SQL",
                    "Django"
                ]
            },
            "is_missing": False,
            "is_vague": False
        },

        {
            "question_id": "Q3",
            "category": "salary",
            "original_answer": "6 LPA",
            "structured_answer": {
                "salary": "6 LPA"
            },
            "is_missing": False,
            "is_vague": False
        },

        {
            "question_id": "Q4",
            "category": "availability",
            "original_answer": "I can join immediately.",
            "structured_answer": {
                "availability": "Immediate"
            },
            "is_missing": False,
            "is_vague": False
        },

        {
            "question_id": "Q5",
            "category": "experience",
            "original_answer": "I don't know.",
            "structured_answer": {
                "experience_years": None
            },
            "is_missing": False,
            "is_vague": True
        }

    ]

    scores = [

        {
            "question_id": "Q1",
            "final_score": 90
        },

        {
            "question_id": "Q2",
            "final_score": 88
        },

        {
            "question_id": "Q3",
            "final_score": 84
        },

        {
            "question_id": "Q4",
            "final_score": 86
        },

        {
            "question_id": "Q5",
            "final_score": 45
        }

    ]

    behavior_reports = [

        {
            "communication_strength": "Strong"
        },

        {
            "communication_strength": "Strong"
        },

        {
            "communication_strength": "Strong"
        },

        {
            "communication_strength": "Strong"
        },

        {
            "communication_strength": "Weak"
        }

    ]

    report = generate_screening_report(
        candidate_id,
        job_id,
        answers,
        scores,
        behavior_reports
    )

    print("\n========== AI SCREENING REPORT ==========\n")

    print(report)


if __name__ == "__main__":
    run_demo()