from typing import ClassVar

from project import Appliance


class Stove(Appliance):
    _COST: ClassVar[float] = 0.7

    def __init__(self) -> None:
        super().__init__(self.__class__._COST)
