from scanner import fetch_page
from detectors.urgency import detect_urgency
from detectors.scarcity import detect_scarcity
from risk_score import calculate_risk

url = input("Enter URL: ")

html = fetch_page(url)

urgency_results = detect_urgency(html)
scarcity_results = detect_scarcity(html)

risk_score = calculate_risk(
    urgency_results,
    scarcity_results
)

print("\n========== DARK PATTERN REPORT ==========\n")

print(f"Risk Score: {risk_score}/100\n")

if urgency_results:
    print("[HIGH] Fake urgency detected")

    for item in urgency_results:
        print(f"- {item}")

    print()

if scarcity_results:
    print("[MEDIUM] Scarcity pressure detected")

    for item in scarcity_results:
        print(f"- {item}")

if not urgency_results and not scarcity_results:
    print("No dark patterns detected.")