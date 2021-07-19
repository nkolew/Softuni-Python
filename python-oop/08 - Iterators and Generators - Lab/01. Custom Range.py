class custom_range:
    start: int
    end: int

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.i = self.start

    def __iter__(self) -> 'custom_range':
        return self

    def __next__(self) -> int:
        if self.i > self.end:
            raise StopIteration()

        i = self.i
        self.i += 1
        return i


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
