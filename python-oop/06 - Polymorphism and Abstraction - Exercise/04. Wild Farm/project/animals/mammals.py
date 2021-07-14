from project import Mammal, Fruit, Meat, Vegetable


class Mouse(Mammal):
    _VALID_FOOD_TYPES = (Vegetable, Fruit)
    _WEIGHT_INCREASE_FACTOR = 0.10
    _SOUND = 'Squeak'


class Dog(Mammal):
    _VALID_FOOD_TYPES = (Meat,)
    _WEIGHT_INCREASE_FACTOR = 0.40
    _SOUND = 'Woof!'


class Cat(Mammal):
    _VALID_FOOD_TYPES = (Meat, Vegetable)
    _WEIGHT_INCREASE_FACTOR = 0.30
    _SOUND = 'Meow'


class Tiger(Mammal):
    _VALID_FOOD_TYPES = (Meat,)
    _WEIGHT_INCREASE_FACTOR = 1.00
    _SOUND = 'ROAR!!!'
