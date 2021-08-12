from typing import ClassVar

from project.fish.base_fish import BaseFish


class SaltwaterFish (BaseFish):
    _default_size: ClassVar[int] = 5
    habitat: ClassVar[str] = 'SaltwaterAquarium'

    def eat(self):
        self.size += 2
