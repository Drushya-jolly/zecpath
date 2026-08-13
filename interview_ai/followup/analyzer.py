LOW_INFO = {
    "ok",
    "okay",
    "yes",
    "no",
    "idk",
    "don't know",
    "not sure",
    "nothing",
    "what"
}


class ResponseAnalyzer:

    VAGUE_WORDS = [
        "maybe",
        "probably",
        "kind of",
        "i think",
        "not sure"
    ]

    CONFIDENT_WORDS = [
        "implemented",
        "developed",
        "built",
        "designed",
        "managed",
        "led",
        "optimized",
        "created",
        "successfully"
    ]

    def analyze(self, answer):

        answer = answer.strip()

        lower = answer.lower()

        words = answer.split()

        result = {}

        if not answer:

            result["quality"] = "empty"

        elif len(words) < 4:

            result["quality"] = "too_short"

        elif len(words) < 10:

            result["quality"] = "basic"

        else:

            result["quality"] = "good"

        result["is_low_info"] = lower in LOW_INFO

        result["is_vague"] = any(
            word in lower
            for word in self.VAGUE_WORDS
        )

        result["is_confident"] = any(
            word in lower
            for word in self.CONFIDENT_WORDS
        )

        return result