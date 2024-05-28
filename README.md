# Python Automation Framework

## Overview
This framework is designed to simplify automated testing for various domains including UI, API, Database, and Mobile. It supports both BDD (Behavior-Driven Development) and TDD (Test-Driven Development) approaches, making it versatile and user-friendly. With pre-built components and comprehensive training materials, users can quickly start writing and running tests with minimal setup.

## Features
- Python-based BDD and TDD frameworks
- UI Automation Capability
- API Automation Capability
- Database Automation Capability
- Mobile Automation Capability
- Sufficient Reporting Tool
- Training Materials
- Sample Implementations
- Getting Started
  
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
- apiAutomation/
- steps/: Contains step definitions for BDD tests.
- tests/: Contains TDD test cases.
- commonUISteps.py: Pre-built UI automation methods.
- reports/: Directory for test reports.<br />

PythonAutoFramework/<br />
│<br />
├── apiAutomation/<br />
│ ├── init.py<br />
│ └── commonAPISteps.py<br />
│<br />
├── uiAutomation/<br />
│ ├── init.py<br />
│ └── commonUISteps.py<br />
│<br />
├── tests/<br />
│ ├── init.py<br />
│ ├── api/<br />
│ │ ├── init.py<br />
│ │ └── test_api.py<br />
│ └── ui/<br />
│ ├── init.py<br />
│ └── test_ui.py<br />
│<br />
├── features/<br />
│ ├── steps/<br />
│ │ └── apiSteps.py<br />
│ └── tutorial.feature<br />
│<br />
├── requirements.txt<br />
└── README.md<br />

## BDD Testing with Behave:
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

   Step definitions are in the steps/ directory. This is where the test code is written. <br />
   All BDD tests must include the "load module" function to import the pre-built components <br />
   Example:
```
from behave import given, when, then
from selenium import webdriver
from features.commonUISteps import CommonUISteps
import time

#set path of commonUISteps.py and load the module
common_ui_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../uiAutomation/commonUISteps.py'))
spec = importlib.util.spec_from_file_location("commonUISteps", common_ui_steps_path)
commonUISteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonUISteps)


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

For additional information about Behave please visit ...
## TDD Testing with PyTest:
1. Ensure PyTest is installed (This should have been installed when installing dependencies)
```
pip install pytest
```

2. Writing Tests

   Pytests should be placed in the 'tests/' directory. PyTest will automatically discover and run any test files that start with test_ or end with _test.py.<br />
   <br />
Here's an example of a Pytest file, 'test_ui.py':
```
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_navigate_to_example(driver):
    driver.get("http://example.com")
    assert "Example Domain" in driver.title

def test_get_element_text(driver):
    driver.get("http://example.com")
    element = driver.find_element_by_xpath("/html/body/div/h1")
    assert element.text == "Example Domain"
```

3. Running Tests

To run all tests in the 'tests/' directory, use the following command:
```
pytest
```

   To run a specific test file, provide the path to the file:
```
pytest tests/ui/test_ui.py
```

   To run a specific test function within a file, use the following command:
```
pytest tests/api/test_api.py::test_get_element_text
```

For additional information about PyTest please visit ...
## UI Automation
UI automation in this framework uses Selenium WebDriver to interact with web pages. The 'uiAutomation/' directory contains pre-built methods for common UI operations in the 'commonUISteps.py' file.

### Testing UI with Behave
- Follow the steps outlined in the BDD Testing with Behave section.
- Sample UI tests using Behave can be found in the 'features/steps/' directory, such as 'apiSteps.py'.

### Testing UI with PyTest
- Follow the steps outlined in the TDD Testing with PyTest section.
- Sample UI tests using PyTest can be found in the 'tests/ui/' directory, such as 'test_ui.py'.

## API Automation
API automation in this framework uses requests and other libraries to interact with APIs. The 'apiAutomation/' directory contains pre-built methods for common API operations in the 'commonAPISteps.py' file.

### Testing API with Behave
- Follow the steps outlined in the BDD Testing with Behave section.
- Sample API tests using Behave can be found in the 'features/steps/' directory, such as 'apiSteps.py'.
### Testing API with PyTest
- Follow the steps outlined in the TDD Testing with PyTest section.
- Sample API tests using PyTest can be found in the 'tests/api/' directory, such as 'test_api.py'.
