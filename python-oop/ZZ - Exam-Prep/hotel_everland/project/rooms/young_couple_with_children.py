from typing import ClassVar, List

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.rooms.room import Room
from project.people.child import Child


class YoungCoupleWithChildren(Room):
    _adults_count: ClassVar[int] = 2
    _default_room_cost: ClassVar[int] = 30
    _default_appliances: ClassVar[List[Appliance]] = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary1: float, salary2: float, *children: Child) -> None:
        members_count = self._adults_count+len(children)
        super().__init__(family_name, salary1+salary2, members_count)
        self.children = list(children)
        self.appliances = self._default_appliances * members_count
        self.calculate_expenses(self.children, self.appliances)


yc = YoungCoupleWithChildren('Test', 1000, 1000, Child(5), Child(5))
print(yc.room_cost)
