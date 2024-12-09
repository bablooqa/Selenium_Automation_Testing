#!/bin/bash

# Make the Script Executable:
# chmod +x generate_allure_report.sh



# Step 1: Ensure the reports/allure-results directory exists and is clean
mkdir -p reports/allure-results
rm -rf reports/allure-results/*

# Step 2: Set up environment properties
echo -e "Browser=Chrome\nBrowser.Version=117.0\nPlatform=macOS\nPlatform.Version=Ventura 13.5\nEnvironment=Staging" > reports/allure-results/environment.properties

# Step 3: Set up categories
cat <<EOL > reports/allure-results/categories.json
[
  {
    "name": "Known Issue",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*NullPointerException.*"
  },
  {
    "name": "Infrastructure Problem",
    "matchedStatuses": ["broken"],
    "traceRegex": ".*Database connection.*"
  }
]
EOL

# Step 4: Set up executor information
cat <<EOL > reports/allure-results/executor.json
{
  "name": "Local Machine",
  "type": "local",
  "url": "http://127.0.0.1",
  "buildOrder": "1",
  "reportName": "Local Test Report"
}
EOL

# Step 5: Copy history folder if it exists
if [ -d "reports/allure-report/history" ]; then
  cp -r reports/allure-report/history reports/allure-results/
fi

# Step 6: Run Behave with Allure Formatter
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results

# Step 7: Generate Allure report
if [ "$(ls -A reports/allure-results)" ]; then
  allure generate reports/allure-results -o reports/allure-report --clean
  allure open reports/allure-report
else
  echo "No test result files found in reports/allure-results. Please check your Behave tests and formatter configuration."
fi
