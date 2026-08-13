from .analyzer import ResponseAnalyzer

from .decision_engine import DecisionEngine

from .state_manager import ConversationState


class FollowupEngine:

    def __init__(self):

        self.analyzer = ResponseAnalyzer()

        self.decision = DecisionEngine()

        self.state = ConversationState()

    def process(self, answer):

        analysis = self.analyzer.analyze(answer)

        question = self.decision.decide(

            analysis,

            self.state

        )

        return {

            "quality": analysis["quality"],

            "followup": question

        }

    def next_question(self):

        self.state.reset()