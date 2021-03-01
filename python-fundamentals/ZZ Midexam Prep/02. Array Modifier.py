class ArrayModifier:
    def __init__(self, l: list) -> None:
        self.l = l

    def swap(self, i1: int, i2: int):
        self.l[i1], self.l[i2] = self.l[i2], self.l[i1]

    def multiply(self, i1: int, i2: int):
        self.l[i1] = self.l[i1] * self.l[i2]

    def decrease(self):
        self.l = list(map(lambda e: e-1, self.l))

    def __repr__(self) -> str:
        return f'{", ".join(map(str, self.l))}'


array = list(map(int, input().split()))
am = ArrayModifier(array)

while True:
    tokens = input()
    if tokens == 'end':
        break
    command = tokens.split()[0]
    if command == 'swap':
        idx1, idx2 = int(tokens.split()[1]), int(tokens.split()[2])
        am.swap(idx1, idx2)
    elif command == 'multiply':
        idx1, idx2 = int(tokens.split()[1]), int(tokens.split()[2])
        am.multiply(idx1, idx2)
    elif command == 'decrease':
        am.decrease()

print(am)
