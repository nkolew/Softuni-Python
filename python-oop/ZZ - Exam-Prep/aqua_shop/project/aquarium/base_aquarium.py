from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    _name: str
    capacity:  int
    decorations: List[BaseDecoration]
    fish: List[BaseFish]

    def __init__(self, name: str) -> None:
        self.name = name
        self.capacity = self._initial_capacity
        self.decorations = []
        self.fish = []

    @property
    @abstractmethod
    def _initial_capacity(self) -> int:
        ...

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self._name = value

    def calculate_comfort(self) -> float:
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish: BaseFish) -> str:
        if not self.has_capacity:
            return "Not enough capacity."

        if not fish.can_live_in(self.__class__.__name__):
            return "Water not suitable."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    @property
    def has_capacity(self) -> bool:
        return self.capacity > len(self.fish)

    def str(self) -> str:
        return f'''{self.name}:
        Fish: {' '.join(f.name for f in self.fish) or "none"}
        Decorations: {len(self.decorations)}
        Comfort: {self.calculate_comfort()}'''
