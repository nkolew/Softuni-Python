from typing import ClassVar

from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    _default_comfort: ClassVar[int] = 5
    _default_price: ClassVar[float] = 10
