from selenium import webdriver

def get_driver(browser_name):
    if browser_name.lower() == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser_name.lower() == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    
    driver.maximize_window()
    return driver


# from selenium import webdriver

# def get_driver(browser_name):
#     if browser_name == "chrome":
#         options = webdriver.ChromeOptions()
#         return webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         options = webdriver.FirefoxOptions()
#         return webdriver.Firefox(options=options)
#     elif browser_name == "edge":
#         options = webdriver.EdgeOptions()
#         return webdriver.Edge(options=options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
