Feature: To test the post requests

#  Scenario: To test create user request
#    Given request url and post body
#    When send the url and json body
#    Then Receive the Json response and status code as 201

  Scenario Outline: To test create user request
    Given request url and post body
    When send the url and json body with "<name>" and "<job>"
    Then Then Receive the Json response and status code as 201
    Examples:
      | name | job |
      | Mir |  QA |
      |  Ayaan    |   Dev  |
