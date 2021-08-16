from typing import ClassVar

from project import Drink


class Tea(Drink):
    _default_price: ClassVar[float] = 2.50
