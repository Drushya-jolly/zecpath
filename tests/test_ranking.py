from ranking.rank_candidates import (
    rank_candidates
)

import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]

def test_ranking():

    candidates = [

        {
            "candidate_score": 80
        },

        {
            "candidate_score": 60
        }
    ]

    result = rank_candidates(
        candidates
    )

    assert result[0][
        "candidate_score"
    ] == 80