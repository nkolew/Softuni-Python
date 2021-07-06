from project import Food


class Dessert(Food):
    __calories: float

    def __init__(self, name, price, grams: float, calories: float) -> None:
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        """The calories property."""
        return self.__calories

    @calories.setter
    def calories(self, value):
        self.__calories = value
