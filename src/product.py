class Product:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def dispense(self):
        if self.count > 0:
            self.count -= 1
