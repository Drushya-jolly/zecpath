import json


# Master Skill Dictionary
SKILL_DICTIONARY = {

    "python": ["python"],

    "sql": ["sql", "mysql", "postgresql"],

    "java": ["java"],

    "javascript": ["javascript", "js"],

    "react": ["react"],

    "nodejs": ["nodejs", "node.js"],

    "mongodb": ["mongodb"],

    "git": ["git"],

    "github": ["github"],

    "linux": ["linux"],

    "cloud": ["cloud", "aws", "azure", "gcp"],

    "cicd": ["cicd", "ci/cd"],

    "rag": ["rag"],

    "langchain": ["langchain"]
}


SOFT_SKILLS = [

    "adaptability",

    "team collaboration",

    "discipline",

    "communication",

    "leadership"
]


def extract_skills(segmented_resume):

    extracted_skills = {}

    # Search technical skills
    for section, content in segmented_resume.items():

        section_text = " ".join(content).lower()

        for skill, aliases in SKILL_DICTIONARY.items():

            for alias in aliases:

                if alias in section_text:

                    if section == "skills":

                        confidence = 1.0

                    elif section == "projects":

                        confidence = 0.8

                    else:

                        confidence = 0.6

                    extracted_skills[skill] = confidence

                    break

    return extracted_skills


def extract_soft_skills(segmented_resume):

    detected = []

    all_text = ""

    for content in segmented_resume.values():

        all_text += " ".join(content).lower()

    for skill in SOFT_SKILLS:

        if skill in all_text:

            detected.append(skill)

    return detected


def save_skill_output(data, output_path):

    with open(output_path, "w") as file:

        json.dump(data, file, indent=4)