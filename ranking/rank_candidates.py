import json


SHORTLIST_THRESHOLD = 80
REVIEW_THRESHOLD = 45


def classify_candidate(score):

    if score >= SHORTLIST_THRESHOLD:

        return "Shortlist"

    elif score >= REVIEW_THRESHOLD:

        return "Review"

    return "Reject"


def rank_candidates(candidate_list):

    ranked_candidates = sorted(

        candidate_list,

        key=lambda x: x["candidate_score"],

        reverse=True
    )

    for rank, candidate in enumerate(

        ranked_candidates,

        start=1
    ):

        candidate["rank"] = rank

        candidate["status"] = (

            classify_candidate(

                candidate[
                    "candidate_score"
                ]
            )
        )

    return ranked_candidates


def save_ranked_candidates(

    data,

    output_path

):

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )