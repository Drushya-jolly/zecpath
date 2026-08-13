from screening_ai.stt_processor import clean_transcript


def process_audio_answers(audio_inputs):

    processed_results = []

    for index, audio in enumerate(audio_inputs):

        cleaned = clean_transcript(audio)

        processed_results.append({

            "question_id": f"Q{index+1}",

            "clean_text": cleaned["clean_text"],

            "confidence": cleaned["confidence"],

            "status": cleaned["status"]

        })

    return processed_results


if __name__ == "__main__":

    audio_inputs = [

        "um i have 3 years experience in python",

        "uh currently working as backend developer",

        ""

    ]

    results = process_audio_answers(audio_inputs)

    for result in results:

        print(result)