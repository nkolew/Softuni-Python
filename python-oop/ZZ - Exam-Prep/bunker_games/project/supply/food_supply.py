from typing import ClassVar

from project.supply.supply import Supply


class FoodSupply(Supply):
    _default_needs_increase: ClassVar[int] = 20
