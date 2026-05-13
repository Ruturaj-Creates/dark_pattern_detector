from scanner import fetch_page
from detectors.urgency import detect_urgency

url = input("Enter URL: ")

html = fetch_page(url)

results = detect_urgency(html)

if results:
    print("\n[WARNING] Fake urgency patterns detected:\n")

    for item in results:
        print(f"- {item}")

else:
    print("\nNo urgency patterns detected.")