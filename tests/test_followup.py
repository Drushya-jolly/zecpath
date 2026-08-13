from interview_ai.followup.followup_engine import FollowupEngine

engine = FollowupEngine()

print("Type 'next' for a new interview question.")
print("Type 'exit' to quit.\n")

while True:

    answer = input("Candidate: ")

    if answer.lower() == "exit":

        break

    if answer.lower() == "next":

        engine.next_question()

        print("---- New Interview Question ----\n")

        continue

    result = engine.process(answer)

    print()

    print("Quality :", result["quality"])

    if result["followup"]:

        print("AI      :", result["followup"])

    else:

        print("AI      : Moving to the next interview question.")

    print()