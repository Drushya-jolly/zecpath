import re
import json
import fitz

def extract_pdf_text(file_path):

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    return text
    

# Skill Keywords
SKILLS = [
    "python",
    "java",
    "sql",
    "react",
    "mongodb",
    "nodejs",
    "linux",
    "azure",
    "angular",
    ".net",
    "bash",
    "ci/cd"
]

# Role Keywords
ROLES = [
    "software development engineer",
    "software engineer",
    "software developer",

    "developer",
    "java developer",
    "python developer",

    "mern stack developer",
    "frontend developer",
    "backend developer",
    "full stack developer",

    "devops engineer",
    "cloud engineer",

    ".net core engineer",
    ".net developer",

    "data analyst",
    "data scientist",

    "machine learning engineer",
    "ai engineer"
]

# Parse Job Description
def parse_job_description(file_path):

    if file_path.endswith(".pdf"):

        text = extract_pdf_text(file_path)

    else:

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

    normalized_text = normalize_text(text)

    

    extracted_skills = extract_skills(normalized_text)

    extracted_roles = extract_roles(normalized_text)

    experience = extract_experience(normalized_text)

    education = extract_education(normalized_text)

    jd_object = {
        "company": extract_company_name(normalized_text),
        "role": extracted_roles,
        "skills": extracted_skills,
        "experience": experience,
        "education": education
    }

    return jd_object


# Normalize JD Text
def normalize_text(text):

    text = text.lower()

    text = re.sub(r"\s+", " ", text)

    return text.strip()

#Extract company name

def extract_company_name(text):

    company_pattern = r"company name\s*[:\-]\s*(.*?)\s*(detailed instructions|we currently have|role|job)"

    match = re.search(company_pattern, text)

    if match:
        return match.group(1).strip()

    return "Not Specified"


# Extract Skills
def extract_skills(text):

    detected_skills = []

    for skill in SKILLS:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills


# Extract Roles
def extract_roles(text):

    detected_roles = []

    for role in ROLES:

        if role in text:

            detected_roles.append(role)

    if detected_roles:

        return detected_roles

    role_pattern = r"\b([a-zA-Z\s]+(?:developer|engineer|analyst|scientist))\b"

    matches = re.findall(
        role_pattern,
        text
    )

    cleaned_matches = []

    for match in matches:

        match = match.strip()

        if len(match.split()) <= 5:

            cleaned_matches.append(match)

    return list(set(cleaned_matches))


# Extract Experience
def extract_experience(text):

    sentences = re.split(r'[.\n]', text)

    patterns = [
        r'(\d+\+?\s*(?:-\s*\d+\+?)?\s*years?)'
    ]

    for sentence in sentences:

        sentence = sentence.lower()

        # Skip sentences that are about bonds/commitments
        if any(word in sentence for word in [
            "bond",
            "service bond",
            "commitment",
            "contract",
            "probation"
        ]):
            continue

        # Only consider sentences mentioning experience
        if "experience" not in sentence:
            continue

        for pattern in patterns:

            match = re.search(pattern, sentence)

            if match:
                return match.group(1)

    return "Not Specified"


# Extract Education
def extract_education(text):

    education_patterns = [
        "b.tech",
        "btech",
        "b.e",
        "m.tech",
        "mtech",
        "m.e",
        "bachelor",
        "computer science"
    ]

    detected = []

    text = text.lower()

    for edu in education_patterns:
        if edu in text:
            if edu in ["b.tech", "btech", "b.e"]:
                detected.append("B.Tech")
            elif edu in ["m.tech", "mtech", "m.e"]:
                detected.append("M.Tech")
            else:
                detected.append(edu.title())

    return list(set(detected))


# Save Output
def save_jd_output(data, output_path):

    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)