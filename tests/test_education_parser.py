from parsers.education_parser import (
    extract_education,
    extract_certifications
)

import json
import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]

def test_education_parser():

    with open(
        TEST_SECTIONS,
        "r"
    ) as file:

        segmented_resume = json.load(file)

    education = extract_education(
        segmented_resume
    )

    assert "degree" in education

    assert "field_of_study" in education

    assert "institution" in education


def test_certification_parser():

    with open(
        TEST_SECTIONS,
        "r"
    ) as file:

        segmented_resume = json.load(file)

    certifications = extract_certifications(
        segmented_resume
    )

    assert len(certifications) > 0