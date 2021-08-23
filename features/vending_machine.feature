Feature: Vending Machine

    Scenario: The vending machine dispenses cola and says thank you
        Given The vending machine is running
        When The "cola" button is pushed
        Then "Cola" will be dispensed
        And The display will say "THANK YOU"
