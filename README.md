# Zecpath AI System

## Project Overview

Zecpath is an AI-powered autonomous hiring platform designed to automate and streamline the complete recruitment lifecycle. The platform integrates AI-based resume screening, automated voice interactions, HR and technical interviews, behavioral analysis, machine tests, scoring systems, and offer automation to improve hiring efficiency and reduce recruiter workload.

---

## Features

- AI-based ATS resume screening  
- Automated AI voice calling system  
- HR and technical interview automation  
- Communication and behavioral analysis  
- Machine test and coding assessment  
- AI scoring and recommendation engine  
- Offer letter generation and onboarding support  

---

## Project Structure

### data/
Stores candidate resumes, job descriptions, interview transcripts, and related datasets.

### parsers/
Processes resumes and extracts candidate information such as skills, education, and experience.

### ats_engine/
Manages ATS-based scoring, resume matching, and candidate shortlisting.

### screening_ai/
Handles automated AI screening calls and candidate interaction workflows.

### interview_ai/
Contains AI modules for HR interviews, technical interviews, and adaptive questioning.

### scoring/
Calculates interview scores and generates hiring recommendations.

### utils/
Includes common helper functions, logging configuration, and reusable utilities.

### tests/
Contains testing scripts for validating AI modules and workflows.

---

## Setup Instructions

### Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

### Execute Test Scripts

```bash
pytest tests/
```

---

## API

### Start AI Screening

**Endpoint**

```
POST /screening/start
```

**Sample Request**

```json
{
  "candidate_id": "C101",
  "job_id": "J501",
  "answers": [],
  "scores": [],
  "behavior": []
}
```

**Sample Response**

```json
{
  "candidate_id": "C101",
  "job_id": "J501",
  "final_score": 82.5,
  "decision": "Proceed"
}
```

---

## Output

The system generates a structured AI screening report containing:

- Candidate ID
- Job ID
- Final Screening Score
- Hiring Decision
- Candidate Strengths
- Risk Factors
- Missing Information
- Salary Expectation
- Availability
- Confirmed Skills
- Candidate Answers

---

## Technologies Used

- Python
- Flask
- PyTest
- JSON
- Regular Expressions
- Sentence Transformers
- FAISS
- LangChain

---

## Future Improvements

- LLM-based reasoning for interview evaluation
- Multilingual AI interviews
- Real-time speech recognition
- Cloud deployment
- Recruiter dashboard