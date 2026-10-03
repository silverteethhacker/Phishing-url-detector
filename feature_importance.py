import joblib

model = joblib.load("phishing_model.pkl")

feature_names = [
    "url_length",
    "hostname_length",
    "path_length",
    "dot_count",
    "hyphen_count",
    "slash_count",
    "question_count",
    "equal_count",
    "at_count",
    "digit_count",
    "special_char_count",
    "has_https",
    "has_ip",
    "subdomain_count",
    "suspicious_word_count",
    "has_login",
    "has_verify",
    "has_password",
    "has_at_symbol",
    "double_slash_redirect"
]

importances = model.feature_importances_

results = list(zip(feature_names, importances))

results.sort(key=lambda x: x[1], reverse=True)

print("\n" + "=" * 45)
print("       FEATURE IMPORTANCE")
print("=" * 45)

for name, importance in results:
    print(f"{name:25} : {importance:.4f}")

print("=" * 45)
