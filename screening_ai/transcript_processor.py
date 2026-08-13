from screening_ai.transcript_normalizer import normalize_transcript


def process_transcript(raw_answers):

    processed = []

    for answer in raw_answers:

        processed.append({

            "question_id":
            answer["question_id"],

            "answer_text":
            normalize_transcript(answer["text"]),

            "confidence_score":
            answer.get("confidence", 0.90)

        })

    return processed