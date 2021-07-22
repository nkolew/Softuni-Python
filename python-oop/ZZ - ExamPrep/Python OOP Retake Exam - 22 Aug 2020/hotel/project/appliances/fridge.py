from typing import ClassVar

from project import Appliance


class Fridge(Appliance):
    _COST: ClassVar[float] = 1.2

    def __init__(self) -> None:
        super().__init__(self.__class__._COST)
