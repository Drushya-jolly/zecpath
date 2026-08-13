from screening_ai.error_framework import fallback_strategy


def detect_edge_case(answer, confidence=1.0):
    """
    Detect common edge cases during AI interview.
    """

    if not answer or not answer.strip():
        return "missing"

    if confidence < 0.6:
        return "poor_audio"

    answer = answer.lower()

    # Language mixing
    local_words = ["hai", "enna", "chetta", "bhai"]

    if any(word in answer for word in local_words):
        return "language_mix"

    # Hesitation / unclear
    if any(word in answer.split() for word in ["um", "uh"]):
        return "unclear"

    # Very short answer
    if len(answer.split()) < 2:
        return "incomplete"

    return "valid"


def handle_edge_case(answer, confidence=1.0, retry_count=0):

    issue = detect_edge_case(answer, confidence)

    if issue == "valid":
        return {
            "issue": issue,
            "action": "continue"
        }

    return {
        "issue": issue,
        "action": fallback_strategy(issue, retry_count)
    }