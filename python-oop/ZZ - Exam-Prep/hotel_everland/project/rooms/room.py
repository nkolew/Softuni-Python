from typing import ClassVar, List

from project.appliances.appliance import Appliance
from project.people.child import Child

NL = '\n'


class Room:
    family_name: str
    budget: float
    members_count: int
    children: List[Child]
    appliances: List[Appliance]

    _expenses: float
    _adults_count: int

    _default_room_cost: ClassVar[int] = 0
    _default_expenses: ClassVar[float] = 0
    _default_appliances: ClassVar[List[Appliance]] = []
    _default_children: ClassVar[List[Child]] = []

    def __init__(self, family_name: str, budget: float, members_count: int) -> None:
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.room_cost = self._default_room_cost
        self.expenses = self._default_expenses
        self.children = self._default_children
        self.appliances = self._default_appliances

    @property
    def expenses(self):
        """The expenses property."""
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args) -> None:
        self.expenses = sum(i.get_monthly_expense() for l in args for i in l)

    @property
    def monthly_total(self) -> float:
        return self.room_cost + self.expenses

    @property
    def has_enough_to_pay(self) -> bool:
        return self.budget >= self.monthly_total

    def get_prepay_report(self) -> str:
        if self.has_enough_to_pay:
            return f'{self.family_name} paid {self.monthly_total:.2f}$ and have {self.budget - self.monthly_total:.2f}$ left.'
        return f'{self.family_name} does not have enough budget and must leave the hotel.'

    def make_payment(self) -> None:
        self.budget -= self.monthly_total

    def __str__(self) -> str:
        msg = []
        msg.append(
            f'{self.family_name} with {self.members_count} members. Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$')
        for i, c in enumerate(self.children, 1):
            msg.append(
                f'--- Child {i} monthly cost: {c.get_monthly_expense():.2f}$'),
        if self.appliances:
            msg.append(
                f'--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in self.appliances):.2f}$')

        return NL.join(msg)
