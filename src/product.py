class Product:
    def __init__(self, name, count, price_in_cents=0):
        self.name = name
        self.count = count
        self.price_in_cents = price_in_cents

    def dispense(self):
        if self.count > 0:
            self.count -= 1
