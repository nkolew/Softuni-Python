from abc import ABC, abstractmethod
from typing import Tuple, Type
from project import Food


class Animal(ABC):
    name: str
    weight: float
    food_eaten: int

    def __init__(self, name: str, weight: float, food_eaten: int = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def make_sound(self) -> str:
        return self._SOUND

    @property
    @abstractmethod
    def _VALID_FOOD_TYPES(self) -> Tuple[Type[Food]]:
        ...

    @property
    @abstractmethod
    def _WEIGHT_INCREASE_FACTOR(self) -> float:
        ...

    @property
    @abstractmethod
    def _SOUND(self) -> str:
        ...

    def feed(self, food: Food):
        if not isinstance(food, Food) or not isinstance(food, self._VALID_FOOD_TYPES):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * self._WEIGHT_INCREASE_FACTOR

    @abstractmethod
    def __repr__(self) -> str:
        ...


class Bird(Animal):
    wing_size: float

    def __init__(self, name: str, weight: float,  wing_size: float, food_eaten: int = 0) -> None:
        super().__init__(name, weight, food_eaten=food_eaten)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    living_region: str

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0) -> None:
        super().__init__(name, weight, food_eaten=food_eaten)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
