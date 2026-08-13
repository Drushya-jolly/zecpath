import re
import json
from datetime import datetime
from parsers.semantic_matcher import calculate_similarity


def extract_company_names(text):

    companies = []

    pattern = r"intern\s+.*?,\s*([^,]+),"

    matches = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    for match in matches:

        company = match.strip()

        if company not in companies:

            companies.append(company)

    return companies


def extract_job_titles(text):

    pattern = r"intern\s*[–-]\s*([a-zA-Z]+)"

    matches = re.findall(
        pattern,
        text,
        re.IGNORECASE
    )

    job_titles = []

    for match in matches:

        role = f"intern {match.lower()}"

        if role not in job_titles:

            job_titles.append(role)

    return job_titles


def extract_employment_dates(text):

    date_pattern = r"\d{1,2}\s+\w+\s+\d{4}"

    return re.findall(
        date_pattern,
        text,
        re.IGNORECASE
    )


def calculate_total_experience(dates):

    if len(dates) < 2:

        return "0 months"

    try:

        parsed_dates = []

        for date in dates:

            parsed_dates.append(
                datetime.strptime(
                    date.title(),
                    "%d %B %Y"
                )
            )

        parsed_dates.sort()

        total_days = 0

        for i in range(
            0,
            len(parsed_dates) - 1,
            2
        ):

            start_date = parsed_dates[i]

            end_date = parsed_dates[i + 1]

            total_days += (
                end_date - start_date
            ).days

        months = round(
            total_days / 30
        )

        return f"{months} months"

    except:

        return "Unable to Calculate"


def detect_gaps(dates):

    if len(dates) < 4:

        return False

    return False


def detect_overlaps(dates):

    if len(dates) < 4:

        return False

    return False


def calculate_relevance(

    experience_object,

    target_role

):

    if not target_role:

        return 0

    best_score = 0

    for role in experience_object.get(
        "job_titles",
        []
    ):

        similarity = calculate_similarity(

            role,

            target_role

        )

        if similarity > best_score:

            best_score = similarity

    return round(best_score)


def extract_experience(
    segmented_resume
):

    experience_text = " ".join(
        segmented_resume.get("experience", [])
    ).lower()


    dates = extract_employment_dates(
        experience_text
    )

    experience_object = {

        "companies":
        extract_company_names(
            experience_text
        ),

        "job_titles":
        extract_job_titles(
            experience_text
        ),

        "employment_dates":
        dates,

        "total_experience":
        calculate_total_experience(
            dates
        ),

        "gaps_detected":
        detect_gaps(
            dates
        ),

        "overlapping_roles":
        detect_overlaps(
            dates
        )
    }

    return experience_object
    print("EXPERIENCE TEXT:")
    print(experience_text)


def save_experience_output(data, output_path):

    with open(output_path, "w") as file:

        json.dump(data, file, indent=4)