from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


# class Factory(ABC):
#     @abstractmethod
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#         self.ingredients = {}

#     @abstractmethod
#     def add_ingredient(self, type, quantity):
#         """Add products to the factory"""
#         pass

#     @abstractmethod
#     def remove_ingredient(self, type, quantity):
#         """Remove products from the factory"""
#         pass

#     def can_add(self, value):
#         return self.capacity - sum(self.ingredients.values()) - value >= 0

#     def __repr__(self):
#         result = ""
#         result += f"Factory name: {self.name} with capacity {self.capacity}.\n"
#         for ingredient in self.ingredients:
#             result += f"{ingredient}: {self.ingredients[ingredient]}\n"
#         return result


# class PaintFactory(Factory):
#     def __init__(self, name, capacity):
#         super().__init__(name, capacity)

#     def add_ingredient(self, product_type, product_quantity):
#         if product_type in ["white", "yellow", "blue", "green", "red"]:
#             if self.can_add(product_quantity):
#                 if product_type not in self.ingredients:
#                     self.ingredients[product_type] = 0
#                 self.ingredients[product_type] += product_quantity
#             else:
#                 raise ValueError("Not enough space in factory")
#         else:
#             raise TypeError(
#                 f"Ingredient of type {product_type} not allowed in {self.__class__.__name__}")

#     def remove_ingredient(self, product_type, product_quantity):
#         if product_type in self.ingredients:
#             if self.ingredients[product_type] - product_quantity >= 0:
#                 self.ingredients[product_type] -= product_quantity
#             else:
#                 raise ValueError(
#                     "Ingredients quantity cannot be less than zero")
#         else:
#             raise KeyError("No such ingredient in the factory")

#     @property
#     def products(self):
#         return self.ingredients


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
