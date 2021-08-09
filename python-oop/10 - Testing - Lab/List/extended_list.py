class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)


import unittest

class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.list_integers = IntegerList([5, 6, 7])

    def test_init_create_all_attributes(self):
        self.assertEqual(self.list_integers, self.list_integers._IntegerList__data)

    def test_int_takes_not_integers(self):
        list_integers = IntegerList(5.6, '6', 7)
        self.assertEqual([], list_integers._IntegerList__data)

    def test_add_integer_is_added(self):
        pass

if __name__ == "__main__":
    unittest.main()