from abc import ABC


class Food(ABC):
    quantity: int

    def __init__(self, quantity: int) -> None:
        self.quantity = quantity


class Vegetable(Food):
    pass


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass
