from typing import ClassVar

from project import Animal


class Lion(Animal):
    _MONEY_FOR_CARE: ClassVar[int] = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.__class__._MONEY_FOR_CARE)

