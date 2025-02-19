import pytest
import os
import importlib.util
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Path to the commonUISteps.py
common_ui_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../uiAutomation/commonUISteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonUISteps", common_ui_steps_path)
commonUISteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonUISteps)

TestLogger = commonUISteps.TestLogger

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_demo(driver):
    start_time = time.time()

    try:
        commonUISteps.CommonUISteps.launch_web_browser(driver, "https://practise.usemango.co.uk/")
        TestLogger.log_test_step("Launched browser", "PASS")

        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='products']"))
        TestLogger.log_test_step("Go to 'Products' page", "PASS")

        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/div/div/div[2]/div[4]/div/div/div/div/a[2]"))
        TestLogger.log_test_step("Add laptop to basket", "PASS")

        element = commonUISteps.CommonUISteps.wait_for_clickability(driver, (By.XPATH, "//*[@id='searchproduct']"), timeout=10)
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='products']"))
        commonUISteps.CommonUISteps.send_text(element, "AirPods")
        TestLogger.log_test_step("Click search bar and enter product name", "PASS")

        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/div/div/div[2]/div/div/div/div/div/a[2]"))
        TestLogger.log_test_step("Add AirPods to basket", "PASS")

        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='navbarNavAltMarkup']/div[2]/a[2]"))
        TestLogger.log_test_step("Go to basket", "PASS")

        text = commonUISteps.CommonUISteps.get_elements_text(driver, (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/h5"))
        assert text[0] == "AirPods Pro"
        TestLogger.log_test_step("Check item in basket", "PASS")

        commonUISteps.CommonUISteps.wait_for(seconds=4)
        commonUISteps.CommonUISteps.scroll_to_bottom(driver)
        commonUISteps.CommonUISteps.click(driver, (By.XPATH, "//*[@id='root']/footer/div/div/div[1]/div/div[2]/a"))
        commonUISteps.CommonUISteps.wait_for(3)
        TestLogger.log_test_step("Go to Contact Us page", "PASS")

        test_status = "PASS"

    except Exception as e:
        test_status = "FAIL"
        TestLogger.log_test_step(str(e), "FAIL")

    end_time = time.time()
    execution_time = round(end_time - start_time, 2)

    test_result = {
        "test_name": "test_demo",
        "status": test_status,
        "execution_time": execution_time,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }

    with open("test_results.json", "a") as f:
        json.dump(test_result, f)
        f.write("\n")
