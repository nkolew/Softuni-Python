from typing import ClassVar

from project import Dessert


class Cake(Dessert):
    GRAMS: ClassVar[int] = 250
    CALORIES: ClassVar[int] = 1000
    PRICE: ClassVar[int] = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__class__.PRICE,
                         self.__class__.GRAMS, self.__class__.CALORIES)
