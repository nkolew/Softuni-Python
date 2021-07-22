from typing import ClassVar, List

from project import TV, Appliance, Room, Fridge, Laptop


class YoungCouple(Room):
    _ROOM_COST: ClassVar[float] = 20.0
    _MEMBERS_COUNT: ClassVar[int] = 2
    _APPLIANCES: ClassVar[List[Appliance]] = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary1: float, salary2: float) -> None:
        budget = salary1 + salary2
        super().__init__(family_name, budget, self.__class__._MEMBERS_COUNT)
        
        self.appliances = self.__class__._APPLIANCES*self.__class__._MEMBERS_COUNT
        
        self.calculate_expenses(self.appliances)