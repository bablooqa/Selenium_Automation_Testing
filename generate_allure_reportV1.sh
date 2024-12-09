#!/bin/bash

# Make the Script Executable:
# chmod +x generate_allure_report.sh
# Step 0: Check if a browser argument is provided, otherwise default to "chrome"
if [ -z "$BROWSER" ]; then
    BROWSER=$1  # Use the argument passed to the script if available
    export BROWSER
fi

echo "Browser argument: $BROWSER"  # Debugging line to ensure browser value is passed

if [ -z "$BROWSER" ]; then
    BROWSER="chrome"  # Default to "chrome" if no argument is given
    echo "No browser argument provided. Defaulting to Chrome."
fi

# Ensure the reports/allure-results directory exists and is clean
mkdir -p reports/allure-results
rm -rf reports/allure-results/*

# Step 1: Set up environment properties
echo -e "Browser=$BROWSER\nBrowser.Version=131.0\nPlatform=macOS\nPlatform.Version=Monterey 12.7\nEnvironment=Staging" > reports/allure-results/environment.properties

# Step 2: Set up categories
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

# Step 3: Set up executor information
cat <<EOL > reports/allure-results/executor.json
{
  "name": "Local Machine",
  "type": "local",
  "url": "http://127.0.0.1",
  "buildOrder": "1",
  "reportName": "Local Test Report"
}
EOL

# Step 4: Copy history folder if it exists
if [ -d "reports/allure-report/history" ]; then
  cp -r reports/allure-report/history reports/allure-results/
fi

# Step 5: Run Behave with Allure Formatter and pass the browser argument
echo "Running Behave tests with browser: $BROWSER"
behave -D browser=$BROWSER -f allure_behave.formatter:AllureFormatter -o reports/allure-results

# Step 6: Generate Allure report
if [ "$(ls -A reports/allure-results)" ]; then
  if command -v allure &> /dev/null; then
    allure generate reports/allure-results -o reports/allure-report --clean
    if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
      allure open reports/allure-report
    else
      echo "Allure report generated. To open it, use: allure open reports/allure-report"
    fi
  else
    echo "Error: 'allure' command not found. Please install Allure before running the script."
    exit 1
  fi
else
  echo "No test result files found in reports/allure-results. Please check your Behave tests and formatter configuration."
fi
