Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

  Scenario: Stronger opponent
    Given the ninja has a third level black-belt
      When attacked by Chuck Norris
      Then the ninja should run for his life
      And fall off a cliff