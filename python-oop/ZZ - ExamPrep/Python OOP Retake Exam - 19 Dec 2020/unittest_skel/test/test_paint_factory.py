from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory(name='FactoryName', capacity=10)

    def test_new_factory_can_be_instantiated(self):
        p_factory = PaintFactory(name='FactoryName', capacity=10)
        products = {}
        message = 'Factory name: FactoryName with capacity 10.\n'
        self.assertEqual('FactoryName', p_factory.name)
        self.assertEqual(10, p_factory.capacity)
        self.assertEqual(products, p_factory.products)
        self.assertEqual(message, repr(p_factory))

    def test_factory_cannot_add_wrong_ingredient(self):
        i_type = 'brown'
        i_quantity = 5
        products = {}
        message = "Ingredient of type brown not allowed in PaintFactory"
        with self.assertRaises(TypeError) as e:
            self.paint_factory.add_ingredient(
                i_type, i_quantity)
            self.assertEqual(message, str(e))
            self.assertEqual(self.paint_factory.products, products)

    def test_factory_cannot_add_valid_ingredient_over_capacity(self):
        i_type = 'white'
        i_quantity = 20
        message = "Not enough space in factory"
        with self.assertRaises(ValueError) as e:
            self.paint_factory.add_ingredient(
                i_type, i_quantity)
            self.assertEqual(message, str(e))

    def test_factory_adds_valid_ingredient_with_valid_quantity(self):
        i_type = 'white'
        i_quantity = 5
        products = {i_type: i_quantity}
        message = f'Factory name: FactoryName with capacity 10.\nwhite: 5\n'
        self.paint_factory.add_ingredient(
            i_type, i_quantity)

        self.assertEqual(products, self.paint_factory.products)
        self.assertEqual(message, repr(self.paint_factory))

    def test_factory_adds_аnother_valid_ingredient_with_valid_quantity(self):
        i_type1 = 'white'
        i_type2 = 'yellow'

        quantity = 5
        products = {i_type1: quantity, i_type2: quantity}

        self.paint_factory.add_ingredient(
            i_type1, quantity)

        self.paint_factory.add_ingredient(
            i_type2, quantity)

        self.assertEqual(products, self.paint_factory.products)

    def test_factory_cannot_add_аnother_valid_ingredient_after_capacity_is_over(self):
        i_type1 = 'white'
        i_type2 = 'yellow'
        i_type3 = 'blue'

        quantity = 5
        products = {i_type1: quantity, i_type2: quantity}
        message = "Not enough space in factory"

        self.paint_factory.add_ingredient(
            i_type1, quantity)

        self.paint_factory.add_ingredient(
            i_type2, quantity)

        self.assertEqual(False, self.paint_factory.can_add(quantity))

        with self.assertRaises(ValueError) as e:
            self.paint_factory.add_ingredient(i_type3, quantity)
            self.assertEqual(message, str(e))

        self.assertEqual(products, self.paint_factory.products)

    def test_factory_cannot_remove_invalid_ingredient(self):
        i_type1 = 'white'
        i_type2 = 'yellow'
        quantity = 5
        message = "No such ingredient in the factory"

        self.paint_factory.add_ingredient(i_type1, quantity)

        self.paint_factory.add_ingredient(i_type2, quantity)

        with self.assertRaises(KeyError) as e:
            self.paint_factory.remove_ingredient('red', 5)
            self.assertEqual(message, str(e))

    def test_factory_cannot_remove_more_than_ingredient_quantity(self):
        i_type1 = 'white'
        i_type2 = 'yellow'
        quantity = 5
        message = "Ingredient quantity cannot be less than zero"

        self.paint_factory.add_ingredient(i_type1, quantity)

        self.paint_factory.add_ingredient(i_type2, quantity)

        with self.assertRaises(ValueError) as e:
            self.paint_factory.remove_ingredient('white', 10)
            self.assertEqual(message, str(e))

    def test_factory_removes_valid_ingredient_with_valid_quantity(self):
        i_type1 = 'white'
        i_type2 = 'yellow'
        quantity = 5
        products = {i_type1: 1, i_type2: quantity}

        self.paint_factory.add_ingredient(i_type1, quantity)

        self.paint_factory.add_ingredient(i_type2, quantity)

        self.paint_factory.remove_ingredient('white', 4)

        self.assertEqual(products, self.paint_factory.products)


if __name__ == "__main__":
    main()
