import json

from scanner import fetch_page
from detectors.urgency import detect_urgency
from detectors.scarcity import detect_scarcity
from risk_score import calculate_risk
from report_generator import generate_report
from save_report import save_report
url = input("Enter URL: ")

html = fetch_page(url)

urgency_results = detect_urgency(html)
scarcity_results = detect_scarcity(html)

risk_score = calculate_risk(
    urgency_results,
    scarcity_results
)

report = generate_report(
    risk_score,
    urgency_results,
    scarcity_results,
    url
)

saved_file = save_report(report)

print(f"\nReport saved to: {saved_file}")

print("\n========== DARK PATTERN REPORT ==========\n")

print(json.dumps(report, indent=4))