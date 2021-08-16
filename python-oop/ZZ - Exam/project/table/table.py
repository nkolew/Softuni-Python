from abc import ABC, abstractmethod
from itertools import chain
from typing import List, Optional

from project import BakedFood, Drink


class Table(ABC):
    _table_number: int
    _capacity: int
    food_orders: List[BakedFood]
    drink_orders: List[Drink]
    number_of_people: int
    is_reserved: bool

    def __init__(self, table_number: int, capacity: int) -> None:
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.table_number == o.table_number

    @property
    @abstractmethod
    def _valid_numbers_range(self) -> range:
        ...

    @property
    @abstractmethod
    def _invalid_number_message(self) -> str:
        ...

    def _validate_range(self, table_number: int) -> None:
        if table_number not in self._valid_numbers_range:
            raise ValueError(self._invalid_number_message)
        return None

    @property
    def table_number(self):
        """The table_number property."""
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        self._validate_range(value)
        self._table_number = value

    @property
    def capacity(self):
        """The capacity property."""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError('Capacity has to be greater than 0!')
        self._capacity = value

    def reserve(self, number_of_people: int) -> None:
        self.number_of_people, self.is_reserved = number_of_people, True

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        return sum(o.price for o in chain(self.food_orders, self.drink_orders))

    def clear(self) -> None:
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        # self.is_reserve = False  # ?Check

    def free_table_info(self) -> Optional[str]:
        if self.is_reserved:
            return None

        return f'''Table: {self.table_number}
Type: {self.__class__.__name__}
Capacity: {self.capacity}'''
