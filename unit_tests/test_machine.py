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
