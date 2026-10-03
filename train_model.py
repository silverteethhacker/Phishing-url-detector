import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from features import extract_features


# ==============================
# 1. Load dataset
# ==============================

df = pd.read_csv("clean_dataset.csv")

df = df.dropna(subset=["url", "label"])


# ==============================
# 2. Extract features
# ==============================

X = []
y = []

for _, row in df.iterrows():

    url = str(row["url"])

    features = extract_features(url)

    X.append(list(features.values()))
    y.append(int(row["label"]))


# ==============================
# 3. Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))


# ==============================
# 4. Create Random Forest
# ==============================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==============================
# 5. Train
# ==============================

model.fit(X_train, y_train)


# ==============================
# 6. Test on unseen data
# ==============================

predictions = model.predict(X_test)


# ==============================
# 7. Evaluation
# ==============================

accuracy = accuracy_score(y_test, predictions)

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

cm = confusion_matrix(y_test, predictions)


# ==============================
# 8. Display results
# ==============================

print("\n==============================")
print("     MODEL EVALUATION")
print("==============================")

print(f"Accuracy  : {accuracy:.2f}")
print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"F1-Score  : {f1:.2f}")

print("\nConfusion Matrix:")
print(cm)


# ==============================
# 9. Save model
# ==============================

joblib.dump(model, "phishing_model.pkl")

print("\nModel saved as phishing_model.pkl")
