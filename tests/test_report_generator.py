from screening_ai.report_generator import generate_screening_report


def test_report_generator():

    report = generate_screening_report(

        "C1",

        "J1",

        [],

        [],

        []

    )

    assert report["candidate_id"] == "C1"

    assert report["job_id"] == "J1"

    assert report["decision"] == "Reject"