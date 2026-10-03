import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from features import extract_features


# Load dataset
df = pd.read_csv("dataset.csv")

X = []
y = []

for _, row in df.iterrows():
    features = extract_features(str(row["url"]))

    X.append(list(features.values()))
    y.append(int(row["label"]))


# Load trained model
model = joblib.load("phishing_model.pkl")


# Make predictions
predictions = model.predict(X)


# Calculate metrics
accuracy = accuracy_score(y, predictions)
precision = precision_score(y, predictions, zero_division=0)
recall = recall_score(y, predictions, zero_division=0)
f1 = f1_score(y, predictions, zero_division=0)

cm = confusion_matrix(y, predictions)


print("=" * 45)
print("       MODEL EVALUATION")
print("=" * 45)

print(f"Accuracy  : {accuracy:.2f}")
print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"F1-Score  : {f1:.2f}")

print("\nConfusion Matrix:")
print(cm)

print("=" * 45)
