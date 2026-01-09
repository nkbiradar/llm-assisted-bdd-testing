LLM-Assisted BDD Functional Testing
📖 Overview
This project demonstrates a simple and practical approach to functional testing using LLM-assisted Behavior Driven Development (BDD).

The system converts plain English business requirements into Gherkin scenarios. These scenarios are then validated, manually approved by a human tester, and selectively automated.

Core Philosophy: Only "happy-path" scenarios are automated to ensure reliability, stability, and control.

🔄 Project Flow
The data pipeline moves through the following stages:

Business Requirement (Input)

BDD Scenario Generation (LLM)

Validation

Manual Approval (Human-in-the-loop)

BDD Automation (Execution)

Dashboard Visualization (Reporting)

🛠 Tech Stack
Language: Python

Framework: Behave (BDD)

Automation: Playwright

Frontend (Dashboard): HTML, CSS, JavaScript

Data Exchange: JSON

🚀 How to Run
1. Prerequisites
Ensure you have the necessary dependencies installed (assuming a requirements.txt exists):

Bash

pip install -r requirements.txt
playwright install
2. Execute the Script
Run the main entry point:

Bash

python run.py
3. View Results
After execution is complete, open the dashboard in your browser:

Plaintext

sample_app/dashboard.html
📋 Scope & Test Coverage
This project uses a Human-in-the-Loop approach to ensure accuracy.

Admin Login: Represents the Automated Happy Path. This flow is fully generated and executed by the script.

User Login: Documented and generated, but not automated. This demonstrates the selective nature of the automation.

Approval: Final validation is performed by a human tester before execution triggers.

👤 Author
Nayan Kumar Biradar
