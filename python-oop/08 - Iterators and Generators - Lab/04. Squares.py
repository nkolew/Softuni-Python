from typing import Generator


def squares(n: int) -> Generator:
    i: int = 1

    while i <= n:
        yield i**2
        i += 1


print(list(squares(5)))
