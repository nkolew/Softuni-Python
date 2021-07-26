from abc import ABC, abstractmethod


class Card(ABC):
    _name: str
    _damage_points: int
    _health_points: int

    @abstractmethod
    def __init__(self, name: str, damage_points: int, health_points: int) -> None:
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Card's name cannot be an empty string.")
        self._name = value

    @property
    def damage_points(self):
        """The damage_points property."""
        return self._damage_points

    @damage_points.setter
    def damage_points(self, value):
        if value < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        self._damage_points = value

    @property
    def health_points(self):
        """The health_points property."""
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        if value < 0:
            raise ValueError("Card's HP cannot be less than zero.")
        self._health_points = value

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    
    def __str__(self) -> str:
        return f'### Card: {self.name} - Damage: {self.damage_points}'
