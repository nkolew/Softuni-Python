from typing import ClassVar

from project import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS: ClassVar[int] = 50
    PRICE: ClassVar[float] = 3.50

    __caffeine: float

    def __init__(self, name: str, caffeine: float) -> None:
        super().__init__(name, self.__class__.PRICE, self.__class__.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        """The caffeine property."""
        return self.__caffeine
