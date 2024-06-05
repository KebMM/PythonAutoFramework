from behave import *
from selenium import webdriver

driver = webdriver.Chrome()

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    driver.get("https://example.com")

@then('behave will test it for us!')
def step_impl(context):
    assert "Example Domain" in driver.title

def after_all(context):
    driver.quit()

# Keep the browser window open
input("Press Enter to close the browser...")
