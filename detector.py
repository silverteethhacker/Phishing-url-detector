from urllib.parse import urlparse


def analyze_url(url):
    parsed = urlparse(url)

    score = 0
    reasons = []

    # HTTPS check
    if parsed.scheme != "https":
        score += 2
        reasons.append("HTTPS is not used")

    # Long URL
    if len(url) > 100:
        score += 2
        reasons.append("URL is unusually long")

    # @ symbol
    if "@" in url:
        score += 3
        reasons.append("URL contains @ symbol")

    hostname = parsed.hostname

    # IP address instead of domain
    if hostname:
        parts = hostname.split(".")

        if len(parts) == 4 and all(part.isdigit() for part in parts):
            score += 3
            reasons.append("URL uses an IP address")

    # Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "verification",
        "password",
        "account",
        "secure",
        "update"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    # Classification
    if score >= 6:
        result = "PHISHING"
    elif score >= 3:
        result = "SUSPICIOUS"
    else:
        result = "LIKELY SAFE"

    return result, score, reasons


url = input("Enter URL: ")

result, score, reasons = analyze_url(url)

print("\nResult:", result)
print("Risk Score:", score)

if reasons:
    print("\nReasons:")

    for reason in reasons:
        print("-", reason)
