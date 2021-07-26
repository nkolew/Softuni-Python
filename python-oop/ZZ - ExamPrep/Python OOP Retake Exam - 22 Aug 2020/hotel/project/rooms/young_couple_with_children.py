from typing import ClassVar, List

from project import TV, Appliance, Child, Fridge, Laptop, Room


class YoungCoupleWithChildren(Room):
    _ROOM_COST: ClassVar[float] = 30.0
    _ADULTS_COUNT: ClassVar[int] = 2
    _APPLIANCES: ClassVar[List[Appliance]] = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary1: float, salary2: float, *children: Child) -> None:
        budget = salary1 + salary2
        members_count = self.__class__._ADULTS_COUNT + len(children)

        super().__init__(family_name, budget, members_count)

        self.children = list(children)
        self.appliances = self.__class__._APPLIANCES*members_count

        self.room_cost = self.__class__._ROOM_COST

        self.calculate_expenses(self.appliances, self.children)
