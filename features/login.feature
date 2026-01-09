Feature: Role Based Login

Scenario: Admin login redirects to admin dashboard
  Given user opens login page
  When user logs in as admin
  Then user should land on admin dashboard
