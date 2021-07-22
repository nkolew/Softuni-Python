import unittest

from project.people.child import Child
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Johnsons", 150, 205)

    def test_room_initializes_correctly(self):
        expected_family_name = 'Test'
        expected_budget = 100.0
        expected_members_count = 5
        r = Room("Test", 100, 5)
        self.assertEqual(expected_family_name, r.family_name)
        self.assertEqual(expected_budget, r.budget)
        self.assertEqual(expected_members_count, r.members_count)

    def test_room_expenses_is_properly_set(self):
        expected_value = 20.0
        self.room.expenses = 20.0
        self.assertEqual(expected_value, self.room.expenses)

    def test_room_expenses_raises_ValueError_when_negative(self):
        expected_message = 'Expenses cannot be negative'
        with self.assertRaises(ValueError) as e:
            self.room.expenses = -20.0
            self.assertEqual(expected_message, str(e))

    def test_room_calculates_expenses_correctly(self):
        expected_value = 42.7
        children = [Child(5, 5, 5, 5), Child(5, 5, 5, 5)]
        appliances = [TV(), Fridge()]
        self.room.calculate_expenses(children, appliances)
        self.assertEqual(expected_value, self.room.expenses)
