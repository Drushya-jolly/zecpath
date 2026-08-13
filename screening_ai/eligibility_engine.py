import json
import os


RULE_FILE = "data/config/eligibility_rules.json"


def load_rules(role):

    default_rules = {
        "minimum_ats_score": 50,
        "mandatory_skills": [],
        "minimum_experience": 0,
        "required_education": []
    }

    if not os.path.exists(RULE_FILE):
        print("Eligibility rules file not found. Using default rules.")
        return default_rules

    with open(RULE_FILE, "r") as file:
        rules = json.load(file)

    role = role.lower().strip()

    if role in rules:
        print(f"Loaded eligibility rules for '{role}'")
        return rules[role]

    print(f"No eligibility rules found for '{role}'. Using default rules.")
    return default_rules


def evaluate_candidate(candidate_name,
                       role,
                       ats_score,
                       candidate_skills,
                       experience_score,
                       education_score):

    rules = load_rules(role)

    minimum_score = rules["minimum_ats_score"]
    mandatory_skills = rules["mandatory_skills"]

    matched_skills = []

    for skill in mandatory_skills:
        if skill.lower() in [s.lower() for s in candidate_skills]:
            matched_skills.append(skill)

    skill_match = len(matched_skills) == len(mandatory_skills)

    experience_match = experience_score >= rules["minimum_experience"]

    education_match = education_score > 0

    score_match = ats_score >= minimum_score

    if score_match and skill_match and experience_match and education_match:
        decision = "Eligible"

    elif ats_score >= minimum_score - 15:
        decision = "Review"

    else:
        decision = "Rejected"

    return {

        "candidate_name": candidate_name,

        "role": role,

        "ats_score": ats_score,

        "eligibility_status": decision,

        "checks": {

            "score_match": score_match,

            "required_skills": mandatory_skills,

            "matched_skills": matched_skills,

            "mandatory_skills_match": skill_match,

            "experience_match": experience_match,

            "education_match": education_match
        }
    }


def save_eligibility(result, output_path):

    with open(output_path, "w") as file:
        json.dump(result, file, indent=4)