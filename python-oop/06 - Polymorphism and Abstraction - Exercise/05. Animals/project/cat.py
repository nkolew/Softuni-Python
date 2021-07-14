from typing import ClassVar
from project import Animal


class Cat(Animal):
    _SOUND: ClassVar[str] = 'Meow meow!'
