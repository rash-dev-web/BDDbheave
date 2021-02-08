Feature: Test all the get requests from reqres

  Scenario: Get the List of users
    Given the request url and parameter
    When submit the list user request
    Then get the response as number of users and status code as 200
