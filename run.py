import json
import os
from datetime import datetime
from app.llm_generator import generate_gherkin
from app.validator import validate_scenarios
from app.approval import get_manual_approval

# --- Input ---
requirement = input("Enter business requirement: ")

# --- LLM Scenario Generation ---
gherkin = generate_gherkin(requirement)

# --- Validation ---
is_valid = validate_scenarios(gherkin)
approved = False
execution_status = "NOT EXECUTED"

# --- Manual Approval & Execution ---
if is_valid:
    approved = get_manual_approval()
    if approved:
        os.system("behave")
        execution_status = "PASSED"

# --- Prepare execution record ---
execution_record = {
    "requirement": requirement,
    "gherkin": gherkin,
    "validation": "PASSED" if is_valid else "FAILED",
    "approval": "APPROVED" if approved else "REJECTED",
    "execution": execution_status,
    "timestamp": str(datetime.now())
}

# --- Ensure reports folder exists ---
os.makedirs("reports", exist_ok=True)

# --- Load existing execution history ---
history = []
report_path = "reports/execution_data.json"

if os.path.exists(report_path):
    with open(report_path, "r") as f:
        try:
            history = json.load(f)
        except json.JSONDecodeError:
            history = []

# --- Append new execution ---
history.append(execution_record)

# --- Save updated history ---
with open(report_path, "w") as f:
    json.dump(history, f, indent=2)

print("\n✅ Execution data written to dashboard.")
