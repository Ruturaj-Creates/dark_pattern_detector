from fastapi import FastAPI
from pydantic import BaseModel

from app.scanner import fetch_page
from app.detectors.urgency import detect_urgency
from app.detectors.scarcity import detect_scarcity
from app.risk_score import calculate_risk
from app.report_generator import generate_report
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScanRequest(BaseModel):
    url: str

@app.post("/scan")
def scan_website(request: ScanRequest):

    html = fetch_page(request.url)

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
    request.url
    )

    return report