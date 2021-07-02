# zero test
from project.hero import Hero
from project.elf import Elf
import unittest

class Tests(unittest.TestCase):
   def test(self):
      hero = Hero("H", 4)
      self.assertEqual(hero.username, "H")
      self.assertEqual(hero.level, 4)
      self.assertEqual(str(hero), "H of type Hero has level 4")
      elf = Elf("E", 4)
      self.assertEqual(str(elf), "E of type Elf has level 4")
      self.assertEqual(elf.__class__.__bases__[0].__name__, "Hero")
      self.assertEqual(elf.username, "E")
      self.assertEqual(elf.level, 4)

if __name__ == "__main__":
   unittest.main()