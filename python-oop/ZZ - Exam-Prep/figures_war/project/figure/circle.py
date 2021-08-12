from math import pi

from project import Figure


class Circle(Figure):
    def __init__(self, name: str, radius: float) -> None:
        super().__init__(name, radius)
        self.radius = self.attributes[0]

    def calculate_area(self) -> float:
        return pi * self.radius ** 2

    def calculate_circumference(self) -> float:
        return 2 * pi * self.radius
