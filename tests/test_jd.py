from parsers.jd_parser import parse_job_description

import glob
TEST_RESUME = glob.glob("data/resumes/*.pdf")[0]
TEST_SECTIONS = glob.glob("data/candidates/*/sections.json")[0]

def test_jd_parser():

    data = parse_job_description(
        "data/jd_samples/jd_sample.pdf"
    )

    assert "skills" in data