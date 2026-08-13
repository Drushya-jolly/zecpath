import json

from parsers.skill_extractor import extract_skills

import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]


def test_skill_extraction():

    with open(
        TEST_SECTIONS,
        "r"
    ) as file:

        segmented_resume = json.load(file)

    skills = extract_skills(segmented_resume)

    assert len(skills) > 0