from project import Figure


class Square(Figure):
    def __init__(self, name: str, side: float) -> None:
        super().__init__(name, side)
        self.side = self.attributes[0]

    def calculate_area(self) -> float:
        return self.side ** 2

    def calculate_circumference(self) -> float:
        return 4 * self.side
