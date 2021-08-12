from typing import ClassVar

from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    _default_size: ClassVar[int] = 3
    habitat: ClassVar[str] = 'FreshwaterAquarium'

    def eat(self):
        self.size += 3
