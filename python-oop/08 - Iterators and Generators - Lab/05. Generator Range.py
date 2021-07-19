from typing import Generator


def genrange(start: int, end: int) -> Generator:
    i: int = start

    while i <= end:
        yield i
        i += 1


print(list(genrange(1, 10)))
