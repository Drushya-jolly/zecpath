import json

from parsers.experience_parser import (
    extract_experience
)

import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]

def test_experience_parser():

    with open(
        TEST_SECTIONS,
        "r"
    ) as file:

        data = json.load(file)

    experience = extract_experience(data)

    assert "companies" in experience