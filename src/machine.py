from src.product import Product

class Machine:
    def __init__(self):
        self.products = []
        self.products.append(Product('COLA', 10))

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

    def refill(self):
        cola = list(filter(lambda p: p.name == 'COLA', self.products))[0]
        cola.count = 10
