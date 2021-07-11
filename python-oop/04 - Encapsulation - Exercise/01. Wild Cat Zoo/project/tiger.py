from typing import ClassVar

from project import Animal


class Tiger(Animal):
    _MONEY_FOR_CARE: ClassVar[int] = 45

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, self.__class__._MONEY_FOR_CARE)
