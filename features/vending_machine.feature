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

    Scenario: The vending machine will send penny straight to the coin return
        Given The vending machine is running
        When A "penny" is inserted
        Then the amount entered will show "INSERT COIN"
        And the coin return will have .01

    Scenario: The vending machine will accept a nickel
        Given The vending machine is running
        When A "nickel" is inserted
        Then the amount entered will show "0.05"

    Scenario: The vending machine will accept a dime
        Given The vending machine is running
        When A "dime" is inserted
        Then the amount entered will show "0.10"

    Scenario: The vending machine will accept a quarter
        Given The vending machine is running
        When A "quarter" is inserted
        Then the amount entered will show "0.25"
