from typing import ClassVar

from project import Animal


class Cheetah(Animal):
    _MONEY_FOR_CARE: ClassVar[int] = 60

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.__class__._MONEY_FOR_CARE)
