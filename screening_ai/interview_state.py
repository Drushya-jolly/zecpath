def create_state():

    return {

        "phase": "Introduction",

        "question_id": 1,

        "responses": [],

        "follow_up": False

    }


def update_state(state,
                 answer):

    state["responses"].append(answer)

    state["question_id"] += 1

    if state["question_id"] <= 2:

        state["phase"] = "Core HR"

    elif state["question_id"] <= 6:

        state["phase"] = "Role Evaluation"

    else:

        state["phase"] = "Closing"

    return state