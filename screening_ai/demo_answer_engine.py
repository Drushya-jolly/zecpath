from screening_ai.answer_engine import process_answer

answers = [
    ("Q1", "experience", "I have 3 years of experience in Python and Django."),
    ("Q2", "skills", "python , django"),
    ("Q3", "salary", "My expected salary is 8 LPA."),
    ("Q4", "availability", "I can join after 30 days."),
    ("Q5", "experience", "")
]

for qid, category, answer in answers:
    result = process_answer(qid, category, answer)
    print(result)
    