from typing import ClassVar
from project import Product


class Drink(Product):
    QUANTITY: ClassVar[int] = 10

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__class__.QUANTITY)
