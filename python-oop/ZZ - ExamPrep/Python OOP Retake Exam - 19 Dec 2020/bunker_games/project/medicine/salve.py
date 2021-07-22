from typing import ClassVar

from project import Medicine


class Salve(Medicine):
    _HEALTH_INCREASE: ClassVar[int] = 50

    def __init__(self) -> None:
        super().__init__(self.__class__._HEALTH_INCREASE)
