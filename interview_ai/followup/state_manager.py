class ConversationState:

    def __init__(self):

        self.previous_questions = []

        self.previous_answers = []

        self.followup_count = 0

        self.max_followups = 2

        self.used_followups = []

    def reset(self):

        self.followup_count = 0

        self.used_followups.clear()