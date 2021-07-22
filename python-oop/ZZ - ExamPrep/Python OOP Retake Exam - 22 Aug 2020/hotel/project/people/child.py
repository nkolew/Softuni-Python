class Child:
    cost: float

    def __init__(self, food_cost: int, *toy_cost) -> None:
        self.cost = float(food_cost + sum(toy_cost))
