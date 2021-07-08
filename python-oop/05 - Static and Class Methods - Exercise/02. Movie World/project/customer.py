from typing import List

from project import DVD


class Customer:
    name: str
    age: int
    id: int
    rented_dvds: List[DVD]

    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({", ".join(d.name for d in self.rented_dvds)})'
