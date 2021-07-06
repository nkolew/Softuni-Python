class Product:
    __name: str
    __price: float

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price

    @property
    def name(self):
        """The name property."""
        return self.__name

    @property
    def price(self):
        """The price property."""
        return self.__price
