from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By
import time
from datetime import datetime
from selenium import webdriver

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

import sys
import logging
import importlib.util
import os

# Path to the commonUISteps.py
common_ui_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../uiAutomation/commonUISteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonUISteps", common_ui_steps_path)
commonUISteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonUISteps)

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define global variable
driver = None

@given('the browser is open')
def step_impl(context):
    global driver
    driver = webdriver.Chrome()
    context.driver = driver

@when('we navigate to "{url}"')
def step_impl(context, url):
    driver.get(url)

@then('we send "{text}" to the alert')
def step_impl(context, text):
    time.sleep(5)
    commonUISteps.CommonUISteps.send_alert_text(context, text)

@then('we print the alert text')
def step_impl(context):
    time.sleep(5)

    # Clean up
    driver.quit()


# from behave import given, when, then
# from PIL import Image
# from features.commonUISteps import CommonUISteps
# import os

# @given('the image file "{image_name}" exists')
# def step_impl(context, image_name):
#     base_dir = os.getcwd()
#     relative_path = os.path.join("images")
#     file_path = os.path.join(base_dir, relative_path, f"{image_name}.png")
#     assert os.path.exists(file_path), f"Image file {file_path} does not exist"

# @when('we click on the image "{image_name}"')
# def step_impl(context, image_name):
#     CommonUISteps.click_on_image(image_name)

# @then('the image "{image_name}" should be clicked successfully')
# def step_impl(context, image_name):
#     # This step is more of a placeholder since the action of clicking
#     # is already handled in the @when step. If there's specific behavior
#     # to verify after clicking, add that verification here.
#     pass


#     # Clean up
#     # driver.quit()
