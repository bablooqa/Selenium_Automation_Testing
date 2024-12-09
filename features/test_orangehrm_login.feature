# Feature: OrangeHRM Login Functionality
#   As a user of OrangeHRM
#   I want to be able to log in with correct and incorrect credentials
#   So that I can access or be denied access appropriately

#   Scenario: Test Login with Correct Credentials
#     Given the user has valid login credentials
#     When the user enters the correct username and password
#     Then the user should be successfully logged in
#     And the correct profile page should be displayed
#     And the user should be able to log out successfully

#   Scenario: Test Login with Incorrect Credentials
#     Given the user has invalid login credentials
#     When the user enters the incorrect username and password
#     Then the user should see an error message
#     And the user should not be logged in


# Feature: OrangeHRM Login Functionality
#   As a user of OrangeHRM
#   I want to be able to log in with correct and incorrect credentials
#   So that I can access or be denied access appropriately

#   Scenario Outline: Test Login with Various Credentials
#     Given the user has "<credentials_type>" login credentials
#     When the user enters the username "<username>" and password "<password>"
#     Then the user should be "<login_status>"
#     And "<expected_result>" should be displayed

#   Examples:
#     | credentials_type   | username | password     | login_status             | expected_result                   |
#     | valid              | admin    | admin123     | successfully logged in   | correct profile page              |
#     | invalid            | Admin5   | admin12345   | not be logged in         | error message                     |


# Feature: OrangeHRM Login Functionality
#   As a user of OrangeHRM
#   I want to be able to log in with correct and incorrect credentials
#   So that I can access or be denied access appropriately

#   Scenario Outline: Test Login with Various Credentials
#     Given the user has "<credentials_type>" login credentials
#     When the user enters the username "<username>" and password "<password>"
#     Then the user should be "<login_status>"
#     And "<expected_result>" should be displayed

#   Examples:
#     | credentials_type | username | password     | login_status             | expected_result                   |
#     | valid            | admin    | admin123     | successfully logged in   | correct profile page              |
#     | invalid          | Admin1   | admin12345   | not be logged in         | error message                     |


Feature: OrangeHRM Login Functionality
  As a user of OrangeHRM
  I want to be able to log in with correct and incorrect credentials
  So that I can access or be denied access appropriately

  Scenario Outline: Test Login with Various Credentials on Different Browsers
    Given the user has "<credentials_type>" login credentials on "<browser>"
    When the user enters the username "<username>" and password "<password>"
    Then the user should be "<login_status>"
    And "<expected_result>" should be displayed

  # Examples:
  #   | credentials_type | username | password     | login_status             | expected_result                   | browser   |
  #   | valid            | admin    | admin123     | successfully logged in   | correct profile page              | chrome    |
  #   | invalid          | Admin1   | admin12345   | not be logged in         | error message                     | firefox   |
  #   | valid            | admin    | admin123     | successfully logged in   | correct profile page              | edge      |
  #   | invalid          | Admin1   | admin12345   | not be logged in         | error message                     | chrome    |


  Examples:
    | credentials_type | username | password     | login_status             | expected_result                   |
    | valid            | admin    | admin123     | successfully logged in   | correct profile page              |
    | invalid          | Admin1   | admin12345   | not be logged in         | error message                     |
