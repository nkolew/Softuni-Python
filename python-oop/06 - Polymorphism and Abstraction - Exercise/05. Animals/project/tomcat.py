from typing import ClassVar
from project import Cat


class Tomcat(Cat):
    _GENDER: ClassVar[str] = 'Male'
    _SOUND: ClassVar[str] = 'Hiss'

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, self.__class__._GENDER)