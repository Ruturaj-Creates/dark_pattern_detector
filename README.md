# Dark Pattern Detector

A browser-assisted dark pattern detection tool built using Python, FastAPI, Chrome Extension APIs, and Scrapling.

The project detects manipulative UX patterns such as fake urgency, scarcity tactics, and cookie traps on websites.

---

## Features

- Detects urgency patterns
- Detects scarcity tactics
- Detects cookie trap patterns
- Chrome extension integration
- FastAPI backend API
- JSON-based reporting system
- Risk score generation
- Automatic report saving

---

## Architecture

```text
Chrome Extension
        ↓
FastAPI Backend
        ↓
Detection Engine
        ↓
JSON Reports
```

---

## Tech Stack

- Python
- FastAPI
- Scrapling (modern web scraping framework)
- JavaScript
- Chrome Extension APIs
- Regex-based detection engine

---

## Screenshots

### Chrome Extension

![Extension Demo](assets/extension_demo.png)

### Detection Popup

![Detection Popup](assets/detection_popup.png)

### FastAPI Swagger Docs

![Swagger Docs](assets/swagger_docs.png)

---

## Project Structure

```text
dark-pattern-detector/
│
├── app/
├── extension/
├── reports/
├── assets/
├── README.md
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Ruturaj-Creates/dark_pattern_detector.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI Backend

```bash
uvicorn app.api:app --reload
```

---

## Load Chrome Extension

1. Open `chrome://extensions`
2. Enable Developer Mode
3. Click "Load unpacked"
4. Select `extension/` folder

---

## Future Improvements

- Dynamic DOM analysis
- AI-based dark pattern classification
- Better visual analysis
- Advanced cookie trap detection

---

## Credits

## Credits

This project uses the open-source scraping framework:

### Scrapling
An adaptive modern web scraping framework for browser automation and dynamic website scraping.

GitHub Repository:
https://github.com/D4Vinci/Scrapling

Special thanks to the Scrapling contributors and maintainers for building such a powerful scraping ecosystem.
---

## Disclaimer

This project is built for educational and research purposes only.