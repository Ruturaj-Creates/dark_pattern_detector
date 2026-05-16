def generate_report(risk_score, urgency_results, scarcity_results):

    report = {
        "risk_score": risk_score,
        "patterns": []
    }

    if urgency_results:
        report["patterns"].append({
            "type": "urgency",
            "severity": "high",
            "matches": urgency_results
        })

    if scarcity_results:
        report["patterns"].append({
            "type": "scarcity",
            "severity": "medium",
            "matches": scarcity_results
        })

    return report