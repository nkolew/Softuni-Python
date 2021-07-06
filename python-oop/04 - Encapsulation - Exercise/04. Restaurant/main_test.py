# zero test
from project.product import Product
from project.beverage.beverage import Beverage
from project.food.soup import Soup
import unittest

class Tests(unittest.TestCase):
    def test(self):
        product = Product("coffee", 2.5)
        self.assertEqual(product.__class__.__name__, "Product")
        self.assertEqual(product.name, "coffee")
        self.assertEqual(product.price, 2.5)
        beverage = Beverage("coffee", 2.5, 50)
        self.assertEqual(beverage.__class__.__name__, "Beverage")
        self.assertEqual(beverage.__class__.__bases__[0].__name__, "Product")
        self.assertEqual(beverage.name, "coffee")
        self.assertEqual(beverage.price, 2.5)
        self.assertEqual(beverage.milliliters, 50)
        soup = Soup("fish soup", 9.90, 230)
        self.assertEqual(soup.__class__.__name__, "Soup")
        self.assertEqual(soup.__class__.__bases__[0].__name__, "Starter")
        self.assertEqual(soup.name, "fish soup")
        self.assertEqual(soup.price, 9.90)
        self.assertEqual(soup.grams, 230)

if __name__ == "__main__":
    unittest.main()