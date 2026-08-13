import json

from screening_ai.conversation_engine import ConversationStateMachine

from screening_ai.error_handling import handle_response


with open("screening_ai/conversation_flow.json") as f:

    flow = json.load(f)

engine = ConversationStateMachine(flow)

while not engine.is_end():

    print()

    print("AI :", engine.get_question())

    answer = input("Candidate : ")

    handle_response(engine, answer)

print()

print("Interview Completed.")