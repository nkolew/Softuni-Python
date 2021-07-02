from typing import ClassVar

from project import Animal


class Cheetah(Animal):
    _NEEDS: ClassVar[int] = 60
