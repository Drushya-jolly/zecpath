import glob
from parsers.section_classifier import segment_resume

TEST_RESUME = glob.glob("data/resumes/*.pdf")

def test_section_detection():

    assert len(TEST_RESUME) > 0

    data = segment_resume(TEST_RESUME[0])

    assert "skills" in data