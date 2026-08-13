INTENT_KEYWORDS = {

    "introduction": [
        "introduce",
        "my name",
        "background",
        "graduate"
    ],

    "experience": [
        "experience",
        "worked",
        "years",
        "developer",
        "project"
    ],

    "skills": [
        "python",
        "java",
        "sql",
        "django",
        "flask",
        "skills"
    ],

    "salary": [
        "salary",
        "ctc",
        "lpa",
        "expected"
    ],

    "availability": [
        "join",
        "notice",
        "immediate",
        "days"
    ]

}


def improved_intent_classification(text):

    text = text.lower()

    scores = {}

    for intent, words in INTENT_KEYWORDS.items():

        scores[intent] = sum(
            word in text
            for word in words
        )

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "unknown"

    return best