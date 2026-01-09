from behave import given, when, then
from playwright.sync_api import sync_playwright
import os

@given("user opens login page")
def step_open(context):
    context.p = sync_playwright().start()
    context.browser = context.p.chromium.launch(headless=False)
    context.page = context.browser.new_page()

    file_path = os.path.abspath("sample_app/index.html")
    context.page.goto(f"file:///{file_path}")

@when("user logs in as admin")
def step_admin_login(context):
    context.page.fill("#username", "admin")
    context.page.fill("#password", "admin123")
    context.page.click("button")

@then("user should land on admin dashboard")
def step_verify_admin_dashboard(context):
    context.page.wait_for_url("**/dashboard.html")
    assert "Dashboard" in context.page.title()

    context.browser.close()
    context.p.stop()
