from typing import ClassVar, List

from project import TV, Appliance, Room, Fridge, Stove


class OldCouple(Room):
    _ROOM_COST: ClassVar[float] = 15.0
    _MEMBERS_COUNT: ClassVar[int] = 2
    _APPLIANCES: ClassVar[List[Appliance]] = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension1: float, pension2: float) -> None:
        budget = pension1 + pension2
        super().__init__(family_name, budget, self.__class__._MEMBERS_COUNT)

        self.appliances = self.__class__._APPLIANCES * \
            self.__class__._MEMBERS_COUNT

        self.calculate_expenses(self.appliances)
