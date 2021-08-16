from typing import ClassVar

from project import BakedFood


class Cake(BakedFood):
    _default_portion: ClassVar[float] = 245
