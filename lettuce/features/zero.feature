Feature: Compute factorial
  In order to play  with Lettuce
  As beginners
  We'll implement factorial

  Scenario:Factorial of 1
    Given I have the number 1
    When I compute its factorial
    Then I see the number 1