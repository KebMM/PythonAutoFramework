from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CommonMobileSteps:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_strategy, locator, timeout=100):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_strategy, locator))
        )

    def click_element(self, locator_strategy, locator):
        self.driver.find_element(locator_strategy, locator).click()

    def send_text(self, locator_strategy, locator, text):
        self.driver.find_element(locator_strategy, locator).send_keys(text)

    def get_element_text(self, locator_strategy, locator):
        return self.driver.find_element(locator_strategy, locator).text

    def take_screenshot(self, file_name):
        self.driver.save_screenshot(file_name)

    def scroll_to_element(self, locator_strategy, locator):
            if locator_strategy == AppiumBy.XPATH:
                raise ValueError("scroll_to_element does not support XPath. Use resource-id, text, or description.")
            elif locator_strategy == AppiumBy.ID:
                scrollable_element = (f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("{locator}"))')
            elif locator_strategy == AppiumBy.ANDROID_UIAUTOMATOR:
                scrollable_element = (f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().description("{locator}"))')
            else:
                raise ValueError(f"Unsupported locator strategy: {locator_strategy}")

            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_element)
