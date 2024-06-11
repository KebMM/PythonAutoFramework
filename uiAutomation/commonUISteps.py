from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedTagNameException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
import os
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import base64
import time
from PIL import Image
import numpy as np
import logging

class SimpleLogHandler(logging.Handler):
    def emit(self, record):
        print(record.getMessage())

# Setup logging configuration
logger = logging.getLogger('Text')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)



class CommonUISteps:
    @staticmethod
    def launch_web_browser(driver, url):
        driver.get(url)

    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def click_with_actions(context, element):
        actions = ActionChains(context.driver)
        actions.click(element).perform()

    @staticmethod
    def double_click_with_actions(context, element):
        actions = ActionChains(context.driver)
        actions.double_click(element).perform()

    @staticmethod
    def right_click_with_actions(context, element):
        actions = ActionChains(context.driver)
        actions.context_click(element).perform()

    @staticmethod
    def click_with_timeout(driver, element, timeout):
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of(element))
        element.click()

    @staticmethod
    def click_and_hold(context, element):
        actions = ActionChains(context.driver)
        actions.click_and_hold(element).perform()

    @staticmethod
    def release_element(context):
        actions = ActionChains(context.driver)
        actions.release().perform()

    @staticmethod
    def click_coordinates(x, y):
        pyautogui.click(x, y)

    @staticmethod
    def send_text(element, text):
        element.send_keys(text)

    @staticmethod
    def move_mouse_to_coordinates(x, y):
        pyautogui.moveTo(x, y)

    @staticmethod
    def get_elements_text(driver, locator):
        elements = driver.find_elements(*locator)
        elem_texts = [el.text for el in elements]
        for text in elem_texts:
            logger.info(text)
        return elem_texts

    @staticmethod
    def verify_element_displayed(context, locator, timeout=10):
        try:
            element = WebDriverWait(context.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            assert element.is_displayed(), f"Element is not displayed: {locator}"
            print(f"Element is displayed: {locator}")
        except NoSuchElementException as e:
            e.printStackTrace()
            assert False, f"Element not found: {locator}"
        except TimeoutException as e:
            assert False, f"Element is not displayed: {locator}"

    @staticmethod
    def verify_element_not_displayed(context, locator, timeout=5):
        try:
            WebDriverWait(context.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            print(f"Element is not displayed: {locator}")
        except TimeoutException:
            assert False, f"Element is still displayed: {locator}"


    @staticmethod
    def scroll_to_element(context, element):
        context.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_down_by_pixels(context, pixels):
        context.driver.execute_script("window.scrollBy(0, arguments[0]);", pixels)

    @staticmethod
    def scroll_up_by_pixels(context, pixels):
        context.driver.execute_script("window.scrollBy(0, -arguments[0]);", pixels)

    @staticmethod
    def scroll_to_bottom(context):
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @staticmethod
    def scroll_to_top(context):
        context.driver.execute_script("window.scrollTo(0, 0);")

    @staticmethod
    def hover_over_element(context, element):
        actions = ActionChains(context.driver)
        actions.move_to_element(element).perform()

    @staticmethod
    def set_attribute(context, element, attribute_name, attribute_value):
        script = "arguments[0].setAttribute(arguments[1], arguments[2]);"
        context.driver.execute_script(script, element, attribute_name, attribute_value)

    @staticmethod
    def highlight_element(context, element):
        # Store original style so it can be restored later
        original_style = element.get_attribute("style")

        # Highlight element by changing background and border color
        context.driver.execute_script(
            "arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
            element
        )

        # Wait for a short period to allow visual confirmation
        WebDriverWait(context.driver, 1).until(
            EC.staleness_of(element)
        )

        # Restore original style
        context.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            original_style
        )

    @staticmethod
    def select_checkbox(element, check):
        if check and not element.is_selected():
            element.click()
        elif not check and element.is_selected():
            element.click()

    from selenium.webdriver.support.ui import Select

    @staticmethod
    def select_dropdown_by_text(dropdown_element, text_to_select):
        try:
            # Click the dropdown to open it
            dropdown_element.click()

            # Locate the dropdown options
            dropdown_options = dropdown_element.find_elements(By.TAG_NAME, "option")

            # Iterate through the options and click the one that matches the given text
            for option in dropdown_options:
                if option.text.strip() == text_to_select:
                    option.click()
                    break

        except Exception as e:
            print("Error occurred:", e)

    @staticmethod
    def accept_alert(context):
        try:
            alert = context.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException as e:
            print("No alert present:", e)

    @staticmethod
    def dismiss_alert(context):
        try:
            alert = context.driver.switch_to.alert
            alert.dismiss()
        except NoAlertPresentException as e:
            print("No alert present:", e)

    @staticmethod
    def get_alert_text(context):
        alert_text = None
        try:
            alert = context.driver.switch_to.alert
            alert_text = alert.text
            logger.info(alert_text)  # Log the alert text
        except NoAlertPresentException as e:
            logger.info(f"No alert present: {e}")
        return alert_text

    def send_alert_text(context, text):
        try:
            alert = context.driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()  # Confirm the alert after sending text
            logger.info(f"Sent text to alert: {text}")
        except NoAlertPresentException as e:
            logger.info(f"No alert present: {e}")
        except Exception as e:
            logger.info(f"Error interacting with alert: {e}")

    @staticmethod
    def switch_to_frame(context, name_or_id):
        try:
            context.driver.switch_to.frame(name_or_id)
        except NoSuchFrameException as e:
            print("Frame not found:", e)

    @staticmethod
    def switch_to_child_window(context):
        main_window = context.driver.current_window_handle
        all_windows = context.driver.window_handles

        for window in all_windows:
            if window != main_window:
                context.driver.switch_to.window(window)
                return window  # Return the handle of the child window

        # If no child window found, raise an exception or handle it accordingly
        raise NoSuchWindowException("No child window found.")

    @staticmethod
    def get_validation_error_message(element):
        message = element.get_attribute("validationMessage")
        return message

    @staticmethod
    def take_screenshot(driver, filename):
        # Convert driver to TakesScreenshot interface
        ts = driver

        # Get current timestamp
        date = datetime.now().strftime("%Y%m%d%H%M%S")

        # Take screenshot as bytes
        pic_bytes = ts.get_screenshot_as_base64()

        # Decode base64 bytes to image
        image_data = base64.b64decode(pic_bytes)

        # Create destination directory if it doesn't exist
        destination_dir = os.path.join(os.getcwd(), "test-output", "Screenshots")
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Save screenshot to file
        destination = os.path.join(destination_dir, f"{filename}_{date}.png")
        with open(destination, "wb") as file:
            file.write(image_data)

        return pic_bytes

    @staticmethod
    def wait_for(seconds):
        time.sleep(seconds)

    @staticmethod
    def wait_for_visibility(driver, element, time_to_wait_in_sec):
        wait = WebDriverWait(driver, time_to_wait_in_sec)
        return wait.until(EC.visibility_of(element))

    @staticmethod
    def wait_for_visibility_by(driver, locator, timeout):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_clickability(driver, locator, timeout):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @staticmethod
    def wait_for_presence_of_element(driver, by, time):
        wait = WebDriverWait(driver, time)
        return wait.until(EC.presence_of_element_located(by))

    @staticmethod
    def wait_for_page_to_load(driver, timeout_in_seconds):
        def page_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"
        wait = WebDriverWait(driver, timeout_in_seconds)
        return wait.until(page_loaded)

    @staticmethod
    def is_element_available(driver, by):
    # Set implicit wait time to 1 second
        driver.implicitly_wait(1)
        try:
            # Attempt to find the element
            element = driver.find_element(*by)
            if element.is_displayed():
                print(f"{by} element found")
                return True
        except NoSuchElementException:
            print(f"{by} element not found")
        return False

    def read_image_file(image_name):
        base_dir = os.getcwd()
        relative_path = os.path.join("images")
        file_path = os.path.join(base_dir, relative_path, f"{image_name}.png")

        try:
            image = Image.open(file_path)
            return image
        except IOError as e:
            print(f"Unable to read image file: {file_path}")
            raise e

    def are_images_similar(actual_image_path, expected_image_path, tolerance=3.0):

        actual_image = Image.open(actual_image_path)
        expected_image = Image.open(expected_image_path)

        if actual_image.size != expected_image.size:
            print("Both images should have the same dimensions")
            return False

        # Convert images to numpy arrays
        actual_image_np = np.array(actual_image)
        expected_image_np = np.array(expected_image)

        # Calculate the absolute difference between the two images
        diff = np.abs(actual_image_np - expected_image_np)

        # Sum the differences for each RGB channel
        total_diff = np.sum(diff)

        # Average difference per pixel
        avg_diff = total_diff / (actual_image_np.shape[0] * actual_image_np.shape[1] * 3)

        # Convert to percentage
        percentage_diff = (avg_diff / 255) * 100

        return percentage_diff <= tolerance

    @staticmethod
    def click_on_image(image_name, timeout=5):
        user_dir = os.getcwd()
        image_address = os.path.join(user_dir, "src", "test", "resources", "projectResources", "uiResources", "uiImages", f"{image_name}.png")

        try:
            start_time = time.time()
            while True:
                try:
                    # Locate the image on the screen
                    location = pyautogui.locateCenterOnScreen(image_address, confidence=0.8)
                    if location:
                        pyautogui.click(location)
                        print(f"Clicked on image: {image_name}")
                        break
                except pyautogui.ImageNotFoundException:
                    pass
                if time.time() - start_time > timeout:
                    raise Exception(f"Image {image_name} not found on screen")
                time.sleep(0.5)
        except Exception as e:
            print(e)


    # Implement other methods similarly
