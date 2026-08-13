UNCERTAINTY_WORDS = [
    "maybe",
    "not sure",
    "probably",
    "i think",
    "don't know"
]


def detect_uncertainty(text):

    text = text.lower()

    return any(word in text for word in UNCERTAINTY_WORDS)


def detect_contradiction(text):

    text = text.lower()

    CONTRADICTION_WORDS = [
        "however",
        "but",
        "although",
        "yet"
    ]

    return any(word in text for word in CONTRADICTION_WORDS)