import joblib
from features import extract_features


# Load trained model
model = joblib.load("phishing_model.pkl")

print("=" * 45)
print("       PHISHING URL DETECTOR")
print("=" * 45)

url = input("Enter URL to scan: ").strip()

# Extract URL features
features = extract_features(url)

# Convert features into model input
X = [list(features.values())]

# Prediction
prediction = model.predict(X)[0]

# Model probability
probability = model.predict_proba(X)[0]

phishing_probability = probability[1] * 100


print("\nURL:", url)

if prediction == 1:
    print("Result: PHISHING")
else:
    print("Result: LIKELY LEGITIMATE")

print(f"Model phishing probability: {phishing_probability:.2f}%")

print("\nExtracted Features:")
print("-" * 30)

for name, value in features.items():
    print(f"{name}: {value}")

print("=" * 45)
