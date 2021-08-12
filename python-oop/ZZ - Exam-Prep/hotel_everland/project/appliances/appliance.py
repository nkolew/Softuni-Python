from typing import ClassVar


class Appliance:
    cost: float
    _days_in_month: ClassVar[int] = 30

    def __init__(self, cost: float) -> None:
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * self._days_in_month
