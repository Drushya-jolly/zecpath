from screening_ai.robust_flow import handle_edge_case

samples = [

    ("", 1.0),

    ("hello", 0.4),

    ("hai I know python", 0.9),

    ("um", 1.0),

    ("yes", 1.0),

    ("I have two years of Python experience.", 0.95)

]


for answer, confidence in samples:

    print("--------------------------------")

    print("Answer :", answer)

    result = handle_edge_case(answer,
                              confidence,
                              retry_count=1)

    print(result)