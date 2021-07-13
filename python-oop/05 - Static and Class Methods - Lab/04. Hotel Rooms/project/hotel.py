from typing import List

from project import Room


class Hotel:
    name: str
    rooms: List[Room]
    guests: int

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = []
        self.guests = 0

    def update_guests(self) -> None:
        self.guests = sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int) -> 'Hotel':
        name = f'{stars_count} stars Hotel'
        return cls(name)

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for r in self.rooms:
            if r.number != room_number or r.capacity < people:
                continue
            r.take_room(people)
            self.update_guests()
            return

    def free_room(self, room_number: int) -> None:
        for r in self.rooms:
            if r.number != room_number:
                continue
            r.free_room()
            self.update_guests()
            return

    def status(self) -> str:
        return f'''Hotel {self.name} has {self.guests} total guests
Free rooms: {", ".join(map(str, [r.number for r in self.rooms if not r.is_taken]))}
Taken rooms: {", ".join(map(str, [r.number for r in self.rooms if r.is_taken]))}'''
