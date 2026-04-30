import pandas as pd

# Load datasets
ground_truth = pd.read_csv("../dataset/ground_truth.csv")
model_v1 = pd.read_csv("../dataset/model_v1_predictions.csv")
model_v2 = pd.read_csv("../dataset/model_v2_predictions.csv")

# Fields to evaluate
fields = [
    "invoice_number",
    "currency",
    "total_amount",
    "date",
    "shipper"
]

# Function to calculate accuracy
def calculate_accuracy(ground_truth, predictions):
    total_checks = 0
    correct_predictions = 0
    mismatches = []

    for index in range(len(ground_truth)):
        for field in fields:
            total_checks += 1

            gt_value = str(ground_truth.loc[index, field]).strip()
            pred_value = str(predictions.loc[index, field]).strip()

            if gt_value == pred_value:
                correct_predictions += 1
            else:
                mismatches.append({
                    "document_id": ground_truth.loc[index, "document_id"],
                    "field": field,
                    "ground_truth": gt_value,
                    "prediction": pred_value
                })

    accuracy = (correct_predictions / total_checks) * 100

    return accuracy, mismatches


# Evaluate Model V1
v1_accuracy, v1_mismatches = calculate_accuracy(
    ground_truth,
    model_v1
)

# Evaluate Model V2
v2_accuracy, v2_mismatches = calculate_accuracy(
    ground_truth,
    model_v2
)

# Print results
print("========== ML Evaluation Results ==========")
print()

print(f"Model V1 Accuracy: {v1_accuracy:.2f}%")
print(f"Model V2 Accuracy: {v2_accuracy:.2f}%")

print()
print("========== Model Comparison ==========")

if v2_accuracy > v1_accuracy:
    print("Model V2 shows improved extraction accuracy.")
else:
    print("No significant improvement observed.")

print()
print("========== Sample Mismatches (V1) ==========")

for mismatch in v1_mismatches[:5]:
    print(mismatch)

# Export mismatch report
mismatch_df = pd.DataFrame(v1_mismatches)

mismatch_df.to_csv(
    "../metrics-analysis/v1_mismatch_report.csv",
    index=False
)

print()
print("Mismatch report exported successfully.")
