import unittest
from src.money import identify_coin

class TestMoney(unittest.TestCase):

    def test_identifies_a_penny(self):
        coin = identify_coin(2.5, .75, 1.52)

        assert coin['value_in_cents'] == 1

    def test_identifies_a_nickel(self):
        coin = identify_coin(5.0, .835, 1.95)

        assert coin['value_in_cents'] == 5

    def test_identifies_a_dime(self):
        coin = identify_coin(2.268, .705, 1.35)

        assert coin['value_in_cents'] == 10

    def test_identifies_a_dime(self):
        coin = identify_coin(5.670, .955, 1.75)

        assert coin['value_in_cents'] == 25
