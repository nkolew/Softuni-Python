class reverse_iter:
    iterable_: list
    i: int

    def __init__(self, iterable_) -> None:
        self.iterable_ = iterable_
        self.i = len(self.iterable_)-1

    def __iter__(self) -> 'reverse_iter':
        return self

    def __next__(self):
        if self.i < 0:
            raise StopIteration()

        i = self.i
        self.i -= 1
        return self.iterable_[i]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
