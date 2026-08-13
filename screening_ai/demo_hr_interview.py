from screening_ai.hr_qn_generator import generate_questions
from screening_ai.interview_state import create_state
from screening_ai.interview_state import update_state





# -------------------------
# Candidate Type
# -------------------------

while True:

    candidate_type = input(
        "\nAI : Are you a Fresher or Experienced?\nCandidate : "
    ).lower().strip()

    if candidate_type in ["fresher", "experienced"]:
        break

    print("AI : Please answer either Fresher or Experienced.")


# -------------------------
# Role Type
# -------------------------

while True:

    role_type = input(
        "\nAI : Are you applying for a Technical or Non-Technical role?\nCandidate : "
    ).lower().strip()

    if role_type in ["technical", "non-technical"]:
        break

    print("AI : Please answer either Technical or Non-Technical.")


# -------------------------
# Generate Questions
# -------------------------

questions = generate_questions(
    candidate_type,
    role_type
)

state = create_state()


print("\nInterview Started...\n")


for question in questions:

    print(f"\nPhase : {state['phase']}")

    print("\nAI :", question)

    answer = input("Candidate : ")

    state = update_state(
        state,
        answer
    )


print("\n" + "=" * 50)
print("Interview Completed")
print("=" * 50)

print(f"\nCandidate Type : {candidate_type.title()}")
print(f"Role           : {role_type.title()}")
print(f"Questions Asked: {len(questions)}")
print(f"Responses Saved: {len(state['responses'])}")
print(f"Current Phase  : {state['phase']}")
print(f"Follow Up      : {state['follow_up']}")