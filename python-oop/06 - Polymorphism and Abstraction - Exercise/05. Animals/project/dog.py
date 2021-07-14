from typing import ClassVar
from project import Animal


class Dog(Animal):
    _SOUND: ClassVar[str] = 'Woof!'
