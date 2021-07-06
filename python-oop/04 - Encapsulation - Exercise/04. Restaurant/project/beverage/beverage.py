from project import Product


class Beverage(Product):
    __milliliters: float

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        """The milliliters property."""
        return self.__milliliters
