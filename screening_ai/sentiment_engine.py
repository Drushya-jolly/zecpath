POSITIVE_WORDS = [
    "good",
    "great",
    "confident",
    "strong",
    "experienced",
    "skilled",
    "excellent",
    "happy"
]

NEGATIVE_WORDS = [
    "bad",
    "weak",
    "problem",
    "difficult",
    "struggle",
    "confused",
    "poor"
]


def detect_sentiment(text):

    text = text.lower()

    positive = sum(word in text for word in POSITIVE_WORDS)

    negative = sum(word in text for word in NEGATIVE_WORDS)

    if positive > negative:

        sentiment = "Positive"

        score = min(positive / 5, 1.0)

    elif negative > positive:

        sentiment = "Negative"

        score = min(negative / 5, 1.0)

    else:

        sentiment = "Neutral"

        score = 0.5

    return {
        "sentiment": sentiment,
        "sentiment_score": round(score, 2)
    }