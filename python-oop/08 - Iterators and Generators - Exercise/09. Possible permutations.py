from itertools import permutations
from typing import Any, Generator, List


def possible_permutations(seq: List[Any]) -> Generator:
    return (list(p) for p in permutations(seq))


[print(n) for n in possible_permutations([1, 2, 3])]
