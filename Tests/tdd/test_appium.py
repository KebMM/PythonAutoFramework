import unittest
import os
import importlib.util
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import allure

# Path to the commonMobileSteps.py
common_mobile_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../mobileAutomation/commonMobileSteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonMobileSteps", common_mobile_steps_path)
commonMobileSteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonMobileSteps)

@allure.feature('Mobile Tests')
@allure.story('Click and Send Text')
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

    @allure.step('Test clicking and sending text')
    def test_click_and_send_text(self):
        with allure.step("Open app"):
            # Wait for the first element and click
            self.mobile_steps.wait_for_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')
            self.mobile_steps.click_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')

        with allure.step("Click searchbox"):
            # Wait for the second element and click
            self.mobile_steps.wait_for_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
            self.mobile_steps.click_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')

        # Wait for the input field and send text
        self.mobile_steps.wait_for_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
        self.mobile_steps.send_text(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText', 'Sample Text')

        # Wait for the text field and verify the text
        self.mobile_steps.wait_for_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
        text = self.mobile_steps.get_element_text(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')
        self.assertEqual(text, 'Sample Text')

    # def test_scroll_and_screenshot(self):
    #         self.mobile_steps.wait_for_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')
    #         self.mobile_steps.click_element(AppiumBy.ID, 'com.cglrstudios.svkttt:id/button7')
    #         # Wait for the input field and send text
    #         self.mobile_steps.wait_for_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText')

    #         # Scroll to the element using description
    #         self.mobile_steps.scroll_to_element(AppiumBy.ANDROID_UIAUTOMATOR, 'Download the DuckDuckGo App')

    #         # Wait for the element after scrolling and take a screenshot
    #         self.mobile_steps.wait_for_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Download the DuckDuckGo App"]/android.widget.TextView')
    #         self.mobile_steps.take_screenshot('screenshot.png')

if __name__ == '__main__':
    unittest.main()
