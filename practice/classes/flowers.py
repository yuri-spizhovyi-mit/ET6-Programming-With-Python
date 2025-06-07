class Flower:
    """Class of flowers"""
    def __init__(self, name: str, num_petals: int, price: float):
        self.name = name
        self.num_petals = num_petals
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_num_petals(self, num_petals):
        self.num_petals = num_petals

    def get_num_petals(self):
        return self.num_petals

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"The name of flower is {self.name}. It has {self.num_petals} petals. Price is {self.price}"


flower_1 = Flower('rose', 10, 20)
print(flower_1)
