from flask import Flask, request, jsonify

from screening_ai.report_generator import generate_screening_report

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Zecpath AI Screening API Running"
    }

@app.route("/screening/start", methods=["POST"])
def start_screening():

    data = request.json

    candidate_id = data["candidate_id"]
    job_id = data["job_id"]

    answers = data["answers"]
    scores = data["scores"]
    behavior = data["behavior"]

    report = generate_screening_report(
        candidate_id,
        job_id,
        answers,
        scores,
        behavior
    )

    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True)