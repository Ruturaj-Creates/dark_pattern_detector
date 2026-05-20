from datetime import datetime
import uuid

def generate_report(
    risk_score,
    urgency_results,
    scarcity_results,
    cookie_findings,
    url
):

    report = {
        "scan_id": str(uuid.uuid4())[:8],
        "url": url,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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

    if cookie_findings:
        report["patterns"].append({
            "type": "cookie_trap",
            "severity": "medium",
            "matches": cookie_findings
        })

    return report