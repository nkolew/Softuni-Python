from abc import ABC, abstractmethod
from typing import ClassVar


class Vehicle(ABC):
    fuel_quantity: float
    fuel_consumption: float

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: float):
        current_fuel_quantity = self.fuel_quantity * \
            self.tank_capacity_factor
        current_fuel_consumption = self.fuel_consumption + \
            self.aircon_consumption

        if current_fuel_quantity < distance * current_fuel_consumption:
            return

        self.fuel_quantity -= distance * current_fuel_consumption

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * self.tank_capacity_factor

    @property
    @abstractmethod
    def aircon_consumption(self) -> float:
        ...

    @property
    @abstractmethod
    def tank_capacity_factor(self) -> float:
        ...


class Car(Vehicle):
    _AIRCON_CONSUMPTION: ClassVar[float] = 0.9
    _TANK_CAPACITY_FACTOR: ClassVar[float] = 1.0

    @property
    def aircon_consumption(self) -> float:
        return self.__class__._AIRCON_CONSUMPTION

    @property
    def tank_capacity_factor(self) -> float:
        return self.__class__._TANK_CAPACITY_FACTOR


class Truck(Vehicle):
    _AIRCON_CONSUMPTION: ClassVar[float] = 1.6
    _TANK_CAPACITY_FACTOR: ClassVar[float] = 0.95

    @property
    def aircon_consumption(self) -> float:
        return self.__class__._AIRCON_CONSUMPTION

    @property
    def tank_capacity_factor(self) -> float:
        return self.__class__._TANK_CAPACITY_FACTOR


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
