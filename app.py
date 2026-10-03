from flask import Flask, render_template, request
import joblib

from features import extract_features

app = Flask(__name__)

model = joblib.load("phishing_model.pkl")


def get_reasons(features):

    reasons = []

    if features["has_ip"]:
        reasons.append("IP address used instead of a normal domain")

    if not features["has_https"]:
        reasons.append("HTTPS is not detected")

    if features["url_length"] > 75:
        reasons.append("URL is unusually long")

    if features["suspicious_word_count"] > 0:
        reasons.append("Suspicious keywords detected")

    if features["subdomain_count"] > 2:
        reasons.append("Multiple subdomains detected")

    if features["at_count"] > 0:
        reasons.append("@ symbol detected in URL")

    if features["double_slash_redirect"]:
        reasons.append("Possible double-slash redirect pattern")

    if not reasons:
        reasons.append("No major suspicious URL characteristics detected")

    return reasons


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    probability = None
    url = ""
    details = None
    reasons = []

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        if url:

            features = extract_features(url)

            X = [list(features.values())]

            prediction = model.predict(X)[0]

            probabilities = model.predict_proba(X)[0]

            probability = probabilities[1] * 100

            if prediction == 1:
                result = "PHISHING"
            else:
                result = "LIKELY LEGITIMATE"

            reasons = get_reasons(features)

            details = {
                "HTTPS": "Yes" if features["has_https"] else "No",
                "IP Address": "Yes" if features["has_ip"] else "No",
                "Suspicious Keywords":
                    features["suspicious_word_count"],
                "URL Length":
                    features["url_length"],
                "Subdomains":
                    features["subdomain_count"]
            }

    return render_template(
        "index.html",
        result=result,
        probability=probability,
        url=url,
        details=details,
        reasons=reasons
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
