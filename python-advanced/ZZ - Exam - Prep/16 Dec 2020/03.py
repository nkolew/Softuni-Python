import unittest


def get_magic_triangle(n):
    res = []
    for i in range(n):
        next_row = []
        if i == 0:
            next_row = [1]
            res.append(next_row)
        elif i == 1:
            next_row = [1, 1]
            res.append(next_row)
        else:
            next_row = [1]*(i+1)
            for j in range(len(next_row)-1):
                if 1 <= j <= len(res[-1]):
                    next_row[j] = res[i-1][j-1] + res[i-1][j]
                else:
                    next_row[j] = 1
            res.append(next_row)

    return res


class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
