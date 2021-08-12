from typing import ClassVar


class Child:
    cost: float
    _days_in_month: ClassVar[int] = 30

    def __init__(self, food_cost: float, *toys_cost: float) -> None:
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * self._days_in_month
