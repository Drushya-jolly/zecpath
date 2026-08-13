import json
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    classification_report
)

# Load expected results
with open("tests/expected_results.json", "r") as f:
    expected = json.load(f)

# Load ATS output
with open("data/ranking_output/ranked_candidates.json", "r") as f:
    actual = json.load(f)

label_map = {
    "Reject": 0,
    "Review": 1,
    "Shortlist": 2
}

y_true = []
y_pred = []

rows = []

for e in expected:

    candidate = e["candidate_name"]
    expected_status = e["expected_status"]

    result = next(
        (c for c in actual if c["candidate_name"] == candidate),
        None
    )

    if result is None:
        actual_status = "Missing"
        match = False
    else:
        actual_status = result["status"]
        match = expected_status == actual_status

        y_true.append(label_map[expected_status])
        y_pred.append(label_map[actual_status])

    rows.append({
        "Candidate": candidate,
        "Expected": expected_status,
        "Actual": actual_status,
        "Match": "✅" if match else "❌"
    })

df = pd.DataFrame(rows)

print("\n========== ATS TEST REPORT ==========\n")
print(df.to_string(index=False))

print("\n========== METRICS ==========\n")

print(f"Accuracy : {accuracy_score(y_true, y_pred):.2f}")
print(f"Precision: {precision_score(y_true, y_pred, average='weighted', zero_division=0):.2f}")
print(f"Recall   : {recall_score(y_true, y_pred, average='weighted'):.2f}")

print("\nClassification Report\n")
print(classification_report(y_true, y_pred, zero_division=0))