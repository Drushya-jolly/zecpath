def adaptive_retry_logic(issue, retry_count):

    if issue == "silence":

        if retry_count == 0:
            return "retry"

        elif retry_count == 1:
            return "simplify_question"

        return "skip_question"

    elif issue == "confusion":

        return "clarify"

    elif issue == "repeat":

        return "ask_example"

    return "next"