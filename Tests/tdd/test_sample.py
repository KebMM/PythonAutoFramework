# test_ui.py

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
