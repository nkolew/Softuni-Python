class take_skip:
    step: int
    count: int

    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.i = 0

    def __iter__(self) -> 'take_skip':
        return self

    def __next__(self) -> int:
        i = self.i

        if self.count == 0:
            raise StopIteration()

        self.i += self.step
        self.count -= 1

        return i


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
