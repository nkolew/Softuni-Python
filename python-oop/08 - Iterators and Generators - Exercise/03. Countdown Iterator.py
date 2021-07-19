from typing import Iterator


class countdown_iterator:
    count: int

    def __init__(self, count: int) -> None:
        self.count = count
        self.__current = self.count

    def __iter__(self) -> Iterator:
        self.__current = self.count
        return self

    def __next__(self) -> int:
        if self.__current < 0:
            raise StopIteration()

        i, self.__current = self.__current, self.__current-1
        return i


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
