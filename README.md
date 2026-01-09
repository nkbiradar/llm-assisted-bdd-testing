# LLM-Assisted BDD Functional Testing

## Overview
This project demonstrates a simple and practical approach to functional testing
using LLM-assisted BDD. Plain English business requirements are converted into
Gherkin scenarios, validated, manually approved, and selectively automated.

Only happy-path scenarios are automated to ensure reliability and control.

---

## Project Flow
Business Requirement → BDD Scenario Generation → Validation → Manual Approval →
BDD Automation → Dashboard Visualization

---

## Tech Stack
- Python
- Behave (BDD)
- Playwright
- HTML, CSS, JavaScript
- JSON for reporting

---

## How to Run

```bash
python run.py


After execution, open:
sample_app/dashboard.html


Notes

Admin login represents the automated happy path

User login is documented but not automated

Approval is done by a tester (human-in-the-loop)

Author

Nayan Kumar Biradar


---
