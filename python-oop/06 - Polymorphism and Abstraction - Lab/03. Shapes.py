import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...

    @abstractmethod
    def calculate_perimeter(self):
        ...


class Circle(Shape):
    radius: int

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    height: int
    width: int

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


# circle = Circle(5)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())
# rectangle = Rectangle(10, 20)
# print(rectangle.calculate_area())
# print(rectangle.calculate_perimeter())
