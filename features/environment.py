from Helper.Helper import WebDriverHelper
from logging_config import logger  # Import logger from logging_config.py
import allure
from logging_config import allure_log
from Webdriver.webdriver import get_driver  # Import your get_driver function

def before_all(context):
    allure_log("Starting all tests")

    # Retrieve the browser from the command line argument (or default to "chrome")
    context.browser = context.config.userdata.get('browser', 'chrome')
    if not context.browser:
        context.browser = 'chrome'  # Default to chrome if the browser is not specified

    print(f"Browser in before_all: {context.browser}")
    
    try:
        # Initialize the driver using the get_driver function
        context.driver = get_driver(context.browser)
        print(f"Using browser: {context.browser}")
        print(f"Driver initialized with {context.browser} browser.")
    except Exception as e:
        logger.error(f"Failed to initialize WebDriver for browser '{context.browser}': {e}")
        allure_log(f"WebDriver initialization failed for browser '{context.browser}'")
        raise e  # Raising exception to stop the test run

def before_scenario(context, scenario):
    allure_log(f"Starting scenario: {scenario.name}")
    
    browser = context.browser
    try:
        # Initialize WebDriver for the specified browser
        context.driver = WebDriverHelper.get_driver(browser=browser)
        context.driver.implicitly_wait(10)  # Optional: Set an implicit wait
    except Exception as e:
        logger.error(f"Failed to initialize WebDriver for browser '{browser}': {e}")
        allure_log(f"WebDriver initialization failed for browser '{browser}'")
        raise e  # Raising exception to stop the scenario

def after_scenario(context, scenario):
    if scenario.status == "failed":
        logger.error(f"Scenario failed: {scenario.name}")  # Log failed scenario
        screenshot_path = WebDriverHelper.take_screenshot(context.driver, f"{scenario.name}_failure.png")
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)
    else:
        allure_log(f"Scenario passed: {scenario.name}")  # Log passed scenario

    with open('logs/test_log.log', 'r') as log_file:
        allure.attach(log_file.read(), name="Test Log", attachment_type=allure.attachment_type.TEXT)

    if context.driver:
        WebDriverHelper.close_driver(context.driver)
        context.driver = None  # Reset the driver to None

def after_all(context):
    allure_log("All tests completed")
    
    # Quit the driver after all tests
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
