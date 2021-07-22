from typing import ClassVar
from project import Supply


class FoodSupply(Supply):
    _NEEDS_INCREASE: ClassVar[int] = 20

    def __init__(self) -> None:
        super().__init__(self.__class__._NEEDS_INCREASE)
