from typing import ClassVar

from project.supply.supply import Supply


class WaterSupply(Supply):
    _default_needs_increase: ClassVar[int] = 40
