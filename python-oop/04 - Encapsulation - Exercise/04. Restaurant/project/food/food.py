from project import Product


class Food(Product):
    __grams: float

    def __init__(self, name, price, grams: float) -> None:
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        """The grams property."""
        return self.__grams

    @grams.setter
    def grams(self, value):
        self.__grams = value
