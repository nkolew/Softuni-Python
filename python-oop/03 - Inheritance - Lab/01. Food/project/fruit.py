from project.food import Food


class Fruit(Food):

    name: str

    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name
