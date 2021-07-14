from project import Food, Meat, Bird


class Owl(Bird):
    _VALID_FOOD_TYPES = (Meat,)
    _WEIGHT_INCREASE_FACTOR = 0.25
    _SOUND = 'Hoot Hoot'


class Hen(Bird):
    _VALID_FOOD_TYPES = (Food,)
    _WEIGHT_INCREASE_FACTOR = 0.35
    _SOUND = 'Cluck'
