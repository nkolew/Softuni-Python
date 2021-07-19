from typing import Any, Sequence


class sequence_repeat:
    __sequence: Sequence[Any]
    __number: int

    def __init__(self, sequence, number) -> None:
        self.__sequence = sequence
        self.__number = number
        self.__index = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == self.__number:
            raise StopIteration()

        idx, self.__index = self.__index, self.__index+1
        return self.__sequence[idx % len(self.__sequence)]


result = sequence_repeat('abc', 500)
for item in result:
    print(item, end='')
