import re


def extract_experience(text):
    match = re.search(r"(\d+)\s+(?:year|years)", text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def extract_salary(text):
    match = re.search(
        r"(₹?\s?\d+(?:\.\d+)?)\s*(lpa|lakhs?|k|per annum)?",
        text,
        re.IGNORECASE,
    )
    return match.group().strip() if match else None


def extract_availability(text):
    if re.search(r"immediate", text, re.IGNORECASE):
        return "Immediate"

    match = re.search(r"(\d+)\s*(day|days|month|months)", text, re.IGNORECASE)
    if match:
        return match.group()

    return None


def extract_skills(text):
    """
    Extract skills from answers like:
    'I know Python, SQL, Java and Django'
    """
    text = re.sub(r"(?i)i know|i have experience in|my skills are|skills include", "", text)

    separators = r",|and|/"

    parts = re.split(separators, text)

    skills = []

    for part in parts:
        skill = part.strip(" .")
        if len(skill) > 1:
            skills.append(skill)

    return skills


def detect_vague(answer):

    answer = answer.lower().strip()

    vague_words = [
        "maybe",
        "perhaps",
        "around",
        "approximately",
        "not sure",
        "don't know",
        "dont know",
        "no idea",
        "can't say",
        "cannot say"
    ]

    return any(word in answer for word in vague_words)


def detect_missing(text):
    return len(text.strip()) == 0


def process_answer(question_id, question_category, answer):

    result = {
        "question_id": question_id,
        "category": question_category,
        "original_answer": answer,
        "structured_answer": None,
        "off_topic": False,
        "is_vague": detect_vague(answer),
        "is_missing": detect_missing(answer),
    }

    if question_category == "experience":
        result["structured_answer"] = {
            "experience_years": extract_experience(answer)
        }

    elif question_category == "skills":
        result["structured_answer"] = {
            "skills": extract_skills(answer)
        }

    elif question_category == "salary":
        result["structured_answer"] = {
            "salary": extract_salary(answer)
        }

    elif question_category == "availability":
        result["structured_answer"] = {
            "availability": extract_availability(answer)
        }

    else:
        result["structured_answer"] = {
            "text": answer
        }

    return result