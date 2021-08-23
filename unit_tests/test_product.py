import unittest
from src.product import Product

class TestMachine(unittest.TestCase):

    def test_dispense_reduces_count_by_one(self):
        product = Product('COLA', 2)

        product.dispense()
        assert product.count == 1

    def test_product_count_will_never_go_below_0(self):
        product = Product('COLA', 0)
        
        product.dispense()
        assert product.count == 0
