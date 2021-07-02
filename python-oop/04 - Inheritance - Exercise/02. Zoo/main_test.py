# zero test
from project.animal import Animal
from project.mammal import Mammal
from project.lizard import Lizard
import unittest


class Tests(unittest.TestCase):
    def test(self):
        mammal = Mammal("Stella")
        self.assertEqual(mammal.__class__.__bases__[0].__name__, "Animal")
        self.assertEqual(mammal.name, "Stella")
        lizard = Lizard("John")
        self.assertEqual(lizard.__class__.__bases__[0].__name__, "Reptile")
        self.assertEqual(lizard .name, "John")


if __name__ == "__main__":
    unittest.main()
