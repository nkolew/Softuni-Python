from typing import ClassVar

from project import Medicine


class Painkiller(Medicine):
    _HEALTH_INCREASE: ClassVar[int] = 20

    def __init__(self) -> None:
        super().__init__(self.__class__._HEALTH_INCREASE)
