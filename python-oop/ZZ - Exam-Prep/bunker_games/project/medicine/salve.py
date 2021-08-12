from typing import ClassVar

from project.medicine.medicine import Medicine


class Salve(Medicine):
    _default_health_increase: ClassVar[int] = 50
