import unittest

from project.pet_shop import PetShop


class PetShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ps = PetShop('test')

    def test_pet_shop_has_correct_attributes_after_init(self):
        self.assertEqual(
            (True, True, True),
            (
                hasattr(self.ps, 'name'),
                hasattr(self.ps, 'food'),
                hasattr(self.ps, 'pets'),
            ),
        )
        self.assertEqual(
            ('test', {}, []),
            (self.ps.name, self.ps.food, self.ps.pets),
        )

    def test_pet_shop_add_food_raises_with_negative_qty(self):
        msg = 'Quantity cannot be equal to or less than 0'
        with self.assertRaises(ValueError) as ctx:
            self.ps.add_food('test_food', -1)
        self.assertEqual(
            (msg, 0),
            (str(ctx.exception), len(self.ps.food))
        )

    def test_pet_shop_add_food_new_food(self):
        self.assertEqual(0, len(self.ps.food))
        self.assertNotIn('new_food', self.ps.food)
        self.ps.add_food('new_food', 5)
        self.assertEqual(1, len(self.ps.food))
        self.assertIn('new_food', self.ps.food)
        self.assertEqual(5, self.ps.food['new_food'])
        self.assertEqual(1, len(self.ps.food))
        self.assertNotIn('another_food', self.ps.food)
        self.ps.add_food('another_food', 10)
        self.assertEqual(2, len(self.ps.food))
        self.assertIn('another_food', self.ps.food)
        self.assertEqual(5, self.ps.food['new_food'])
        self.assertEqual(10, self.ps.food['another_food'])

    def test_pet_shop_adds_qty_if_food_exist(self):
        self.assertEqual(0, len(self.ps.food))
        self.ps.add_food('new_food', 5)
        self.assertEqual(1, len(self.ps.food))
        self.assertIn('new_food', self.ps.food)
        self.ps.add_food('new_food', 15)
        self.assertEqual(1, len(self.ps.food))
        self.assertEqual(20, self.ps.food['new_food'])

    def test_pet_shop_add_food_returns_correct_message(self):
        msg = 'Successfully added 10.00 grams of test_food.'
        rv = self.ps.add_food('test_food', 10)
        self.assertEqual(msg, rv)

    def test_pet_shop_add_pet_can_add_pet_if_it_is_not_already_present(self):
        self.assertEqual(0, len(self.ps.pets))
        msg = 'Successfully added new_pet.'
        rv = self.ps.add_pet('new_pet')
        self.assertEqual(msg, rv)
        self.assertEqual(1, len(self.ps.pets))
        self.assertIn('new_pet', self.ps.pets)
        msg2 = 'Successfully added another_pet.'
        rv2 = self.ps.add_pet('another_pet')
        self.assertEqual(msg2, rv2)
        self.assertEqual(2, len(self.ps.pets))
        self.assertIn('another_pet', self.ps.pets)

    def test_pet_shop_add_pet_raises_if_name_of_pet_already_present(self):
        self.assertEqual(0, len(self.ps.pets))
        self.ps.add_pet('new_pet')
        self.assertEqual(1, len(self.ps.pets))
        self.assertIn('new_pet', self.ps.pets)
        msg = 'Cannot add a pet with the same name'
        with self.assertRaises(Exception) as ctx:
            self.ps.add_pet('new_pet')
        self.assertEqual(msg, str(ctx.exception))

    def test_petshop_can_feed_pet_if_such_pet_and_enough_food_exists(self):
        msg = 'test_pet was successfully fed'
        self.ps.add_pet('test_pet')
        self.ps.add_food('test_food', 150)
        rv = self.ps.feed_pet('test_food', 'test_pet')
        self.assertEqual(msg, rv)
        self.assertEqual(50, self.ps.food['test_food'])

    def test_petshop_feed_pet_raises_if_no_such_pet_exist(self):
        msg = 'Please insert a valid pet name'
        self.ps.add_pet('test_pet')
        self.ps.add_food('test_food', 150)
        with self.assertRaises(Exception) as ctx:
            self.ps.feed_pet('test_food', 'pet')
        self.assertEqual(msg, str(ctx.exception))
        self.assertEqual(150, self.ps.food['test_food'])

    def test_petshop_feed_pet_returns_correct_msg_if_no_such_food_exist(self):
        msg = 'You do not have food'
        self.ps.add_pet('test_pet')
        self.ps.add_food('test_food', 150)
        rv = self.ps.feed_pet('food', 'test_pet')
        self.assertEqual(msg, rv)
        self.assertEqual(150, self.ps.food['test_food'])

    def test_petshop_feed_pet_returns_correct_msg_if_food_is_not_enough(self):
        msg = 'Adding food...'
        self.ps.add_pet('test_pet')
        self.ps.add_food('test_food', 50)
        rv = self.ps.feed_pet('test_food', 'test_pet')
        self.assertEqual(msg, rv)
        self.assertEqual(1050.00, self.ps.food['test_food'])

    def test_pet_shop_has_correct_representation(self):
        msg = '''Shop test_shop:
Pets: test1, test2'''
        p = PetShop('test_shop')
        p.add_pet('test1')
        p.add_pet('test2')
        self.assertEqual(msg, repr(p))


if __name__ == "__main__":
    unittest.main()
