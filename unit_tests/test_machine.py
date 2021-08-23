import unittest
from src.machine import Machine

class TestMachine(unittest.TestCase):

    def test_new_machine_has_10_colas(self):
        machine = Machine()

        cola = list(filter(lambda p: p.name == 'COLA', machine.products))[0]
        assert cola.count == 10

    def test_machine_will_dispense_cola(self):
        machine = Machine()

        machine.dispense('cola')
        cola = list(filter(lambda p: p.name == 'COLA', machine.products))[0]

        assert cola.count == 9

    def test_machine_display_set_on_successful_dispense(self):
        machine = Machine()

        machine.dispense('cola')

        assert machine.display == 'THANK YOU'

    def test_dispenser_is_set_on_successful_dispense(self):
        machine = Machine()

        machine.dispense('cola')

        assert machine.dispenser == 'DISPENSING COLA...'

    def test_will_display_out_of_product_message_and_not_dispense_if_out_of_cola(self):
        machine = Machine()
        
        for x in range(11):
            machine.dispense('cola')

        assert machine.dispenser == ''
        assert machine.display == 'SORRY, WE ARE OUT OF COLA'
        
    def test_new_machine_has_10_chips(self):
        machine = Machine()

        chips = list(filter(lambda p: p.name == 'CHIPS', machine.products))[0]
        assert chips.count == 10

    def test_new_machine_has_10_candy(self):
        machine = Machine()

        candy = list(filter(lambda p: p.name == 'CANDY', machine.products))[0]
        assert candy.count == 10

    def test_adding_a_penny_adds_one_cent_to_coin_return(self):
        machine = Machine()

        machine.add_coin(2.5, .75, 1.52)

        assert machine.coin_return_in_cents == 1

    def test_adding_a_nickel_adds_five_cents_to_amount(self):
        machine = Machine()

        machine.add_coin(5.0, .835, 1.95)

        assert machine.amount_in_cents == 5