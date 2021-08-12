from typing import ClassVar, List

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.rooms.room import Room


class OldCouple(Room):
    _adults_count: ClassVar[int] = 2
    _default_room_cost: ClassVar[int] = 15
    _default_appliances: ClassVar[List[Appliance]] = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension1: float, pension2: float) -> None:
        super().__init__(family_name, pension1+pension2, self._adults_count)
        self.appliances = self._default_appliances * self._adults_count
        self.calculate_expenses(self.appliances)
