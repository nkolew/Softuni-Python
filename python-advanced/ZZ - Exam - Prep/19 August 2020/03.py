def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    unique_nums = set()
    duplicates = set()
    missing_num = None

    for num in range(min_num, max_num):
        if num not in args:
            missing_num = num

    for num in args:
        if num in unique_nums:
            duplicates.add(num)
        unique_nums.add(num)

    return [missing_num, [*sorted(duplicates)]]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48,
      45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [6, [5, 7, 9]]
        result = numbers_searching(5, 5, 9, 10, 7, 8, 7, 9)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()