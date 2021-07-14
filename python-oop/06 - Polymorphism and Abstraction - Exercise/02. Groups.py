import unittest
from typing import List


class Person:
    name: str
    surname: str

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'

    def __add__(self, o: 'Person') -> 'Person':
        if not isinstance(o, self.__class__):
            raise TypeError(
                f'Expected {self.__class__.__name__}, got {o.__class__.__name__}')

        return self.__class__(self.name, o.surname)


class Group:
    name: str
    people: List[Person]

    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __str__(self) -> str:
        return f'Group {self.name} with members {", ".join(map(str, self.people))}'

    def __len__(self) -> int:
        return len(self.people)

    def __getitem__(self, key: int) -> str:
        return f'Person {key}: {str(self.people[key])}'

    def __add__(self, o: 'Group') -> 'Group':
        if not isinstance(o, self.__class__):
            raise TypeError(
                f'Expected {self.__class__.__name__}, got {o.__class__.__name__}')

        return self.__class__(f'{self.name} {o.name}', self.people + o.people)


class PersonTests(unittest.TestCase):
    def test_person_is_properly_initiated(self):
        name, surname = ('Aliko', 'Dangote')
        p1 = Person(name, surname)
        self.assertEqual(p1.name, name)
        self.assertEqual(p1.surname, surname)

    def test_person_is_correctly_converted_to_str(self):
        name, surname = ('Aliko', 'Dangote')
        p1 = Person(name, surname)
        expected_value = 'Aliko Dangote'
        actual_value = str(p1)
        self.assertEqual(expected_value, actual_value)

    def test_two_persons_can_be_added_resulting_new_person_with_complex_name(self):
        name1, surname1 = ('Warren', 'Buffet')
        name2, surname2 = ('Elon', 'Musk')
        p1 = Person(name1, surname1)
        p2 = Person(name2, surname2)
        p3 = p1 + p2
        self.assertEqual(p3.name, name1)
        self.assertEqual(p3.surname, surname2)

    def test_person_cannot_be_added_with_something_else(self):
        name1, surname1 = ('Warren', 'Buffet')
        name2, surname2 = ('Elon', 'Musk')
        p1 = Person(name1, surname1)
        p2 = 0
        with self.assertRaises(TypeError) as exc:
            p3 = p1 + p2
        expected_message = f'Expected Person, got {p2.__class__.__name__}'
        self.assertEqual(expected_message, str(exc.exception))


class GroupTests(unittest.TestCase):

    def setUp(self) -> None:
        self.p0 = Person('Aliko', 'Dangote')
        self.p1 = Person('Bill', 'Gates')
        self.p2 = Person('Warren', 'Buffet')
        self.p3 = Person('Elon', 'Musk')
        self.p4 = self.p2 + self.p3

    def test_group_is_properly_initiated(self):
        first_group_name = '__VIP__'
        first_group_people = [self.p0, self.p1, self.p2]
        first_group = Group(first_group_name, first_group_people)
        self.assertEqual(first_group_name, first_group.name)
        self.assertEqual(first_group_people, first_group.people)

    def test_group_returns_correct_length(self):
        first_group_name = '__VIP__'
        first_group_people = [self.p0, self.p1, self.p2]
        first_group = Group(first_group_name, first_group_people)
        expected_value = len(first_group_people)
        actual_value = len(first_group)
        self.assertEqual(expected_value, actual_value)

    def test_two_groups_can_be_added(self):
        first_group_people = [self.p0, self.p1, self.p2]
        second_group_people = [self.p3, self.p4]
        all_people = first_group_people + second_group_people
        first_group = Group('__VIP__', first_group_people)
        second_group = Group('Special', second_group_people)
        third_group = first_group + second_group
        self.assertEqual(all_people, third_group.people)

    def test_group_cannot_be_added_with_something_else(self):
        first_group_people = [self.p0, self.p1, self.p2]
        first_group = Group('__VIP__', first_group_people)
        second_group = [1, 2, 3]
        with self.assertRaises(TypeError) as exc:
            third_group = first_group + second_group
        expected_message = f'Expected Group, got {second_group.__class__.__name__}'
        self.assertEqual(expected_message, str(exc.exception))

    def test_group_is_correctly_converted_to_str(self):
        second_group_people = [self.p3, self.p4]
        second_group = Group('Special', second_group_people)
        expected_value = 'Group Special with members Elon Musk, Warren Musk'
        actual_value = str(second_group)
        self.assertEqual(expected_value, actual_value)

    def test_group_can_be_indexed(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        second_group = Group('Special', [self.p3, self.p4])
        third_group = first_group + second_group
        actual_value = str(third_group[0])
        expected_value = 'Person 0: Aliko Dangote'
        self.assertEqual(expected_value, actual_value)

    def test_group_can_be_iterated(self):
        first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
        second_group = Group('Special', [self.p3, self.p4])
        third_group = first_group + second_group
        expected_value = '''Person 0: Aliko Dangote
Person 1: Bill Gates
Person 2: Warren Buffet
Person 3: Elon Musk
Person 4: Warren Musk'''
        actual_value = '\n'.join([str(p) for p in third_group])
        self.assertEqual(expected_value, actual_value)


if __name__ == "__main__":
    unittest.main()
