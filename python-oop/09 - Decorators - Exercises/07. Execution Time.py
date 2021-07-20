import time
import unittest
from functools import wraps


def exec_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        return stop - start

    return wrapper


# test first zero


class ExecTimeTests(unittest.TestCase):
    def test_zero_first(self):
        @exec_time
        def loop(start, end):
            total = 0
            for x in range(start, end):
                total += x
            return total
        self.assertEqual(round(loop(1, 10000000)), 1)


if __name__ == '__main__':
    unittest.main()
