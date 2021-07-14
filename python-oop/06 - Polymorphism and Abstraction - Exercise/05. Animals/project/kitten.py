from typing import ClassVar
from project import Cat


class Kitten(Cat):
    _GENDER: ClassVar[str] = 'Female'
    _SOUND: ClassVar[str] = 'Meow'

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, self.__class__._GENDER)
