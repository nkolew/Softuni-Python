from abc import ABC, abstractmethod


class BakedFood(ABC):
    _name: str
    _price: float
    portion: float

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.portion = self._default_portion
        self.price = price

    def __repr__(self) -> str:
        return f' - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv'

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    @property
    @abstractmethod
    def _default_portion(self) -> float:
        ...

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '' or value == ' ':
            raise ValueError('Name cannot be empty string or white space!')
        self._name = value

    @property
    def price(self):
        """The price property."""
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Price cannot be less than or equal to zero!')
        self._price = value
