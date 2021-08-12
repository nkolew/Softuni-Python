from typing import ClassVar

from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    _default_health_increase: ClassVar[int] = 20
