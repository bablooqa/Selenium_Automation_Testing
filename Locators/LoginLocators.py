from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    DASHBOARD_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    PROFILE_DROPDOWN = (By.XPATH, "//img[@class='oxd-userdropdown-img']")
    LOGOUT_OPTION = (By.XPATH, "//a[text()='Logout']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Invalid credentials']")
