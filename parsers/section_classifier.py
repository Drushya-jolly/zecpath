import json
from parsers.resume_parser import extract_resume
from parsers.resume_parser import clean_resume_text

# Common Resume Headings
SECTION_HEADINGS = {

    "contact": [
        "contact",
        "personal information"
    ],

    "career_objective": [
        "career objective",
        "objective",
        "summary",
        "profile summary"
    ],

    "skills": [
        "skills",
        "technical skills",
        "core skills"
    ],

    "education": [
        "education",
        "academic qualification"
    ],

    "experience": [
        "experience",
        "work experience",
        "employment history"
    ],

    "projects": [
        "projects",
        "academic projects"
    ],

    "certifications": [
        "certifications",
        "licenses"
    ]
}


# Resume Segmentation
def segment_resume(file_path):

    text = extract_resume(file_path)

    text = clean_resume_text(text)

    lines = text.splitlines()

    segmented_sections = {}

    current_section = "other"

    segmented_sections[current_section] = []

    for line in lines:

        cleaned_line = line.strip().lower()

        found_section = False

        # Detect Headings
        for section, keywords in SECTION_HEADINGS.items():

            if any(keyword in cleaned_line for keyword in keywords):

                current_section = section

                segmented_sections[current_section] = []

                found_section = True

                break

        if not found_section:

            segmented_sections[current_section].append(line)

    return segmented_sections


# Save Output
def save_output(data, output_path):

    with open(output_path, "w") as file:

        json.dump(data, file, indent=4)