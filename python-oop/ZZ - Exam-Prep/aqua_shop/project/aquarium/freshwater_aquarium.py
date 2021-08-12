from typing import ClassVar

from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    _initial_capacity: ClassVar[int] = 50
