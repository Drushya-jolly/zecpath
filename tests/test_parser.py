import glob
from parsers.resume_parser import extract_resume

TEST_RESUME = glob.glob("data/resumes/*.pdf")

def test_resume_extraction():

    assert len(TEST_RESUME) > 0

    text = extract_resume(TEST_RESUME[0])

    assert len(text) > 0