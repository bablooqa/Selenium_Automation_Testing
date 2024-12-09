from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Helper.Helper import WebDriverHelper
from Locators.LoginLocators import LoginLocators
import allure
from logging_config import logger  # Import logger
from logging_config import allure_log

@given('the user has "{credentials_type}" login credentials on "{browser}"')
def step_given_credentials(context, credentials_type, browser):
    with allure.step(f"Setting up {credentials_type} login credentials and opening the login page on {browser}"):
        allure_log(f"Setting up {credentials_type} login credentials")

        # Set valid or invalid credentials based on the example data
        credentials = {
            "valid": ("admin", "admin123"),
            "invalid": ("Admin1", "admin12345")
        }
        context.username, context.password = credentials.get(credentials_type, ("", ""))

        # Initialize WebDriver and open login page for specified browser
        context.driver = WebDriverHelper.get_driver(browser=browser)
        allure_log(f"Opening the login page URL in {browser} browser")
        context.driver.get("https://opensource-demo.orangehrmlive.com/")
        allure.attach(context.driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)

@when('the user enters the username "{username}" and password "{password}"')
def step_when_enter_login_credentials(context, username, password):
    with allure.step("Entering provided username and password"):
        allure_log("Entering username and password")

        # Fill in the username and password fields
        username_field = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)
        allure_log(f"Entered username: {username}")

        password_field = context.driver.find_element(*LoginLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        allure_log("Entered password: [HIDDEN]")

        # Click the login button
        login_button = context.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()
        allure_log("Clicked the login button")

@then('the user should be "{login_status}"')
def step_then_check_login_status(context, login_status):
    with allure.step("Verifying login status based on provided credentials"):
        allure_log(f"Checking if the user is {login_status}")

        try:
            if login_status == "successfully logged in":
                # Wait for dashboard to be visible
                dashboard_header = WebDriverHelper.wait_for_element(context.driver, LoginLocators.DASHBOARD_HEADER)
                assert "Dashboard" in dashboard_header.text, "Dashboard message is not displayed or incorrect"
                allure_log("Dashboard is displayed successfully")
                allure.attach(context.driver.get_screenshot_as_png(), name="Dashboard Page", attachment_type=allure.attachment_type.PNG)
            else:
                # Check if login form is displayed, indicating an unsuccessful login
                login_form = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
                assert login_form.is_displayed(), "User is logged in, but they shouldn't be"
                allure_log("User is not logged in as expected")
        except TimeoutException:
            allure_log(f"TimeoutException: Expected {login_status} but did not load")
            raise AssertionError(f"{login_status} did not occur as expected")

@then('"{expected_result}" should be displayed')
def step_then_check_expected_result(context, expected_result):
    with allure.step("Verifying the expected result on the page"):
        allure_log(f"Checking if {expected_result} is displayed")

        try:
            if expected_result == "correct profile page":
                profile_element = WebDriverHelper.wait_for_element(context.driver, LoginLocators.PROFILE_DROPDOWN)
                assert profile_element.is_displayed(), "Profile page is not displayed correctly"
                allure_log("Profile page displayed correctly")
                allure.attach(context.driver.get_screenshot_as_png(), name="Profile Page", attachment_type=allure.attachment_type.PNG)
            elif expected_result == "error message":
                error_message = WebDriverHelper.wait_for_element(context.driver, LoginLocators.ERROR_MESSAGE)
                assert "Invalid credentials" in error_message.text, "Error message not displayed or incorrect"
                allure_log("Error message displayed correctly")
                allure.attach(context.driver.get_screenshot_as_png(), name="Error Message", attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            allure_log(f"TimeoutException: {expected_result} not found")
            raise AssertionError(f"{expected_result} not displayed as expected")

@then("the user should be able to log out successfully")
def step_then_logout_and_verify(context):
    with allure.step("Logging out and verifying the user is redirected to the login page"):
        allure_log("Logging out the user")

        # Click profile dropdown to access logout option
        profile_dropdown = WebDriverHelper.wait_for_element(context.driver, LoginLocators.PROFILE_DROPDOWN)
        profile_dropdown.click()
        allure_log("Clicked on the profile dropdown")

        # Select logout option
        logout_option = WebDriverHelper.wait_for_element(context.driver, LoginLocators.LOGOUT_OPTION)
        logout_option.click()
        allure_log("Clicked the logout option")

        # Verify redirection to login page
        login_page_element = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        assert login_page_element.is_displayed(), "User is not redirected to the login page after logout"
        allure_log("User successfully logged out and redirected to the login page")
