from src.product import Product
from src.money import identify_coin

PRODUCTS = ['COLA', 'CHIPS', 'CANDY']

class Machine:
    def __init__(self):
        self.products = []
        for product in PRODUCTS:
            self.products.append(Product(product, 10))

        self.display = ''
        self.dispenser = ''
        self.coin_return_in_cents = 0

    def dispense(self, product_name):
        product = list(filter(lambda p: p.name == product_name.upper(), self.products))[0]
        
        if product.count > 0:
            product.dispense()
            self.display = 'THANK YOU'
            self.dispenser = f'DISPENSING {product.name}...'
        else:
            self.dispenser = ''
            self.display = f'SORRY, WE ARE OUT OF {product.name}'

    def add_coin(self, weight, diameter, thickness):
        coin = identify_coin(weight, diameter, thickness)

        self.coin_return_in_cents += coin['value_in_cents']
