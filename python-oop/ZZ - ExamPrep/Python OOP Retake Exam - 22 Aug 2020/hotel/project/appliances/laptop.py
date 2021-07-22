from typing import ClassVar

from project import Appliance


class Laptop(Appliance):
    _COST: ClassVar[float] = 1.0

    def __init__(self) -> None:
        super().__init__(self.__class__._COST)
