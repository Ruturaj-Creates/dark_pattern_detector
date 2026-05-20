import json

from scanner import fetch_page
from detectors.urgency import detect_urgency
from detectors.scarcity import detect_scarcity
from risk_score import calculate_risk
from report_generator import generate_report
from app.utils.save_report import save_report
from detectors.cookie_trap import detect_cookie_trap

url = input("Enter URL: ")
html = fetch_page(url)
cookie_results = detect_cookie_trap(html)

urgency_results = detect_urgency(html)
scarcity_results = detect_scarcity(html)

risk_score = calculate_risk(
    urgency_results,
    scarcity_results,
    cookie_results
)

report = generate_report(
    risk_score,
    urgency_results,
    scarcity_results,
    cookie_results,
    url
)

saved_file = save_report(report)

print(f"\nReport saved to: {saved_file}")

print("\n========== DARK PATTERN REPORT ==========\n")

print(json.dumps(report, indent=4))