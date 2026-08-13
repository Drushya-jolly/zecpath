from screening_ai.answer_engine import process_answer
from screening_ai.scoring_engine import score_answer
from screening_ai.behavior_report import generate_behavior_report

from screening_ai.report_generator import generate_screening_report
from screening_ai.report_exporter import export_report_text


answers = [

    process_answer(
        "Q1",
        "experience",
        "I have 3 years of experience in Python."
    ),

    process_answer(
        "Q2",
        "skills",
        "Python SQL Django"
    ),

    process_answer(
        "Q3",
        "salary",
        "6 LPA"
    ),

    process_answer(
        "Q4",
        "availability",
        "I can join after 30 days."
    ),

    process_answer(
        "Q5",
        "experience",
        "I don't know."
    )

]


scores = [

    score_answer(answer)

    for answer in answers

]


behavior_reports = [

    generate_behavior_report(

        answer["original_answer"],

        5

    )

    for answer in answers

]


report = generate_screening_report(

    "C101",

    "J205",

    answers,

    scores,

    behavior_reports

)


print(report)

print()

print(export_report_text(report))