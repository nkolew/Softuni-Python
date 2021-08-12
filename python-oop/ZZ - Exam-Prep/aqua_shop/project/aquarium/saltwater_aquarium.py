from typing import ClassVar

from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    _initial_capacity: ClassVar[int] = 25
