from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

class WebDriverHelper:
    @staticmethod
    def get_chrome_driver():
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize the browser window
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def get_firefox_driver():
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")  # Maximize the browser window
        return webdriver.Firefox(options=firefox_options)

    @staticmethod
    def get_driver(browser="chrome"):
        """ 
        Get the WebDriver instance based on the specified browser. 
        Supported browsers: 'chrome', 'firefox'.
        """
        if browser.lower() == "firefox":
            return WebDriverHelper.get_firefox_driver()
        else:
            return WebDriverHelper.get_chrome_driver()

    @staticmethod
    def take_screenshot(driver, file_name="screenshot.png"):
        """ Take a screenshot and save it to the 'screenshots' directory. """
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        file_path = os.path.join(screenshots_dir, file_name)
        driver.save_screenshot(file_path)
        print(f"Screenshot saved at: {file_path}")

    @staticmethod
    def close_driver(driver):
        """ Close the browser and quit the WebDriver instance. """
        driver.quit()

    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """ Wait for an element to be visible on the page. """
        try:
            element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None
