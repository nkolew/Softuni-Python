import unittest

from project.mammal import Mammal

ANIMAL_NAME = 'Test'
ANIMAL_TYPE = 'dog'
ANIMAL_SOUND = 'bark'
KINGDOM = 'animals'


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal(ANIMAL_NAME, ANIMAL_TYPE, ANIMAL_SOUND)

    def test_animal_init(self):
        self.assertEqual(ANIMAL_NAME, self.mammal.name)
        self.assertEqual(ANIMAL_TYPE, self.mammal.type)
        self.assertEqual(ANIMAL_SOUND, self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_animal_can_make_sound(self):
        expected = 'Test makes bark'
        self.assertEqual(expected, self.mammal.make_sound())

    def test_animal_can_report_info(self):
        expected = 'Test is of type dog'
        self.assertEqual(expected, self.mammal.info())

    def test_animal_can_report_kingdom(self):

        self.assertEqual(KINGDOM, self.mammal.get_kingdom())


if __name__ == "__main__":
    unittest.main()
