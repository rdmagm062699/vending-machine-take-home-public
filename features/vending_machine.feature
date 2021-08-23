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

    Scenario: The vending machine dispenses candy and says thank you
        Given The vending machine is running
        When The "candy" button is pushed 1 time(s)
        Then "Candy" will be dispensed
        And The display will say "THANK YOU"

    Scenario: The vending machine will run out of candy
        Given The vending machine is running
        When The "candy" button is pushed 11 time(s)
        Then nothing will be dispensed
        And The display will say "SORRY, WE ARE OUT OF CANDY"

    Scenario: The vending machine will prompt to insert coins if none are entered
        Given The vending machine is running
        Then the amount entered will show "INSERT COIN"