import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
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
# MODELS
# ==============================

models = {

    "Decision Tree":
        DecisionTreeClassifier(
            random_state=42
        ),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "Logistic Regression":
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(
                max_iter=1000,
                random_state=42
            ))
        ]),

    "KNN":
        Pipeline([
            ("scaler", StandardScaler()),
            ("model", KNeighborsClassifier(
                n_neighbors=3
            ))
        ])
}


# ==============================
# TRAIN & EVALUATE
# ==============================

print("\n" + "=" * 70)
print("              MODEL COMPARISON")
print("=" * 70)

print(f"\nTraining samples : {len(X_train)}")
print(f"Testing samples  : {len(X_test)}")

print("\n")


for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

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

    print("-" * 70)

    print(f"Model      : {name}")
    print(f"Accuracy   : {accuracy:.2f}")
    print(f"Precision  : {precision:.2f}")
    print(f"Recall     : {recall:.2f}")
    print(f"F1-Score   : {f1:.2f}")


print("-" * 70)
