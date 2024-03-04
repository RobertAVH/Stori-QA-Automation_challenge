Feature: Stori_Challenge

  Scenario: Go to challenge page
    Given I access to web site

  Scenario: Suggestion class example
    Given I access to web site
    When I type Me in suggestion class input
    Then I select Mexico option
    And I type Uni in suggestion class input
    Then I select United States (USA) option
    And I type Uni in suggestion class input
    Then I select United Arab Emirates option
    And I type Ire in suggestion class input
    Then I select Ireland option

  Scenario: Dropdown Example
    Given I access to web site
    When I select than dropdown_example the option 2
    Then I wait to be able to see the change
    When I select than dropdown_example the option 3
    Then I wait to be able to see the change

  Scenario: Switch window Example
    Given I access to web site
    When I do click in button_new_window
    Then I switch the new window
    And I validate text SELF PACED ONLINE TRAINING in the page
    And I report the bugs in excel report
    And I validate text IN DEPTH MATERIAL in the page
    And I report the bugs in excel report
    And I validate text LIFETIME INSTRUCTOR SUPPORT in the page
    And I report the bugs in excel report
    And I validate text RESUME PREPARATION in the page
    And I report the bugs in excel report

