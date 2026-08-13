import json
import os
import shutil
from parsers.resume_parser import extract_resume
from parsers.resume_parser import clean_resume_text
from parsers.resume_parser import save_output
from parsers.jd_parser import parse_job_description
from parsers.jd_parser import save_jd_output
from parsers.section_classifier import segment_resume
from parsers.section_classifier import save_output
from parsers.skill_extractor import extract_skills
from parsers.skill_extractor import extract_soft_skills
from parsers.skill_extractor import save_skill_output
from parsers.experience_parser import extract_experience
from parsers.experience_parser import calculate_relevance
from parsers.experience_parser import save_experience_output
from parsers.education_parser import *
from parsers.semantic_matcher import *
from scoring.ats_score import *
from ranking.rank_candidates import *
import gc
import time
from screening_ai.eligibility_engine import *

def sync_candidate_folder(resume_folder, candidate_folder):

    current_resumes = {
        os.path.splitext(f)[0]
        for f in os.listdir(resume_folder)
        if f.endswith(".pdf")
    }

    os.makedirs(candidate_folder, exist_ok=True)

    deleted = 0

    for folder in os.listdir(candidate_folder):

        folder_path = os.path.join(candidate_folder, folder)

        if os.path.isdir(folder_path):

            if folder not in current_resumes:

                shutil.rmtree(folder_path)

                deleted += 1

                print(f"Removed deleted candidate: {folder}")

    return deleted

def run_pipeline():
    print("=== run_pipeline started ===")
    start_time = time.perf_counter()
    RESUME_FOLDER = "data/resumes"

    print("Resume folder:", RESUME_FOLDER)
    print("Exists:", os.path.exists(RESUME_FOLDER))
    print("Files:", os.listdir(RESUME_FOLDER))

    resume_files = [

        file

        for file in os.listdir(
            RESUME_FOLDER
        )

        if file.lower().endswith(".pdf")
    ]

    print("Found resumes:")
    for f in resume_files:
        print(f)

    CANDIDATE_FOLDER = "data/candidates"

    deleted_candidates = sync_candidate_folder(
        RESUME_FOLDER,
        CANDIDATE_FOLDER
    )


    # DAY 6 - Job Description Parsing System

    # Input JD Path
    JD_PATH = "data/jd_samples/jd_sample.pdf"

    # Output Path
    OUTPUT_PATH = "data/parsed_jd/jd_output.json"

    # Parse Job Description
    jd_data = parse_job_description(JD_PATH)

    # Save Structured Output
    save_jd_output(jd_data, OUTPUT_PATH)

    print("Job description parsing completed successfully")

    processed_count = 0
    skipped_count = 0

    for resume_file in resume_files:

        candidate_name = os.path.splitext(
            resume_file
        )[0]

        RESUME_PATH = os.path.join(
            RESUME_FOLDER,
            resume_file
        )

        candidate_folder = os.path.join(

            "data",

            "candidates",

            candidate_name
        )

        ats_file = os.path.join(candidate_folder, "ats.json")

        if os.path.exists(ats_file):
            print(f"Skipping {candidate_name} (already processed)")
            skipped_count += 1
            continue

        processed_count += 1

        os.makedirs(
            candidate_folder,
            exist_ok=True
        )

        print(
            f"\nProcessing {candidate_name}"
        )



        #DAY 5

        

        OUTPUT_PATH = os.path.join(
            candidate_folder,
            "extracted.txt"
        )

        resume_text = extract_resume(RESUME_PATH)

        cleaned_text = clean_resume_text(resume_text)

        save_output(cleaned_text, OUTPUT_PATH)

        print("Resume extraction completed successfully")


        
        # DAY 8 - Resume Section Segmentation

        segmented_data = segment_resume(
            RESUME_PATH
        )

        OUTPUT_PATH = os.path.join(
            candidate_folder,
            "sections.json"
        )
        # Segment Resume Sections
        segmented_data = segment_resume(RESUME_PATH)

        # Save Output
        save_output(segmented_data, OUTPUT_PATH)

        print("Resume section segmentation completed")

        # DAY 9 - Skill Extraction Engine

        skills = extract_skills(segmented_data)
        normalized = {}

        for skill, score in skills.items():

            normalized[skill.title()] = score

        skills = normalized

        soft_skills = extract_soft_skills(segmented_data)


        skill_output = {

            "technical_skills": skills,

            "soft_skills": soft_skills
        }

        save_skill_output(
            skill_output,
            os.path.join(
                candidate_folder,
                "skills.json"
            )
        )

        skills_data = skill_output

        print("Skill extraction completed successfully")


        # DAY 10

        sections_file = os.path.join(
            candidate_folder,
            "sections.json"
        )

        with open(
            sections_file,
            "r"
        ) as file:

            segmented_resume = json.load(file)

        experience_data = extract_experience(
            segmented_resume
        )

        target_role = "general"

        if jd_data["role"]:
            target_role = jd_data["role"][1]

        experience_data[
            "relevance_score"
        ] = calculate_relevance(
            experience_data,
            target_role
        )

        print(
            "Experience parsing completed successfully"
        )
        save_experience_output(
            experience_data,
            os.path.join(
                candidate_folder,
                "experience.json"
            )
        )

        # DAY 11

        sections_file = os.path.join(
            candidate_folder,
            "sections.json"
        )

        with open(
            sections_file,
            "r"
        ) as file:

            segmented_resume = json.load(file)

        academic_profile = {

            "education":
            extract_education(
                segmented_resume
            ),

            "certifications":
            extract_certifications(
                segmented_resume
            )
        }

        academic_profile[
            "education_relevance"
        ] = calculate_education_relevance(

            academic_profile["education"],

            jd_data["education"]
        )

        save_academic_profile(

            academic_profile,

            os.path.join(
                candidate_folder,
                "education.json"
            )
        )

        print(
            "Education and certification parsing completed successfully"
        )


        # DAY 12

        sections_file = os.path.join(
            candidate_folder,
            "sections.json"
        )

        with open(
            sections_file,
            "r"
        ) as file:

            segmented_resume = json.load(file)

        with open(
            "data/parsed_jd/jd_output.json",
            "r"
        ) as file:

            jd_data = json.load(file)

        similarity_result = semantic_match(
            segmented_resume,
            jd_data
        )

        save_similarity_report(
            similarity_result,
            os.path.join(
                candidate_folder,
                "similarity.json"
            )
        )

        print(
            "Semantic matching completed successfully"
        )

        
        # DAY 13

        sections_file = os.path.join(
            candidate_folder,
            "sections.json"
        )

        with open(
            sections_file,
            "r"
        ) as file:

            segmented_resume = json.load(file)

        with open(
            "data/parsed_jd/jd_output.json",
            "r"
        ) as file:

            jd_data = json.load(file)

        with open(
            os.path.join(
                candidate_folder,
                "education.json"
            ),
            "r"
        ) as file:

            education_data = json.load(file)

        with open(
            os.path.join(
                candidate_folder,
                "experience.json"
            ),
            "r"
        ) as file:

            experience_data = json.load(file)

        with open(
            os.path.join(
                candidate_folder,
                "similarity.json"
            ),
            "r"
        ) as file:

            semantic_data = json.load(file)


        candidate_skills = list(

            skills_data[
                "technical_skills"
            ].keys()
        )

        jd_skills = jd_data[
            "skills"
        ]

        skill_score = calculate_skill_score(

            candidate_skills,

            jd_skills
        )

        experience_score = experience_data.get(
            "relevance_score",
            0
        )

        education_score = education_data.get(
            "education_relevance",
            0
        )

        semantic_score = semantic_data.get(
            "overall_similarity",
            0
        )
        
        if jd_data["role"]:

            role = jd_data[
                "role"
            ][1]

        else:

            role = "general"  

        scores = {

            "skill_score": skill_score,

            "experience_score": experience_score,

            "education_score": education_score,

            "semantic_score": semantic_score
        }

        

        skill_score = scores["skill_score"]
        experience_score = scores["experience_score"]
        education_score = scores["education_score"]
        semantic_score = scores["semantic_score"] 

        final_score = calculate_ats_score(

            skill_score,

            experience_score,

            education_score,

            semantic_score,

            role
        )

        result = {

            "candidate_score":
            final_score,

            "role":
            role,

            "breakdown":
            generate_explanation(

                skill_score,

                experience_score,

                education_score,

                semantic_score
            )
        }

        save_ats_score(

            result,

            os.path.join(
            candidate_folder,
            "ats.json"
        )
        )
        
        print("Evaluating candidate...")
        eligibility = evaluate_candidate(

            candidate_name,

            role,

            final_score,

            candidate_skills,

            experience_score,

            education_score

        )

        print("Saving eligibility...")
        save_eligibility(

            eligibility,

            os.path.join(

                candidate_folder,

                "eligibility.json"

            )

        )

        print(
            "Eligibility decision completed successfully"
        )

        print(
            "ATS scoring completed successfully"
        )

        

        bias_report = {

            "resume_normalized": True,

            "semantic_matching_used": True,

            "keyword_only_matching": False,

            "personal_information_masked": False,

            "score_range": "0-100"
        }

        with open(

            os.path.join(
                candidate_folder,
                "bias_report.json"
            ),

            "w"

        ) as file:

            json.dump(
                bias_report,
                file,
                indent=4
            )
        del resume_text
        del cleaned_text
        del segmented_data
        del skills_data
        del experience_data
        del education_data
        del semantic_data

        gc.collect()


    # DAY 14

    

    candidate_list = []

    for candidate in os.listdir(
        "data/candidates"
    ):

        ats_file = os.path.join(

            "data",

            "candidates",

            candidate,

            "ats.json"
        )

        if os.path.exists(
            ats_file
        ):

            with open(
                ats_file,
                "r"
            ) as file:

                ats_data = json.load(
                    file
                )

            candidate_list.append({

                "candidate_name":
                candidate,

                **ats_data
            })

    ranked_output = rank_candidates(
        candidate_list
    )

    save_ranked_candidates(
        ranked_output,
        "data/ranking_output/ranked_candidates.json"
    )

    print("Candidate ranking completed successfully")

    end_time = time.perf_counter()

    print("\n========== PERFORMANCE REPORT ==========")
    print(f"Total Resumes      : {len(resume_files)}")
    print(f"Deleted Candidates : {deleted_candidates}")
    print(f"Processing Time    : {end_time-start_time:.2f} sec")
    print("========================================")

    report = {
        "total_resumes": len(resume_files),
        "processed": processed_count,
        "skipped": skipped_count,
        "deleted_candidates": deleted_candidates,
        "processing_time_seconds": round(end_time-start_time, 2),
        "status": "Completed"
    }

    os.makedirs("data/reports", exist_ok=True)

    with open("data/reports/performance_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print(f"Total Resumes      : {len(resume_files)}")
    print(f"Processed          : {processed_count}")
    print(f"Skipped            : {skipped_count}")
    print(f"Deleted Candidates : {deleted_candidates}")
    print(f"Processing Time    : {end_time-start_time:.2f} sec")

    

if __name__ == "__main__":
    run_pipeline()
