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
UI automation in this framework uses Selenium WebDriver to interact with web pages. The 'uiAutomation/' directory contains pre-built methods for common UI operations in the 'commonUISteps.py' file. You can edit and add to this file to create custom methods for further testing. UI can be tested in either BDD or TDD using any testing library you wish to. For our examples we have primarily used Behave for BDD and PyTest for TDD, as seen above. 

### Testing UI with Behave
- Follow the steps outlined in the BDD Testing with Behave section.
- Sample UI tests using Behave can be found in the 'features/steps/' directory, such as 'apiSteps.py'.

### Testing UI with PyTest
- Follow the steps outlined in the TDD Testing with PyTest section.
- Sample UI tests using PyTest can be found in the 'tests/ui/' directory, such as 'test_ui.py'.

## API Automation
API automation in this framework uses requests and other libraries to interact with APIs. The 'apiAutomation/' directory contains pre-built methods for common API operations in the 'commonAPISteps.py' file. ou can edit and add to this file to create custom methods for further testing. API can be tested in either BDD or TDD using any testing library you wish to.

### Testing API with Behave
- Follow the steps outlined in the BDD Testing with Behave section.
- Sample API tests using Behave can be found in the 'features/steps/' directory, such as 'apiSteps.py'.
### Testing API with PyTest
- Follow the steps outlined in the TDD Testing with PyTest section.
- Sample API tests using PyTest can be found in the 'tests/api/' directory, such as 'test_api.py'.

## Mobile Automation
Mobile automation in this framework uses Appium to interact with mobile applications. The 'mobileAutomation/' directory contains pre-built methods for common mobile operations in the 'commonMobileSteps.py' file. For mobile testing we recommend using python's built in testing module, 'unittest', and have provided an example of how to create a test using this module below. Mobile tests can also be written using other TDD or BDD testing frameworks, like Pytest or Behave.

### Prerequisites for Mobile Testing
Ensure you have the following installed and configured:
- Appium server
- Android SDK
- Java JDK
- Android Virtual Device (AVD) or a real device connected

### Setting Up Appium
1. Install Appium:
   ```
   npm install -g appium
   ```
2. Start Appium server:
   ```
   appium
   ```

### Testing Mobile with unittest
Inside the 'tests/mobile' directory create a test file that either start with 'test_' or ends with '_test.py' . We have a sample test inside this directory called 'test_mobile.py'. Below you can see how we structured our sample mobile test:
```
import unittest
import os
import importlib.util
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Path to the commonMobileSteps.py
common_mobile_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../mobileAutomation/commonMobileSteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonMobileSteps", common_mobile_steps_path)
commonMobileSteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonMobileSteps)

class TestAppium(unittest.TestCase):
    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "platformVersion": "11.0",
            "app": os.path.abspath(r'C:\k\All Search Engines_1.0_apkcombo.com.apk'),
            "automationName": "UiAutomator2",
            "ensureWebviewsHavePages": "true"
        }

        options = UiAutomator2Options()
        options.load_capabilities(capabilities)

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        self.mobile_steps = commonMobileSteps.CommonMobileSteps(self.driver)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

  def test_scroll_and_screenshot(self):
            self.mobile_steps.wait_for_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')
            self.mobile_steps.click_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')
            # Wait for the input field and send text
            self.mobile_steps.wait_for_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')

            # Scroll to the element using description
            self.mobile_steps.scroll_to_element(AppiumBy.ANDROID_UIAUTOMATOR, 'Download the DuckDuckGo App')

            # Wait for the element after scrolling and take a screenshot
            self.mobile_steps.wait_for_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Download the DuckDuckGo App"]/android.widget.TextView')
            self.mobile_steps.take_screenshot('screenshot.png')

if __name__ == '__main__':
    unittest.main()
```
To run the mobile test, use the following command:
```
python nameOfTest
```

## Using the Reporting Tool
For this framework we use Allure as a reporting tool...

### Allure in PyTest

1. Import allure:
```
import allure
```
2. Use Allure annotations to add metadata to your tests:
```
@allure.feature('Feature Name')
@allure.story('Story Name')
def test_example():
    pass
```
3. Execute the tests and generate Allure results:
```
pytest --alluredir=allure-results
```
4. Use the Allure command-line tool to open a web server and display the test results in your browser
```
allure serve allure-results
```
Here is an example pytest that uses allure:
```
import pytest
import allure
import os
import importlib.util
from selenium import webdriver
from selenium.webdriver.common.by import By

# Path to the commonUISteps.py
common_ui_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../uiAutomation/commonUISteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonUISteps", common_ui_steps_path)
commonUISteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonUISteps)

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature('UI Tests')
@allure.story('Get Element Text')
def test_get_element_text(driver):
    commonUISteps.CommonUISteps.launch_web_browser(driver, "http://example.com")

    with allure.step("Get text of the element"):
        text = commonUISteps.CommonUISteps.get_elements_text(driver, (By.XPATH, "/html/body/div/h1"))
        assert text[0] == "Example Domain"
```
When the 'allure serve allure-results' command is run, you will be able to view detailed information about each test, including steps, attachments, and failures. <br />
For further information on Allure reporting please visit...
