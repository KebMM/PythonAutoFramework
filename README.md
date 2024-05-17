# Python Automation Framework

## Overview
This framework is designed to simplify automated testing for various domains including UI, API, Database, and Mobile. It supports both BDD (Behavior-Driven Development) and TDD (Test-Driven Development) approaches, making it versatile and user-friendly. With pre-built components and comprehensive training materials, users can quickly start writing and running tests with minimal setup.

## Features
Python-based BDD and TDD frameworks
UI Automation Capability
API Automation Capability
Database Automation Capability
Mobile Automation Capability
Sufficient Reporting Tool
Training Materials
Sample Implementations
Getting Started
## Prerequisites
Ensure you have the following installed on your system:

Python 3.7+
pip (Python package installer)
Google Chrome (for UI tests)

## Getting Started 
Once the repository has been cloned, cd into the path of the repository and install the necessary dependencies:
```
pip install -r requirements.txt
```

## Framework Structure
File structure will go here e.g
- features/: Contains feature files for BDD tests.
- steps/: Contains step definitions for BDD tests.
- tests/: Contains TDD test cases.
- commonUISteps.py: Pre-built UI automation methods.
- reports/: Directory for test reports.

## UI Automation
### BDD with Behave:
1. Ensure Behave is installed (This should have been installed when installing dependencies)
```
pip install behave
```
2. Write Feature Files


    Feature files are written in Gherkin syntax and are located in the features/ directory.

    Example feature file (features/tutorial.feature):
```
Feature: Get elements text

  Scenario: Retrieve text from elements on the page
    Given the browser is open
    When we navigate to "http://example.com"
    Then we get text of elements by locator "/html/body/div/h1"
    And the text of elements should be printed
```

3. Define Steps

   Step definitions are in the steps/ directory. This is where the test code is written. Example:
```
from behave import given, when, then
from selenium import webdriver
from features.commonUISteps import CommonUISteps
import time

@given('the browser is open')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('we navigate to "{url}"')
def step_impl(context, url):
    context.driver.get(url)

@then('we get text of elements by locator "{locator}"')
def step_impl(context, locator):
    CommonUISteps.get_elements_text(context, locator)

@then('the text of elements should be printed')
def step_impl(context):
    pass
```

4. Run the test using the following command:
```
behave
```
