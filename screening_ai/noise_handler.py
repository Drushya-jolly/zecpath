import re


def clean_noise(text):

    # Remove background noise markers
    text = re.sub(r"\[.*?\]", "", text)

    # Remove repeated characters
    text = re.sub(r"(.)\1{2,}", r"\1", text)

    return text.strip()


def detect_language_mix(text):

    local_words = [
        "hai",
        "enna",
        "chetta",
        "bhai"
    ]

    text = text.lower()

    return any(word in text for word in local_words)