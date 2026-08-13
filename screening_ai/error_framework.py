ERROR_RESPONSES = {

    "missing":
        "I didn't receive your response. Could you please answer?",

    "poor_audio":
        "The audio isn't clear. Could you please repeat?",

    "language_mix":
        "Would you like to continue in English?",

    "unclear":
        "Could you explain your answer more clearly?",

    "incomplete":
        "Could you provide a little more detail?",

    "fallback":
        "Let's move to the next question."
}


def get_error_response(issue):

    return ERROR_RESPONSES.get(issue,
                               ERROR_RESPONSES["fallback"])


def fallback_strategy(issue, retry_count):

    if retry_count >= 2:
        return "skip_question"

    if issue in ["missing", "poor_audio"]:
        return "retry"

    if issue == "language_mix":
        return "switch_language"

    if issue in ["unclear", "incomplete"]:
        return "clarify"

    return "continue"