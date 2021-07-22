from typing import ClassVar

from project import Room


class AloneOld(Room):
    _ROOM_COST: ClassVar[float] = 10.0
    _MEMBERS_COUNT: ClassVar[int] = 1

    def __init__(self, family_name: str, pension: float) -> None:
        budget = pension
        
        super().__init__(family_name, budget, self.__class__._MEMBERS_COUNT)
        
        self.calculate_expenses()
