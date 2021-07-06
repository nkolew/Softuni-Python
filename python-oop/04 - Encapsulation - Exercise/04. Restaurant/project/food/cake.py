from typing import ClassVar

from project import Dessert


class Cake(Dessert):
    GRAMS: ClassVar[int] = 250
    CALORIES: ClassVar[int] = 1000
    PRICE: ClassVar[int] = 5
