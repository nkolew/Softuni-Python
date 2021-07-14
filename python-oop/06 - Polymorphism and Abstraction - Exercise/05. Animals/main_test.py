import unittest

from project.animal import Animal
from project.cat import Cat
from project.dog import Dog
from project.kitten import Kitten
from project.tomcat import Tomcat


class Tests(unittest.TestCase):
    def test_cat_init(self):
        c = Cat("Meowy", 10, "Male")
        self.assertEqual(c.name, "Meowy")
        self.assertEqual(c.age, 10)
        self.assertEqual(c.gender, "Male")
        self.assertTrue(issubclass(c.__class__, Animal))

    def test_cat_repr(self):
        c = Cat("Meowy", 10, "Male")
        exp = "This is Meowy. Meowy is a 10 year old Male Cat"
        self.assertEqual(exp, repr(c))

    def test_cat_sound(self):
        c = Cat("Meowy", 20, "Male")
        exp = "Meow meow!"
        self.assertEqual(exp, c.make_sound())

    def test_dog_init(self):
        d = Dog("Wolfy", 15, "Male")
        self.assertEqual(d.name, "Wolfy")
        self.assertEqual(d.age, 15)
        self.assertEqual(d.gender, "Male")
        self.assertTrue(issubclass(d.__class__, Animal))

    def test_dog_repr(self):
        d = Dog("Wolfy", 15, "Female")
        exp = "This is Wolfy. Wolfy is a 15 year old Female Dog"
        self.assertEqual(exp, repr(d))

    def test_dog_sound(self):
        d = Dog("Wolfy", 15, "Male")
        exp = "Woof!"
        self.assertEqual(exp, d.make_sound())

    def test_kitten_init(self):
        k = Kitten("Meowy", 1)
        self.assertEqual(k.name, "Meowy")
        self.assertEqual(k.age, 1)
        self.assertEqual(k.gender, "Female")
        self.assertTrue(issubclass(k.__class__, Animal))
        self.assertTrue(issubclass(k.__class__, Cat))

    def test_kitten_repr(self):
        k = Kitten("Meowy", 1)
        exp = "This is Meowy. Meowy is a 1 year old Female Kitten"
        self.assertEqual(exp, repr(k))

    def test_kitten_sound(self):
        k = Kitten("Meowy", 1)
        exp = "Meow"
        self.assertEqual(exp, k.make_sound())

    def test_tomcat_init(self):
        t = Tomcat("Meowy", 15)
        self.assertEqual(t.name, "Meowy")
        self.assertEqual(t.age, 15)
        self.assertEqual(t.gender, "Male")
        self.assertTrue(issubclass(t.__class__, Animal))
        self.assertTrue(issubclass(t.__class__, Cat))

    def test_tomcat_repr(self):
        t = Tomcat("Meowy", 20)
        exp = "This is Meowy. Meowy is a 20 year old Male Tomcat"
        self.assertEqual(exp, repr(t))

    def test_tomcat_sound(self):
        k = Tomcat("Meowy", 20)
        exp = "Hiss"
        self.assertEqual(exp, k.make_sound())


if __name__ == "__main__":
    unittest.main()
