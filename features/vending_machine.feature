Feature: Vending Machine

    Scenario: The vending machine dispenses cola and says thank you
        Given The vending machine is running
        When The "cola" button is pushed 1 time(s)
        Then "Cola" will be dispensed
        And The display will say "THANK YOU"

    Scenario: The vending machine will run out of cola
        Given The vending machine is running
        When The "cola" button is pushed 11 time(s)
        Then nothing will be dispensed
        And The display will say "SORRY, WE ARE OUT OF COLA"

    Scenario: The vending machine dispenses chips and says thank you
        Given The vending machine is running
        When The "chips" button is pushed 1 time(s)
        Then "Chips" will be dispensed
        And The display will say "THANK YOU"

    Scenario: The vending machine will run out of chips
        Given The vending machine is running
        When The "chips" button is pushed 11 time(s)
        Then nothing will be dispensed
        And The display will say "SORRY, WE ARE OUT OF CHIPS"