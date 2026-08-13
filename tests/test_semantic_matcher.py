import json
import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]


from parsers.semantic_matcher import (
    semantic_match
)


def test_semantic_matcher():

    with open(
        TEST_SECTIONS,
        "r"
    ) as file:

        resume = json.load(file)

    with open(
        "data/parsed_jd/jd_output.json",
        "r"
    ) as file:

        jd = json.load(file)

    result = semantic_match(
        resume,
        jd
    )

    assert (
        "overall_similarity"
        in result
    )