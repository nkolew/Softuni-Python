from typing import ClassVar, List

from project import TV, Appliance, Room


class AloneYoung(Room):
    _ROOM_COST: ClassVar[float] = 10.0
    _MEMBERS_COUNT: ClassVar[int] = 1
    _APPLIANCES: ClassVar[List[Appliance]] = [TV()]

    def __init__(self, family_name: str, budget: float) -> None:
        super().__init__(family_name, budget, self.__class__._MEMBERS_COUNT)
        
        self.appliances = self.__class__._APPLIANCES
        
        self.calculate_expenses(self.appliances)
