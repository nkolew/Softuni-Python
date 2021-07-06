from project import Food


class Dessert(Food):
    __calories: float

    def __init__(self, name: str, price: float, grams: float, calories: float) -> None:
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        """The calories property."""
        return self.__calories
