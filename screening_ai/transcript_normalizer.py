import re

FILLER_WORDS = [
    "um",
    "uh",
    "like",
    "you know",
    "so",
    "i mean",
    "yaah"
]


def normalize_transcript(text):
    """
    Normalize transcript text by removing filler words,
    converting to lowercase, and removing extra spaces.
    """

    text = text.lower()

    for filler in FILLER_WORDS:
        text = re.sub(rf"\b{re.escape(filler)}\b", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()