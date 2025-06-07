class Flower:
    """Class of flowers"""

    def __init__(self, name: str, num_petals: int, price: float):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    def set_num_petals(self, num_petals: int) -> None:
        self._num_petals = num_petals

    def get_num_petals(self) -> int:
        return self._num_petals

    def set_price(self, price: int) -> None:
        self._price = price

    def get_price(self) -> float:
        return self._price

    def __str__(self):
        return f"The name of flower is {self._name}. It has {self._num_petals} petals. Price is {self._price}"


flower_1 = Flower("rose", 10, 20)
print(flower_1)
