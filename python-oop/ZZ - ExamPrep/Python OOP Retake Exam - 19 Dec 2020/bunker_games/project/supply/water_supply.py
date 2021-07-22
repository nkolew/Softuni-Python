from typing import ClassVar

from project import Supply


class WaterSupply(Supply):
    _NEEDS_INCREASE: ClassVar[int] = 40

    def __init__(self) -> None:
        super().__init__(self.__class__._NEEDS_INCREASE)
