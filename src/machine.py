from src.product import Product

class Machine:
    def __init__(self):
        self.products = []
        self.products.append(Product('COLA', 10))

        self.display = ''

    def dispense(self, product_name):
        product = list(filter(lambda p: p.name == product_name.upper(), self.products))[0]
        
        product.dispense()
        self.display = 'THANK YOU'
