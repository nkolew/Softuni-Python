from typing import List
import unittest

from project import *


class FoodTests(unittest.TestCase):
    def test_food_can_be_initiated(self):
        food: List[Food] = [Vegetable(5),
                            Fruit(5),
                            Meat(5),
                            Seed(5),
                            ]
        actual_value = [f.quantity for f in food]
        expected_value = [5, 5, 5, 5]
        self.assertEqual(expected_value, actual_value)


class AnimalTests(unittest.TestCase):
    def test_birds_can_be_initiated(self):
        birds: List[Bird] = [
            Owl("Pip", 10, 10),
            Hen("Harry", 10, 10)
        ]
        expected_value = 'Owl [Pip, 10, 10, 0]\nHen [Harry, 10, 10, 0]'
        actual_value = '\n'.join(str(b) for b in birds)
        self.assertEqual(expected_value, actual_value)

    def test_mammals_can_be_initiated(self):
        mammals: List[Mammal] = [
            Mouse("Jerry", 10, 'Cartoon World'),
            Cat("Tom", 10, 'Cartoon World'),
            Dog('Spike', 10, 'Cartoon World'),
            Tiger('Shir-Khan', 10, 'Cartoon World')
        ]
        expected_value = '''Mouse [Jerry, 10, Cartoon World, 0]
Cat [Tom, 10, Cartoon World, 0]
Dog [Spike, 10, Cartoon World, 0]
Tiger [Shir-Khan, 10, Cartoon World, 0]'''
        actual_value = '\n'.join(str(m) for m in mammals)
        self.assertEqual(expected_value, actual_value)

    def hen_is_fed_succesfuly_when_food_is_from_correct_type(self):
        m = Meat(4)
        v = Vegetable(4)
        f = Fruit(4)
        s = Seed(4)
        expected_value = 'Hen [Harry, 10, 15.600000000000001, 16]'
        hen = Hen('Harry', 10, 10)
        for i in [m, v, f, s]:
            hen.feed(i)
        self.assertEqual(expected_value, str(hen))


if __name__ == "__main__":
    unittest.main()


# first zero test
# import unittest
# from project.animals.birds import Owl, Hen
# from project.animals.mammals import Mouse, Dog, Cat, Tiger
# from project.food import Vegetable, Fruit, Meat, Seed

# class WildFarmTests(unittest.TestCase):
#     def test_first_zero(self):
#         owl = Owl("Pip", 10, 10)
#         self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
#         meat = Meat(4)
#         self.assertEqual(owl.make_sound(), "Hoot Hoot")
#         owl.feed(meat)
#         veg = Vegetable(1)
#         owl.feed(veg)
#         self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
#         self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")

# if __name__ == "__main__":
#     unittest.main()