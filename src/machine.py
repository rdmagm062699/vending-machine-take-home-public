from src.product import Product

PRODUCTS = ['COLA', 'CHIPS']

class Machine:
    def __init__(self):
        self.products = []
        for product in PRODUCTS:
            self.products.append(Product(product, 10))

        self.display = ''
        self.dispenser = ''

    def dispense(self, product_name):
        product = list(filter(lambda p: p.name == product_name.upper(), self.products))[0]
        
        if product.count > 0:
            product.dispense()
            self.display = 'THANK YOU'
            self.dispenser = f'DISPENSING {product.name}...'
        else:
            self.dispenser = ''
            self.display = f'SORRY, WE ARE OUT OF {product.name}'
