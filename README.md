<<<<<<< HEAD
# Automation_Testing_Selenium
=======
To run the tests, use the following command in the terminal:

- pytest --bdd-features-path=features

  Allure Command

1. Generate the Allure Report

- allure generate allure-results -o reports/allure-report --clean

  2.Open the Allure Report
- **allure open reports/allure-report**

All in One command

* **behave && allure generate reports/allure-results -o reports/allure-report --clean && allure serve reports/allure-report**

### Explanation:

* `behave`: This command runs your Behave tests.
* `allure generate reports/allure_results -o reports/allure-report --clean`: This generates the Allure report and outputs it to `reports/allure-report`, cleaning any previous data.
* `allure open reports/allure-report`: This opens the generated Allure report in your default browser.

Allure Behave formatter

- behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
>>>>>>> 261c0a7 (example automation script in Selenium)
# Selenium_Automation_Testing
