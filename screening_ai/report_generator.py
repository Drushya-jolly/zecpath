# -------------------------------
# AI Screening Report Generator
# -------------------------------

def generate_screening_report(
    candidate_id,
    job_id,
    answers,
    scores,
    behavior_reports
):

    strengths = []
    risks = []
    missing_data = []
    key_answers = []

    salary = None
    availability = None
    confirmed_skills = set()

    # -------------------------------
    # Process Each Question
    # -------------------------------

    for answer, score, behavior in zip(
        answers,
        scores,
        behavior_reports
    ):

        # ---------------------------
        # Key Answers
        # ---------------------------

        key_answers.append({

            "question_id": answer["question_id"],

            "answer": answer["original_answer"]

        })

        # ---------------------------
        # Strengths
        # ---------------------------

        if score["final_score"] >= 80:

            strengths.append(
                f"Strong response for {answer['question_id']}"
            )

        elif (
            score["final_score"] < 50 or
            behavior["communication_strength"] == "Weak"
        ):

            risks.append(
                f"Weak response for {answer['question_id']}"
            )

        # ---------------------------
        # Missing Data
        # ---------------------------

        if answer["is_missing"]:

            missing_data.append(

                f"Missing answer for {answer['question_id']}"

            )

        elif answer["is_vague"]:

            missing_data.append(

                f"Vague answer for {answer['question_id']}"

            )

        # ---------------------------
        # Extract Highlights
        # ---------------------------

        structured = answer["structured_answer"]

        if answer["category"] == "salary":

            salary = structured.get("salary")

        elif answer["category"] == "availability":

            availability = structured.get("availability")

        elif answer["category"] == "skills":

            for skill in structured.get("skills", []):

                confirmed_skills.add(skill)

    # -------------------------------
    # Final Score
    # -------------------------------

    final_score = round(

        sum(s["final_score"] for s in scores) /

        len(scores),

        2

    ) if scores else 0

    # -------------------------------
    # Decision
    # -------------------------------

    if final_score >= 70:

        decision = "Proceed"

    elif final_score >= 50:

        decision = "Review"

    else:

        decision = "Reject"

    # -------------------------------
    # Final Report
    # -------------------------------

    return {

        "candidate_id": candidate_id,

        "job_id": job_id,

        "final_score": final_score,

        "decision": decision,

        "summary": {

            "strengths": strengths,

            "risks": risks,

            "missing_data": missing_data

        },

        "highlights": {

            "salary_expectation": salary,

            "availability": availability,

            "confirmed_skills": list(confirmed_skills)

        },

        "answers": key_answers

    }