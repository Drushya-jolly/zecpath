import glob

from scoring.ats_score import (
    calculate_ats_score
)


TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]


def test_ats_score():

    score = calculate_ats_score(

        80,
        70,
        90,
        85,

        "software engineer"
    )

    assert score > 0