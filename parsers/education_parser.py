import json
import re


# Degree Normalization
DEGREE_MAP = {

    "b.tech": "B.Tech",
    "btech": "B.Tech",
    "b.e": "B.Tech",

    "m.tech": "M.Tech",
    "mtech": "M.Tech",
    "m.e": "M.Tech",

    "mba": "MBA",
    "mca": "MCA",

    "b.sc": "B.Sc",
    "bsc": "B.Sc",

    "m.sc": "M.Sc",
    "msc": "M.Sc",

    "b.com": "B.Com",
    "bcom": "B.Com",

    "m.com": "M.Com",
    "mcom": "M.Com",

    "bba": "BBA"
}


# Certification Categories
CERT_CATEGORIES = {

    "internet of things": "IoT",
    "iot": "IoT",

    "cloud": "Cloud",
    "aws": "Cloud",
    "azure": "Cloud",
    "gcp": "Cloud",

    "devops": "DevOps",
    "docker": "DevOps",
    "kubernetes": "DevOps",

    "machine learning": "AI",
    "artificial intelligence": "AI",
    "deep learning": "AI",

    "python": "Programming",
    "java": "Programming",

    "data science": "Data",
    "analytics": "Data"
}


def normalize_degree(text):

    return (
        text.lower()
            .replace(".", "")
            .replace("-", "")
            .replace(" ", "")
    )


def extract_education(segmented_resume):

    education_lines = segmented_resume.get(
        "education",
        []
    )

    education_text = " ".join(
        education_lines
    ).lower()

    academic_profile = {

        "degree": [],

        "field_of_study": [],

        "institution": [],

        "graduation_year": []
    }

    # Degree Extraction
    for degree_key, degree_value in DEGREE_MAP.items():

        if degree_key in education_text:

            if degree_value not in academic_profile["degree"]:

                academic_profile[
                    "degree"
                ].append(
                    degree_value
                )

    # Field of Study
    fields = [

        "computer science",
        "information technology",
        "electronics",
        "electrical",
        "mechanical",
        "civil",
        "data science",
        "artificial intelligence",
        "commerce",
        "business administration",
        "finance",
        "accounting"
    ]

    for field in fields:

        if field in education_text:

            academic_profile[
                "field_of_study"
            ].append(
                field.title()
            )

    # Graduation Year
    years = re.findall(

        r"\b(19\d{2}|20\d{2})\b",

        education_text
    )

    academic_profile[
        "graduation_year"
    ] = list(set(years))

    # Institution Extraction
    for line in education_lines:

        line = line.strip()

        if len(line) < 5:
            continue

        if any(
            degree in line.lower()
            for degree in DEGREE_MAP.keys()
        ):
            continue

        if re.search(
            r"\b(19\d{2}|20\d{2})\b",
            line
        ):
            continue

        if "cgpa" in line.lower():
            continue

        if line not in academic_profile[
            "institution"
        ]:

            academic_profile[
                "institution"
            ].append(
                line
            )

    return academic_profile


def extract_certifications(
    segmented_resume
):

    cert_lines = segmented_resume.get(
        "certifications",
        []
    )

    certifications = []

    for cert in cert_lines:

        cert = cert.strip()

        if len(cert) < 3:
            continue

        category = "General"

        for keyword, value in CERT_CATEGORIES.items():

            if keyword in cert.lower():

                category = value

                break

        certifications.append({

            "name": cert,

            "category": category
        })

    return certifications


def calculate_education_relevance(

    academic_profile,

    jd_education

):

    if not jd_education:

        return 0

    # Convert JD education to list if needed
    if not isinstance(
        jd_education,
        list
    ):
        jd_education = [jd_education]

    # Normalize resume degrees
    resume_degrees = [

        normalize_degree(degree)

        for degree in academic_profile.get(
            "degree",
            []
        )
    ]

    # Normalize JD degrees
    jd_degrees = [

        normalize_degree(degree)

        for degree in jd_education
    ]

    # Exact degree match
    for degree in resume_degrees:

        if degree in jd_degrees:

            return 100

    # Optional field match
    jd_text = " ".join(
        jd_education
    ).lower()

    for field in academic_profile.get(
        "field_of_study",
        []
    ):

        if field.lower() in jd_text:

            return 80

    return 0


def save_academic_profile(

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