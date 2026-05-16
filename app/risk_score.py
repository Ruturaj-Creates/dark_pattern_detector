def calculate_risk(urgency_findings, scarcity_findings):
    score = 0

    score += len(urgency_findings) * 20
    score += len(scarcity_findings) * 15

    return min(score, 100)