# LLM-Assisted BDD Functional Testing

## Overview
This project demonstrates a simple and practical approach to functional testing using **LLM-assisted Behavior Driven Development (BDD)**.

Plain English business requirements are converted into Gherkin scenarios, validated, manually approved, and selectively automated.

> **Note:** Only happy-path scenarios are automated to ensure reliability and control.

---

## Project Flow
Business Requirement &rarr; BDD Scenario Generation &rarr; Validation &rarr; Manual Approval &rarr; BDD Automation &rarr; Dashboard Visualization

---

## Tech Stack
* **Language:** Python
* **Framework:** Behave (BDD)
* **Automation:** Playwright
* **Frontend:** HTML, CSS, JavaScript
* **Reporting:** JSON

---

## How to Run

### 1. Prerequisites
Ensure you have the required libraries installed:
```bash
pip install -r requirements.txt
playwright install

## Execute Script
python run.py

## View Report
After execution, open the dashboard in your browser:
sample_app/dashboard.html

## Scope & Notes
Admin Login: Represents the automated happy path.

User Login: Documented but not automated.

Human-in-the-Loop: Approval is strictly done by a tester before execution.
