from typing import ClassVar

from project import BakedFood


class Bread(BakedFood):
    _default_portion: ClassVar[float] = 200
