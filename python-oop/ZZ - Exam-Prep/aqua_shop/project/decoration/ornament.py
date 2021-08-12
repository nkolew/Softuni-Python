from typing import ClassVar

from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    _default_comfort: ClassVar[float] = 1
    _default_price: ClassVar[float] = 5
