import unittest
from src.machine import Machine

class TestMachine(unittest.TestCase):

    def test_new_machine_has_10_colas(self):
        machine = Machine()

        cola = list(filter(lambda p: p.name == 'COLA', machine.products))[0]
        assert cola.count == 10
