from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
import json
import subprocess
import sys



app = FastAPI(
    title="ATS AI API",
    version="1.0"
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
UPLOAD_FOLDER = os.path.join(
    BASE_DIR,
    "data",
    "resumes"
)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
@app.post("/upload-resumes")
async def upload_resume(resume: UploadFile = File(...)):

    save_path = os.path.join(
        UPLOAD_FOLDER,
        resume.filename
    )

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(
            resume.file,
            buffer
        )

    return {
        "message": "Upload Successful",
        "filename": resume.filename
    }


@app.post("/process")
def process_candidates():
    from main import run_pipeline

    run_pipeline()

    return {
        "message": "ATS Pipeline Completed"
    }

@app.get("/ranking")
def get_ranking():

    path = (

        "data/ranking_output/"
        "ranked_candidates.json"
    )

    if not os.path.exists(
        path
    ):

        return JSONResponse(

            status_code=404,

            content={

                "message":

                "Ranking not generated."
            }
        )

    with open(
        path,
        "r"
    ) as file:

        data = json.load(
            file
        )

    return data


@app.get("/candidate/{candidate_name}")
def candidate_details(

    candidate_name: str

):

    folder = os.path.join(

        "data",

        "candidates",

        candidate_name
    )

    if not os.path.exists(
        folder
    ):

        return JSONResponse(

            status_code=404,

            content={

                "message":

                "Candidate not found"
            }
        )

    result = {}

    files = [

        "skills.json",

        "education.json",

        "experience.json",

        "similarity.json",

        "ats.json",

        "bias_report.json"
    ]

    for file_name in files:

        path = os.path.join(

            folder,

            file_name
        )

        if os.path.exists(
            path
        ):

            with open(
                path,
                "r"
            ) as file:

                result[
                    file_name.replace(
                        ".json",
                        ""
                    )
                ] = json.load(
                    file
                )

    return result