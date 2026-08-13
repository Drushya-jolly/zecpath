import json


ROLE_WEIGHTS = {

    "devops engineer": {

        "skills": 0.35,
        "experience": 0.30,
        "education": 0.10,
        "semantic": 0.25
    },

    "software engineer": {

        "skills": 0.30,
        "experience": 0.25,
        "education": 0.15,
        "semantic": 0.30
    }
}


def get_role_weights(role):

    role = role.lower()

    return ROLE_WEIGHTS.get(

        role,

        {
            "skills": 0.30,
            "experience": 0.25,
            "education": 0.15,
            "semantic": 0.30
        }
    )


def calculate_skill_score(

    candidate_skills,

    jd_skills

):

    if len(jd_skills) == 0:

        return 0

    matched = 0

    for skill in jd_skills:

        if skill.lower() in [

            s.lower()

            for s

            in candidate_skills

        ]:

            matched += 1

    return round(

        (matched / len(jd_skills))

        * 100,

        2
    )


def calculate_ats_score(

    skill_score,

    experience_score,

    education_score,

    semantic_score,

    role

):

    weights = get_role_weights(
        role
    )

    final_score = (

        skill_score
        *
        weights["skills"]

        +

        experience_score
        *
        weights["experience"]

        +

        education_score
        *
        weights["education"]

        +

        semantic_score
        *
        weights["semantic"]
    )

    return round(
        final_score,
        2
    )


def generate_explanation(

    skill_score,

    experience_score,

    education_score,

    semantic_score

):

    return {

        "skill_match":
        f"{skill_score}%",

        "experience_relevance":
        f"{experience_score}%",

        "education_alignment":
        f"{education_score}%",

        "semantic_similarity":
        f"{semantic_score}%"
    }


def save_ats_score(

    data,

    output_path

):

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
