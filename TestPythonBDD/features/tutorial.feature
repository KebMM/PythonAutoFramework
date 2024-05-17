# Feature: Screenshot Testing

#   Scenario: Take a screenshot
#     Given the browser is open
#     When we navigate to "https://www.example.com"
#     When we take a screenshot with filename "test_screenshot"
#     Then a screenshot file "test_screenshot" should be created

# Feature: Testing common steps

#   Scenario: Click step is used
#       Given the click step exists
#       When we run this step
#       #Then behave will click the identifier
#       Then the browser will remain open

# Feature: Testing alert methods

#   Scenario: Accept alert
#     Given the click step exists
#     When we run this step
#     Then we should be able to accept the alert

#   Scenario: Dismiss alert
#     Given the click step exists
#     When we run this step
#     Then we should be able to dismiss the alert

#   Scenario: Get alert text
#     Given the click step exists
#     When we run this step
#     Then we should be able to get the alert text

#   Scenario: Send text to alert
#     Given the click step exists
#     When we run this step
#     Then we should be able to send text to the alert

#Feature: Wait Methods Testing

  # Scenario: Wait for a specific duration
  #   Given the browser is open
  #   When we navigate to "https://www.example.com"
  #   Then we wait for 5 seconds

  # Scenario: Wait for visibility of a specific element
  #   Given the browser is open
  #   When we navigate to "https://www.example.com"
  #   Then we wait for visibility of element "/html/body/div/p[2]/a" for 10 seconds

  # Scenario: Wait for visibility of element by locator
  #   Given the browser is open
  #   When we navigate to "https://www.example.com"
  #   Then we wait for visibility of element by "/html/body/div/p[2]/a" for 10 seconds


  # Scenario: Wait for clickability of a specific element
  #   Given the browser is open
  #   When we navigate to "https://www.example.com"
  #   Then we wait for clickability of element "/html/body/div/p[2]/a" for 10 seconds

  # Scenario: Wait for presence of a specific element
  #   Given the browser is open
  #   When we navigate to "https://www.example.com"
  #   Then we wait for presence of element "/html/body/div/p[2]/a" for 10 seconds


Feature: Get elements text

  Scenario: Retrieve text from elements on the page
    Given the browser is open
    When we navigate to "C:\Users\kebba.mm\OneDrive - Infuse Consulting Limited\Desktop\TestPythonBDD\features\test_alerts.html"
    Then we send "Test User" to the alert
    Then we print the alert text
