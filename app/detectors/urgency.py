import re

URGENCY_PATTERNS = [
    r"only \d+ left",
    r"hurry up",
    r"limited stock",
    r"offer ends soon",
    r"sale ends",
]

def detect_urgency(text):
    findings = []

    for pattern in URGENCY_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)

        if matches:
            findings.extend(matches)

    return findings