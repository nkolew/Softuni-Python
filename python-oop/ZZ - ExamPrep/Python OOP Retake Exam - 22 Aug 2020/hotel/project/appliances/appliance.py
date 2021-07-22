from abc import ABC
from typing import ClassVar


class Appliance(ABC):
    _DAYS_IN_MONTH: ClassVar[int] = 30

    cost: float

    def __init__(self, cost: float) -> None:
        self.cost = float(cost)

    def get_monthly_expense(self):
        return self.cost * self.__class__._DAYS_IN_MONTH
