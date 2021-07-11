from typing import Dict

from project import Dough, Topping


class Pizza:
    __name: str
    __dough: Dough
    __toppings_capacity: int
    __toppings: Dict[str, float]

    def __init__(self, name: str, dough: Dough, toppings_capacity: int) -> None:
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("The name cannot be an empty string")

        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if not value:
            raise ValueError("You should add dough to the pizza")

        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError(
                "The topping's capacity cannot be less or equal to zero")

        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.__toppings:
            self.__toppings[topping.topping_type] = 0

        self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(w for _, w in self.toppings.items())
