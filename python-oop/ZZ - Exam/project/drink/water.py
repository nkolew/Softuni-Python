from typing import ClassVar

from project import Drink


class Water(Drink):
    _default_price: ClassVar[float] = 1.50
