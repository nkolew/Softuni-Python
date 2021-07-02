from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    horse_power: int

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers: int):
        fuel_requred = kilometers * self.fuel_consumption
        if self.fuel >= fuel_requred:
            self.fuel -= fuel_requred
