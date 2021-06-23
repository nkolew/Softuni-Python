import unittest


def get_magic_triangle(n: int):
    TOP_NUMBER = 1
    triangle = [[TOP_NUMBER]*(i+1) for i in range(n)]

    def cell_is_mutable(i: int, j: int) -> bool:
        return 0 <= i-1 < len(triangle) and \
            0 <= j-1 < len(triangle[i])

    def mutate_cell(i, j):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    for i in range(n):
        for j in range(i):
            if cell_is_mutable(i, j):
                mutate_cell(i, j)

    return triangle


class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
