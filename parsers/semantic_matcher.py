import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load Pretrained Embedding Model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text):

    return model.encode(text)


def calculate_similarity(
    text1,
    text2
):

    embedding1 = generate_embedding(
        text1
    )

    embedding2 = generate_embedding(
        text2
    )

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return round(
        similarity * 100,
        2
    )


def get_resume_section(
    resume,
    section_name
):

    return " ".join(
        resume.get(
            section_name,
            []
        )
    )


def get_jd_skills(jd):

    return " ".join(
        jd.get(
            "skills",
            []
        )
    )


def get_jd_roles(jd):

    return " ".join(
        jd.get(
            "role",
            []
        )
    )


def semantic_match(
    segmented_resume,
    jd_data
):

    # Skills Comparison
    resume_skills = get_resume_section(
        segmented_resume,
        "skills"
    )

    jd_skills = get_jd_skills(
        jd_data
    )

    skill_similarity = (
        calculate_similarity(
            resume_skills,
            jd_skills
        )
    )

    # Experience Comparison
    resume_experience = (
        get_resume_section(
            segmented_resume,
            "experience"
        )
    )

    jd_roles = get_jd_roles(
        jd_data
    )

    experience_similarity = (
        calculate_similarity(
            resume_experience,
            jd_roles
        )
    )

    # Project Comparison
    resume_projects = (
        get_resume_section(
            segmented_resume,
            "projects"
        )
    )

    project_similarity = (
        calculate_similarity(
            resume_projects,
            jd_skills
        )
    )

    # Weighted Score
    overall_similarity = round(

        (
            skill_similarity * 0.4
            +
            experience_similarity * 0.3
            +
            project_similarity * 0.3
        ),

        2
    )

    if overall_similarity >= 75:

        match_status = (
            "Good Match"
        )

    elif overall_similarity >= 50:

        match_status = (
            "Moderate Match"
        )

    else:

        match_status = (
            "Low Match"
        )

    return {

        "skill_similarity":
        skill_similarity,

        "experience_similarity":
        experience_similarity,

        "project_similarity":
        project_similarity,

        "overall_similarity":
        overall_similarity,

        "match_status":
        match_status
    }


def save_similarity_report(
    data,
    output_path
):

    cleaned_data = {

        key: float(value)
        if hasattr(value, "item")
        else value

        for key, value in data.items()
    }

    with open(
        output_path,
        "w"
    ) as file:

        json.dump(
            cleaned_data,
            file,
            indent=4
        )
