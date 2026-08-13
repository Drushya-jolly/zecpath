RETRY_MESSAGES = {

    "silence": "Sorry, I didn't hear anything. Could you answer again?",

    "confusion": "Let me explain the question once more.",

    "repeat": "Could you provide a little more detail?"

}


def detect_issue(answer):

    if not answer.strip():

        return "silence"

    if len(answer.split()) < 2:

        return "confusion"

    words = answer.lower().split()

    if len(set(words)) < len(words) / 2:

        return "repeat"

    return "valid"


def handle_response(engine, answer):

    issue = detect_issue(answer)

    if issue == "silence":

        print(RETRY_MESSAGES["silence"])

        engine.handle_silence()

    elif issue == "confusion":

        print(RETRY_MESSAGES["confusion"])

        engine.handle_confusion()

    elif issue == "repeat":

        print(RETRY_MESSAGES["repeat"])

        engine.handle_repeat()

    else:

        engine.next()