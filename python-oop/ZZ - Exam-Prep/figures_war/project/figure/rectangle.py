from project import Figure


class Rectangle(Figure):
    def __init__(self, name: str, side_a: float, side_b: float) -> None:
        super().__init__(name, side_a, side_b)
        self.side_a = self.attributes[0]
        self.side_b = self.attributes[1]

    def calculate_area(self) -> float:
        return self.side_a * self.side_b

    def calculate_circumference(self) -> float:
        return 2 * (self.side_a + self.side_b)
