# -------------------------------
# Scoring Weights
# -------------------------------

WEIGHTS = {
    "clarity": 0.25,
    "relevance": 0.30,
    "completeness": 0.25,
    "consistency": 0.20
}


# -------------------------------
# Clarity
# -------------------------------

def score_clarity(answer):

    if answer["is_missing"]:
        return 0.0

    if answer["is_vague"]:
        return 0.5

    return 1.0


# -------------------------------
# Relevance
# -------------------------------

def score_relevance(answer):

    if answer["is_missing"]:
        return 0.0

    return 1.0


# -------------------------------
# Completeness
# -------------------------------

def score_completeness(answer):

    category = answer["category"]
    data = answer["structured_answer"]

    if category == "experience":
        return 1.0 if data.get("experience_years") else 0.0

    elif category == "skills":
        return 1.0 if data.get("skills") else 0.0

    elif category == "salary":
        return 1.0 if data.get("salary") else 0.0

    elif category == "availability":
        return 1.0 if data.get("availability") else 0.0

    return 0.5


# -------------------------------
# Consistency
# -------------------------------

def score_consistency(answer):

    if answer["is_missing"]:
        return 0.0

    if answer["is_vague"]:
        return 0.5

    return 1.0


# -------------------------------
# Per Question Score
# -------------------------------

def score_answer(answer):

    clarity = score_clarity(answer)
    relevance = score_relevance(answer)
    completeness = score_completeness(answer)
    consistency = score_consistency(answer)

    final_score = (
        clarity * WEIGHTS["clarity"] +
        relevance * WEIGHTS["relevance"] +
        completeness * WEIGHTS["completeness"] +
        consistency * WEIGHTS["consistency"]
    ) * 100

    if final_score >= 70:
        decision = "Pass"
    elif final_score >= 50:
        decision = "Review"
    else:
        decision = "Reject"

    return {
        "question_id": answer["question_id"],
        "scores": {
            "clarity": clarity,
            "relevance": relevance,
            "completeness": completeness,
            "consistency": consistency
        },
        "final_score": round(final_score, 2),
        "decision": decision
    }


# -------------------------------
# Aggregate Score
# -------------------------------

def aggregate_scores(results):

    if not results:
        return 0

    total = sum(item["final_score"] for item in results)

    return round(total / len(results), 2)


# -------------------------------
# Screening Pipeline
# -------------------------------

def screening_scoring_pipeline(answers):

    scored_answers = []

    for answer in answers:
        scored_answers.append(score_answer(answer))

    overall_score = aggregate_scores(scored_answers)

    if overall_score >= 70:
        decision = "Pass"
    elif overall_score >= 50:
        decision = "Review"
    else:
        decision = "Reject"

    return {
        "screening_score": overall_score,
        "decision": decision,
        "details": scored_answers
    }