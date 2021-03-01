class Circle:
    __pi = 3.14

    def __init__(self, dia) -> None:
        self.dia = dia
        self.rad = self.dia / 2

    def calculate_circumference(self,):
        return 2 * Circle.__pi * self.rad

    def calculate_area(self,):
        return Circle.__pi * self.rad ** 2

    def calculate_area_of_sector(self, angle: int):
        return self.calculate_area() * angle / 360


circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

