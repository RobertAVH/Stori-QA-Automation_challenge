@stori_challenge
Feature: Stori_Challenge

  @Test_component_01
  Scenario: Go to challenge page
    Given I access to web site

  @Test_component_02
  Scenario: ipt_suggestion_class example
    Given I access to web site
    And I type Me in suggestion class input
    And I select Mexico option
    And I type Uni in suggestion class input
    And I select United States (USA) option
    And I type Uni in suggestion class input
    And I select United Arab Emirates option
    And I type Ire in suggestion class input
    And I select Ireland option

  @Test_component_03
  Scenario: Dropdown Example
    Given I access to web site
    When I scroll to element dropdown_example
    And I select than dropdown_example the option 2
    And I wait to be able to see the change
    And I select than dropdown_example the option 3
    Then I wait to be able to see the change

  @Test_component_04
  Scenario: Switch window Example
    Given I access to web site
    When I do click in button_new_window
    And I switch the new window
    And I validate text SELF PACED ONLINE TRAINING in the page
    And I report the bugs in excel report
    And I validate text IN DEPTH MATERIAL in the page
    And I report the bugs in excel report
    And I validate text LIFETIME INSTRUCTOR SUPPORT in the page
    And I report the bugs in excel report
    And I validate text RESUME PREPARATION in the page
    Then I report the bugs in excel report

  @Test_component_06
  Scenario: Switch Tab Example
    Given I access to web site
    When I scroll to element button_new_window
    And I do click in button_new_window
    And I switch the new tab
    Then I scroll page finding button_view_all_courses and take screenshot

  @Test_component_07
    Scenario: Switch Alert Example
      Given I access to web site
      When I scroll to element input_alerts
      And I type Story Card in input_alerts input
      And I do click in button_alert
      And I switch the new alert
      And I type Story Card in input_alerts input
      And I do click in button_alert_confirm
      Then I switch the new alert

  @Test_component_08
    Scenario: Switch Table Example
      Given I access to web site
      When I scroll to element table_example
      And I get all the courses that cost $25 and print its
      And I get all the courses that cost $15 and print its

  @Test_component_09
    Scenario: Switch Table Fixed Example
      Given I access to web site
      When I scroll to element table_fixed
      And I get all the Engineer from fixed table
      And I get all the Businessman from fixed table

  @Test_component_10
    Scenario: Switch iFrame Example
      Given I access to web site
      When I scroll to element iframe
      And I switch the new iframe
      And I scroll to element iframe_option
      And I get text and print the content the iframe_option element