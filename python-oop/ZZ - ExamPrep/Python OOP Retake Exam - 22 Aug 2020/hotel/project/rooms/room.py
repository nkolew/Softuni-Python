from typing import ClassVar, List, Union

from project import Appliance, Child


class Room:
    family_name: str
    budget: float
    members_count: int
    children: List[Child]

    _ROOM_COST: ClassVar[float] = 0
    _DEFAULT_EXPENSES: ClassVar[float] = 0
    _APPLIANCES: ClassVar[List[Appliance]] = []

    __expenses: float

    def __init__(self,
                 family_name: str,
                 budget: float,
                 members_count: int) -> None:
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []

    @property
    def expenses(self):
        """The expenses property."""
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')

        self.__expenses = value

    def calculate_expenses(self, *args:
                           List[Union[Child, Appliance]]):
        if not args:
            self.expenses = self.__class__._DEFAULT_EXPENSES
        self.expenses = sum(e.cost for l in args for e in l)
