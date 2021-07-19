from typing import Generator


def reverse_text(text: str) -> Generator:
    i: int = len(text) - 1

    while i >= 0:
        yield text[i]
        i -= 1

for char in reverse_text("step"):
    print(char, end='')
