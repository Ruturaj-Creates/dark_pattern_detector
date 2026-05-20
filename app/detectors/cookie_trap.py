import re

COOKIE_PATTERNS = [
    r"accept all",
    r"allow all cookies",
    r"agree",
    r"got it",
    r"accept cookies",
    r"enable cookies"
]

def detect_cookie_trap(text):

    findings = []

    for pattern in COOKIE_PATTERNS:

        matches = re.findall(pattern, text, re.IGNORECASE)

        findings.extend(list(set(matches)))

    return findings