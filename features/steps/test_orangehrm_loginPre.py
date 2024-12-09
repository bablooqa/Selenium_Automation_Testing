''' 
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Helper.Helper import WebDriverHelper
from Locators.LoginLocators import LoginLocators
import allure
from logging_config import logger  # Import logger
from logging_config import allure_log


@given("the user has valid login credentials")
def step_given_valid_credentials(context):
    with allure.step("Setting up valid login credentials and opening the login page"):
        allure_log("Setting up valid login credentials")
        context.username = "admin"
        context.password = "admin123"
        context.driver = WebDriverHelper.get_driver(browser="chrome")
        allure_log("Opening the login page URL")
        context.driver.get("https://opensource-demo.orangehrmlive.com/")
        allure.attach(context.driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)

@when("the user enters the correct username and password")
def step_when_enter_login_credentials(context):
    with allure.step("Entering valid username and password"):
        allure_log("Entering username and password")
        username_field = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        username_field.send_keys(context.username)
        allure_log("Entered username: %s", context.username)

        password_field = context.driver.find_element(*LoginLocators.PASSWORD_FIELD)
        password_field.send_keys(context.password)
        allure_log("Entered password: [HIDDEN]")

        login_button = context.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()
        allure_log("Clicked the login button")

@then("the user should be successfully logged in")
def step_then_check_login_success(context):
    with allure.step("Verifying successful login and taking a screenshot"):
        allure_log("Verifying if the user is successfully logged in")
        WebDriverHelper.take_screenshot(context.driver, "login_success.png")
        try:
            dashboard_header = WebDriverHelper.wait_for_element(context.driver, LoginLocators.DASHBOARD_HEADER)
            assert "Dashboard" in dashboard_header.text, "Dashboard message is not displayed or incorrect"
            allure_log("Dashboard is displayed successfully")
            allure.attach(context.driver.get_screenshot_as_png(), name="Dashboard Page", attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            allure_log("TimeoutException: Dashboard did not load")
            with open("page_source_debug.html", "w", encoding="utf-8") as f:
                f.write(context.driver.page_source)
            raise

@then("the correct profile page should be displayed")
def step_then_correct_profile_page_displayed(context):
    with allure.step("Checking if the correct profile page is displayed"):
        allure_log("Verifying the profile page display")
        try:
            profile_element = WebDriverHelper.wait_for_element(context.driver, LoginLocators.PROFILE_DROPDOWN)
            assert profile_element.is_displayed(), "Profile page is not displayed correctly"
            allure_log("Profile page displayed correctly")
            allure.attach(context.driver.get_screenshot_as_png(), name="Profile Page", attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            allure_log("TimeoutException: Profile page did not load")
            context.driver.save_screenshot("screenshot_profile_page_error.png")
            raise AssertionError("Profile page did not load as expected")

@then("the user should be able to log out successfully")
def step_then_logout_and_verify(context):
    with allure.step("Logging out and verifying the user is redirected to the login page"):
        allure_log("Logging out the user")
        profile_dropdown = WebDriverHelper.wait_for_element(context.driver, LoginLocators.PROFILE_DROPDOWN)
        profile_dropdown.click()
        allure_log("Clicked on the profile dropdown")

        logout_option = WebDriverHelper.wait_for_element(context.driver, LoginLocators.LOGOUT_OPTION)
        logout_option.click()
        allure_log("Clicked the logout option")

        login_page_element = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        assert login_page_element.is_displayed(), "User is not redirected to the login page after logout"
        allure_log("User successfully logged out and redirected to the login page")

@given("the user has invalid login credentials")
def step_given_invalid_credentials(context):
    with allure.step("Setting up invalid login credentials"):
        allure_log("Setting up invalid login credentials")
        context.username = "Admin1"
        context.password = "admin12345"

@when("the user enters the incorrect username and password")
def step_when_enter_invalid_login_credentials(context):
    with allure.step("Entering invalid username and password"):
        allure_log("Entering invalid username and password")
        context.driver.get("https://opensource-demo.orangehrmlive.com/")
        username_field = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(context.username)
        allure_log("Entered invalid username: %s", context.username)

        password_field = context.driver.find_element(*LoginLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(context.password)
        allure_log("Entered invalid password: [HIDDEN]")

        login_button = context.driver.find_element(*LoginLocators.LOGIN_BUTTON)
        login_button.click()
        allure_log("Clicked the login button with invalid credentials")

@then("the user should see an error message")
def step_then_check_error_message(context):
    with allure.step("Verifying the error message is displayed"):
        allure_log("Checking for error message on login failure")
        try:
            error_message = WebDriverHelper.wait_for_element(context.driver, LoginLocators.ERROR_MESSAGE)
            assert "Invalid credentials" in error_message.text, "Error message not displayed or incorrect"
            allure_log("Error message displayed correctly")
            allure.attach(context.driver.get_screenshot_as_png(), name="Error Message", attachment_type=allure.attachment_type.PNG)
        except TimeoutException:
            allure_log("TimeoutException: Error message not found")
            context.driver.save_screenshot("screenshot_invalid_credentials.png")
            raise

@then("the user should not be logged in")
def step_then_check_not_logged_in(context):
    with allure.step("Checking that the user is not logged in"):
        allure_log("Verifying that the user is not logged in")
        login_form = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
        assert login_form.is_displayed(), "User is logged in, but they shouldn't be"
        allure_log("User is not logged in as expected")
'''
# Version 2
'''

from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Helper.Helper import WebDriverHelper
from Locators.LoginLocators import LoginLocators
import allure
from logging_config import logger  # Import logger
from logging_config import allure_log


@given('the user has "{credentials_type}" login credentials')
def step_given_credentials(context, credentials_type):
    with allure.step(f"Setting up {credentials_type} login credentials and opening the login page"):
        allure_log(f"Setting up {credentials_type} login credentials")
        # Set valid or invalid credentials based on the example data
        if credentials_type == "valid":
            context.username = "admin"
            context.password = "admin123"
        else:
            context.username = "Admin1"
            context.password = "admin12345"
        
        # Initialize WebDriver and open login page
        context.driver = WebDriverHelper.get_driver(browser="chrome")
        allure_log("Opening the login page URL")
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
        if login_status == "successfully logged in":
            try:
                dashboard_header = WebDriverHelper.wait_for_element(context.driver, LoginLocators.DASHBOARD_HEADER)
                assert "Dashboard" in dashboard_header.text, "Dashboard message is not displayed or incorrect"
                allure_log("Dashboard is displayed successfully")
                allure.attach(context.driver.get_screenshot_as_png(), name="Dashboard Page", attachment_type=allure.attachment_type.PNG)
            except TimeoutException:
                allure_log("TimeoutException: Dashboard did not load")
                raise AssertionError("Dashboard did not load as expected")
        else:
            # Check that login form is still displayed, indicating unsuccessful login
            login_form = WebDriverHelper.wait_for_element(context.driver, LoginLocators.USERNAME_FIELD)
            assert login_form.is_displayed(), "User is logged in, but they shouldn't be"
            allure_log("User is not logged in as expected")


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
'''