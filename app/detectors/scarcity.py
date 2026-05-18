import re

SCARCITY_PATTERNS = [
    r"\d+ people viewing",
    r"selling fast",
    r"in high demand",
    r"limited time",
    r"few remaining",
]

def detect_scarcity(text):
    findings = []

    for pattern in SCARCITY_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)

        if matches:
            findings.extend(list(set(matches)))

    return findings