from typing import ClassVar

from project.rooms.room import Room


class AloneOld(Room):
    _adults_count: ClassVar[int] = 1
    _default_room_cost: ClassVar[int] = 10

    def __init__(self, family_name: str, pension: float) -> None:
        super().__init__(family_name, pension, self._adults_count)
