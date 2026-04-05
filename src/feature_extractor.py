import re
from urllib.parse import urlparse


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "bank",
    "confirm",
    "password",
    "paypal",
    "signin",
    "free",
    "gift",
    "win",
    "urgent",
    "alert"
]


def has_ip_address(domain: str) -> int:
    """
    Returns 1 if the domain looks like an IP address, otherwise 0.
    """
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return 1 if re.match(ip_pattern, domain) else 0


def count_suspicious_keywords(url: str) -> int:
    """
    Count how many suspicious words appear in the URL.
    """
    url = url.lower()
    count = 0
    for word in SUSPICIOUS_KEYWORDS:
        if word in url:
            count += 1
    return count


def extract_features(url: str) -> dict:
    """
    Extract numerical features from a URL for phishing detection.
    """
    # If user enters URL without http/https, add http://
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    parsed = urlparse(url)

    domain = parsed.netloc.lower()
    path = parsed.path.lower()
    full_url = url.lower()

    # Remove port if present
    domain_no_port = domain.split(":")[0]

    features = {
        "url_length": len(full_url),
        "domain_length": len(domain_no_port),
        "path_length": len(path),
        "num_dots": full_url.count("."),
        "num_hyphens": full_url.count("-"),
        "num_underscores": full_url.count("_"),
        "num_slashes": full_url.count("/"),
        "num_question_marks": full_url.count("?"),
        "num_equals": full_url.count("="),
        "num_at_symbols": full_url.count("@"),
        "num_digits": sum(char.isdigit() for char in full_url),
        "uses_https": 1 if parsed.scheme == "https" else 0,
        "has_ip_address": has_ip_address(domain_no_port),
        "num_subdomains": max(0, len(domain_no_port.split(".")) - 2),
        "suspicious_keyword_count": count_suspicious_keywords(full_url),
        "contains_login": 1 if "login" in full_url else 0,
        "contains_verify": 1 if "verify" in full_url else 0,
        "contains_secure": 1 if "secure" in full_url else 0,
        "contains_bank": 1 if "bank" in full_url else 0,
        "contains_paypal": 1 if "paypal" in full_url else 0,
        "contains_free": 1 if "free" in full_url else 0,
        "contains_win": 1 if "win" in full_url else 0,
        "has_shortener_hint": 1 if any(
            short in domain_no_port for short in ["bit.ly", "tinyurl.com", "goo.gl", "t.co", "rb.gy"]
        ) else 0,
    }

    return features