import random

from .templates import FOLLOWUPS


class DecisionEngine:

    def decide(self, analysis, state):

        if state.followup_count >= state.max_followups:

            return None

        if analysis["quality"] in ["empty","too_short"]:

            level = "clarification"

        elif analysis["is_vague"]:

            level = "clarification"

        elif analysis["quality"] == "basic":

            level = "deep"

        elif analysis["is_confident"]:

            level = "scenario"

        else:

            level = "deep"

        available = [

            q

            for q in FOLLOWUPS[level]

            if q not in state.used_followups

        ]

        if not available:

            state.used_followups.clear()

            available = FOLLOWUPS[level]

        question = random.choice(available)

        state.used_followups.append(question)

        state.followup_count += 1

        return question