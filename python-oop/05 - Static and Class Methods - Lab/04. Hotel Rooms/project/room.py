from typing import Union


class Room:
    number: int
    capacity: int
    guests: int
    is_taken: bool

    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> Union[None, str]:
        if self.is_taken or self.capacity < people:
            return f'Room number {self.number} cannot be taken'

        self.is_taken, self.guests = True, people

    def free_room(self) -> Union[None, str]:
        if not self.is_taken:
            return f'Room number {self.number} is not taken'

        self.is_taken, self.guests = False, 0
