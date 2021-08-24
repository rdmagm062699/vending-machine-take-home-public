from src.product import Product
from src.money import identify_coin

PRODUCTS = [
    {'name': 'COLA', 'price': 100},
    {'name': 'CHIPS', 'price': 50}, 
    {'name': 'CANDY', 'price': 65}
]

class Machine:
    def __init__(self):
        self.products = []
        for product in PRODUCTS:
            self.products.append(Product(product['name'], 10, product['price']))

        self.display = ''
        self.dispenser = ''
        self.coin_return_in_cents = 0
        self.amount_in_cents = 0

    def dispense(self, product_name):
        product = list(filter(lambda p: p.name == product_name.upper(), self.products))[0]
        
        if self._enough_money_entered(product.price_in_cents):
            self._try_to_dispense(product)
        else:
            self._display_not_enough_money(product)

    def add_coin(self, weight, diameter, thickness):
        coin = identify_coin(weight, diameter, thickness)

        if coin['valid'] == True:
            self.amount_in_cents += coin['value_in_cents']
        else:
            self.coin_return_in_cents += coin['value_in_cents']

    def _enough_money_entered(self, price):
        return price <= self.amount_in_cents

    def _try_to_dispense(self, product):
        if product.count > 0:
            product.dispense()
            self.amount_in_cents = 0
            self._display_successful_dispense(product)
        else:
            self._display_out_of_product(product)

    def _display_not_enough_money(self, product):
        display_price = format(product.price_in_cents / 100, '.2f')
        self.display = f'PRICE {display_price}'
        self.dispenser = ''

    def _display_successful_dispense(self, product):
        self.display = 'THANK YOU'
        self.dispenser = f'DISPENSING {product.name}...'

    def _display_out_of_product(self, product):
        self.dispenser = ''
        self.display = f'SORRY, WE ARE OUT OF {product.name}'
