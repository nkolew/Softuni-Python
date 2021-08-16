from abc import ABC, abstractmethod


class Drink(ABC):
    _name: str
    price: float
    _portion: float
    _brand: str

    def __init__(self, name: str, portion: float, brand: str) -> None:
        self.name = name
        self.portion = portion
        self.price = self._default_price
        self.brand = brand

    def __repr__(self) -> str:
        return f' - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv'

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    @property
    @abstractmethod
    def _default_price(self) -> float:
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
    def brand(self):
        """The brand property."""
        return self._brand

    @brand.setter
    def brand(self, value):
        if value == '' or value == ' ':
            raise ValueError('Brand cannot be empty string or white space!')
        self._brand = value

    @property
    def portion(self):
        """The portion property."""
        return self._portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError('Portion cannot be less than or equal to zero!')
        self._portion = value
