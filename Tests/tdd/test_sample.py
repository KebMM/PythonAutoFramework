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
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature('UI Tests')
@allure.story('Demo Test')
def test_demo(driver):
    with allure.step("Launch browser and navigate to demo website"):
        commonUISteps.CommonUISteps.launch_web_browser(driver, "https://practise.usemango.co.uk/")

    with allure.step("Go to 'Products' page"):
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='products']"))

    with allure.step("Add laptop to basket"):
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/div/div/div[2]/div[4]/div/div/div/div/a[2]"))

    with allure.step("Click search bar and enter product name"):
        element = commonUISteps.CommonUISteps.wait_for_clickability(driver, (By.XPATH, "//*[@id='searchproduct']"), timeout=10)
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='products']"))
        commonUISteps.CommonUISteps.send_text(element, "AirPods")

    with allure.step("Add airpods to basket"):
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div/div/div/a[2]"))

    with allure.step("Go to basket"):
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='navbarNavAltMarkup']/div[2]/a[2]"))

    with allure.step("Check item in basket"):
        text = commonUISteps.CommonUISteps.get_elements_text(driver, (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/h5"))
        assert text[0] == "AirPods Pro"

    with allure.step("Go to Contact Us page"):
        commonUISteps.CommonUISteps.wait_for(seconds=4)
        commonUISteps.CommonUISteps.scroll_to_bottom(driver)
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/footer/div/div/div[1]/div/div[2]/a"))
        commonUISteps.CommonUISteps.wait_for(3)
