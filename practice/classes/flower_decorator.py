class Flower:
    def __init__(self, name: str, num_petals: int, price: float):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def num_petals(self) -> int:
        return self._num_petals

    @num_petals.setter
    def num_petals(self, num_petals: int) -> None:
        self._num_petals = num_petals

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price

    def __str__(self):
        return f"The name of flower is {self.name}. It has {self.num_petals} petals. Price is {self.price}"


flower_1 = Flower("rose", 10, 20)
print(flower_1)
flower_1.price = 25.0
