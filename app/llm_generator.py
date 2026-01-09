def generate_gherkin(requirement):
    print("\nGenerating BDD scenarios from requirement...\n")

    return """
Feature: Login Feature

Scenario: Successful login with valid credentials
  Given user is on the login page
  When user enters valid username and password
  And user clicks login button
  Then login should be successful

Scenario: Login fails with invalid credentials
  Given user is on the login page
  When user enters invalid username or password
  Then error message should be displayed
"""
