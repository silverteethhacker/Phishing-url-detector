from urllib.parse import urlparse
import re


def extract_features(url):

    parsed = urlparse(url)

    hostname = parsed.hostname or ""
    path = parsed.path or ""

    url_lower = url.lower()

    features = {}

    # 1. URL length
    features["url_length"] = len(url)

    # 2. Hostname length
    features["hostname_length"] = len(hostname)

    # 3. Path length
    features["path_length"] = len(path)

    # 4. Number of dots
    features["dot_count"] = url.count(".")

    # 5. Number of hyphens
    features["hyphen_count"] = url.count("-")

    # 6. Number of slashes
    features["slash_count"] = url.count("/")

    # 7. Number of question marks
    features["question_count"] = url.count("?")

    # 8. Number of equal signs
    features["equal_count"] = url.count("=")

    # 9. Number of @ symbols
    features["at_count"] = url.count("@")

    # 10. Number of digits
    features["digit_count"] = sum(char.isdigit() for char in url)

    # 11. Number of special characters
    special_chars = r"[!#$%&'()*+,;:<=>?@\[\]^_`{|}~]"
    features["special_char_count"] = len(
        re.findall(special_chars, url)
    )

    # 12. HTTPS
    features["has_https"] = int(
        parsed.scheme.lower() == "https"
    )

    # 13. IP address
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    features["has_ip"] = int(
        bool(re.match(ip_pattern, hostname))
    )

    # 14. Subdomain count
    if hostname:

        parts = hostname.split(".")

        if len(parts) > 2:
            features["subdomain_count"] = len(parts) - 2
        else:
            features["subdomain_count"] = 0

    else:
        features["subdomain_count"] = 0

    # 15. Suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "verification",
        "account",
        "password",
        "secure",
        "update",
        "signin",
        "confirm",
        "bank"
    ]

    features["suspicious_word_count"] = sum(
        word in url_lower
        for word in suspicious_words
    )

    # 16. Contains "login"
    features["has_login"] = int(
        "login" in url_lower
    )

    # 17. Contains "verify"
    features["has_verify"] = int(
        "verify" in url_lower
    )

    # 18. Contains "password"
    features["has_password"] = int(
        "password" in url_lower
    )

    # 19. Contains @
    features["has_at_symbol"] = int(
        "@" in url
    )

    # 20. URL contains double slash after protocol
    after_protocol = url_lower.split("://", 1)[-1]

    features["double_slash_redirect"] = int(
        "//" in after_protocol
    )

    return features
