from typing import ClassVar, List

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.rooms.room import Room


class YoungCouple(Room):
    _adults_count: ClassVar[int] = 2
    _default_room_cost: ClassVar[int] = 20
    _default_appliances: ClassVar[List[Appliance]] = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary1: float, salary2: float) -> None:
        super().__init__(family_name, salary1+salary2, self._adults_count)
        self.appliances = self._default_appliances * self._adults_count
        self.calculate_expenses(self.appliances)
