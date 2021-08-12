from typing import ClassVar, List

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    _adults_count: ClassVar[int] = 1
    _default_room_cost: ClassVar[int] = 10
    _default_appliances: ClassVar[List[Appliance]] = [TV()]

    def __init__(self, family_name: str, salary: float) -> None:
        super().__init__(family_name, salary, self._adults_count)
        self.appliances = self._default_appliances * self._adults_count
        self.calculate_expenses(self.appliances)
