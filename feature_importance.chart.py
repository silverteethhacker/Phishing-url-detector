import joblib
import matplotlib.pyplot as plt

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

top_features = results[:10]

names = [x[0] for x in top_features]
values = [x[1] for x in top_features]

plt.figure(figsize=(10, 6))
plt.barh(names[::-1], values[::-1])

plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Top 10 URL Features")

plt.tight_layout()
plt.show()
