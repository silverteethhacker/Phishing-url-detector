import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from features import extract_features


# ==============================
# LOAD DATASET
# ==============================

df = pd.read_csv("clean_dataset.csv")

df = df.dropna(subset=["url", "label"])


# ==============================
# FEATURE EXTRACTION
# ==============================

X = []
y = []

for _, row in df.iterrows():

    url = str(row["url"])

    features = extract_features(url)

    X.append(list(features.values()))

    y.append(int(row["label"]))


# ==============================
# TRAIN / TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==============================
# LOAD MODEL
# ==============================

model = joblib.load("phishing_model.pkl")


# ==============================
# PREDICTION
# ==============================

predictions = model.predict(X_test)


# ==============================
# METRICS
# ==============================

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    zero_division=0
)


# ==============================
# CONFUSION MATRIX
# ==============================

cm = confusion_matrix(
    y_test,
    predictions
)


# ==============================
# OUTPUT
# ==============================

print("\n" + "=" * 55)
print("        PHISHING URL DETECTOR")
print("        DETAILED EVALUATION")
print("=" * 55)

print(f"\nAccuracy  : {accuracy:.2f}")
print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"F1-Score  : {f1:.2f}")

print("\nConfusion Matrix:")
print(cm)

print("\nMatrix meaning:")
print("Rows    = Actual")
print("Columns = Predicted")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Legitimate",
            "Phishing"
        ],
        zero_division=0
    )
)

print("=" * 55)
