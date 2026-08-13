from screening_ai.report_generator import generate_screening_report


def test_system():

    report = generate_screening_report(

        "C1",

        "J1",

        [],

        [],

        []
    )

    assert "candidate_id" in report
    