from typing import ClassVar, Set


class vowels:
    text: str
    i: int

    _VOWELS: ClassVar[Set[str]] = {'A', 'E', 'I', 'O', 'U', 'Y'} | \
        set(map(lambda s: s.lower(), {'A', 'E', 'I', 'O', 'U', 'Y'}))

    def __init__(self, text: str) -> None:
        self.text = text
        self.i = 0

    def __iter__(self) -> 'vowels':
        return self

    def __next__(self) -> str:
        if self.i == len(self.text):
            raise StopIteration()

        c = self.text[self.i]
        self.i += 1

        if c not in self.__class__._VOWELS:
            return self.__next__()

        return c


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
