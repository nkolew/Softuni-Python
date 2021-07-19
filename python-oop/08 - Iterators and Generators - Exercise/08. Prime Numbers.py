from typing import Generator, List
import math


def is_prime(num: int) -> bool:
    if num in (0, 1):
        return False

    for n in range(2, int(math.sqrt(num)+1)):
        if num % n == 0:
            return False

    return True


def get_primes(nums: List[int]) -> Generator:
    return (n for n in nums if is_prime(n))


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
