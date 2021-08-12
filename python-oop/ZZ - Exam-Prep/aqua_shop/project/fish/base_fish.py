from abc import ABC, abstractmethod


class BaseFish(ABC):
    _name: str
    _species: str
    _price: float
    size: int

    def __init__(self, name: str, species: str, price: float) -> None:
        self.name = name
        self.species = species
        self.price = price
        self.size = self._default_size

    @property
    @abstractmethod
    def _default_size(self) -> int:
        ...

    @property
    @abstractmethod
    def habitat(self) -> str:
        ...

    def can_live_in(self, aquarium_type: str) -> bool:
        return aquarium_type == self.habitat

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Fish name cannot be an empty string.")
        self._name = value

    @property
    def species(self):
        """The species property."""
        return self._species

    @species.setter
    def species(self, value):
        if value == '':
            raise ValueError("Fish species cannot be an empty string.")
        self._species = value

    @property
    def price(self):
        """The price property."""
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self._price = value

    @abstractmethod
    def eat(self):
        self.size += 5
        ...
