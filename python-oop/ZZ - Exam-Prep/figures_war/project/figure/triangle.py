from project import Figure


class Triangle(Figure):
    def __init__(self, name: str, side_a: float, height_a: float, side_b: float, side_c: float) -> None:
        super().__init__(name, side_a, height_a, side_b, side_c)
        self.side_a = self.attributes[0]
        self.height_a = self.attributes[1]
        self.side_b = self.attributes[2]
        self.side_c = self.attributes[3]

    def calculate_area(self) -> float:
        return (self.side_a * self.height_a) / 2

    def calculate_circumference(self) -> float:
        return self.side_a + self.side_b + self.side_c
