import unittest
from src.money import identify_coin

class TestMoney(unittest.TestCase):

    def test_identifies_a_penny(self):
        coin = identify_coin(2.5, .75, 1.52)

        assert coin['value_in_cents'] == 1

    def test_identifies_a_nickel(self):
        coin = identify_coin(5.0, .835, 1.95)

        assert coin['value_in_cents'] == 5
