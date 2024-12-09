#!/bin/bash

# Step 1: Ensure the reports/allure-results directory exists and is clean
mkdir -p reports/allure-results
rm -rf reports/allure-results/*

# Step 2: Check if the history folder exists in the previous report
if [ -d "reports/allure-report/history" ]; then
  # Copy the history folder to allure-results
  cp -r reports/allure-report/history reports/allure-results/
fi

# Step 3: Run Behave with Allure Formatter
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results

# Step 4: Check if the allure-results folder has content
if [ "$(ls -A reports/allure-results)" ]; then
  # Step 5: Generate Allure report
  allure generate reports/allure-results -o reports/allure-report --clean
  allure open reports/allure-report
else
  echo "No test result files found in reports/allure-results. Please check your Behave tests and formatter configuration."
fi
