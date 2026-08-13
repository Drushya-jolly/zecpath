from screening_ai.behavior_report import generate_behavior_report

examples = [

    (
        "I am confident in my Python skills and have strong backend development experience.",
        6
    ),

    (
        "Maybe I know Python but I am not sure.",
        6
    ),

    (
        "I have experience, but I don't know if I can perform well.",
        8
    )

]

for i, (text, duration) in enumerate(examples, start=1):

    print(f"\nCandidate {i}")

    result = generate_behavior_report(text, duration)

    print(result)