class Product:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def dispense(self):
        self.count -= 1
