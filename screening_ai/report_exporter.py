def export_report_text(report):

    text = f"""
=========================================
        AI SCREENING REPORT
=========================================

Candidate ID : {report['candidate_id']}

Job ID       : {report['job_id']}

Final Score  : {report['final_score']}

Decision     : {report['decision']}


========== STRENGTHS ==========
"""

    for item in report["summary"]["strengths"]:

        text += f"\n• {item}"

    text += "\n\n========== RISKS =========="

    for item in report["summary"]["risks"]:

        text += f"\n• {item}"

    text += "\n\n====== MISSING DATA ======"

    for item in report["summary"]["missing_data"]:

        text += f"\n• {item}"

    text += "\n\n========= HIGHLIGHTS ========="

    text += f"""

Salary Expectation : {report['highlights']['salary_expectation']}

Availability       : {report['highlights']['availability']}

Confirmed Skills   : {', '.join(report['highlights']['confirmed_skills'])}

"""

    text += "\n========== ANSWERS ==========\n"

    for answer in report["answers"]:

        text += f"\n{answer['question_id']} : {answer['answer']}\n"

    return text