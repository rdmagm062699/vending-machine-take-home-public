import unittest
from parameterized import parameterized
from src.machine import Machine

class TestMachine(unittest.TestCase):

    @parameterized.expand(['COLA', 'CHIPS', 'CANDY'])
    def test_new_machine_has_10_of_each_product(self, product):
        machine = Machine()

        cola = list(filter(lambda p: p.name == product, machine.products))[0]
        assert cola.count == 10
    
    @parameterized.expand([
        ['COLA', 100], 
        ['CHIPS', 50], 
        ['CANDY', 65]
    ])
    def test_machine_will_successfully_dispense_product_if_price_met(self, name, price_in_cents):
        machine = Machine()
        machine.amount_in_cents = price_in_cents

        machine.dispense(name)
        product = list(filter(lambda p: p.name == name, machine.products))[0]
        assert product.count == 9
        assert machine.display == 'THANK YOU'
        assert machine.dispenser == f'DISPENSING {name}...'

    @parameterized.expand([
        ['COLA', '1.00'], 
        ['CHIPS', '0.50'], 
        ['CANDY', '0.65']
    ])
    def test_machine_will_not_dispense_product_if_price_is_not_met(self, name, price):
        machine = Machine()

        machine.dispense(name)
        product = list(filter(lambda p: p.name == name, machine.products))[0]
        assert product.count == 10
        assert machine.dispenser == ''
        assert machine.display == f'PRICE {price}'

    def test_will_display_out_of_product_message_and_not_dispense_if_out_of_cola(self):
        machine = Machine()
        
        for x in range(11):
            machine.amount_in_cents = 100
            machine.dispense('cola')

        assert machine.dispenser == ''
        assert machine.display == 'SORRY, WE ARE OUT OF COLA'

    def test_adding_a_penny_adds_one_cent_to_coin_return(self):
        machine = Machine()

        machine.add_coin(2.5, .75, 1.52)

        assert machine.coin_return_in_cents == 1

    def test_adding_a_nickel_adds_five_cents_to_amount(self):
        machine = Machine()

        machine.add_coin(5.0, .835, 1.95)

        assert machine.amount_in_cents == 5