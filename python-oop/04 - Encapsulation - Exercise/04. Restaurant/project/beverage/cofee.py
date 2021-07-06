from typing import ClassVar

from project import Beverage


class Coffee(Beverage):
    MILLILITERS: ClassVar[int] = 50
    PRICE: ClassVar[float] = 3.50

    __caffeine: float

    @property
    def caffeine(self):
        """The caffeine property."""
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value
