class ShoppingList:
    def __init__(self, l: list) -> None:
        self.l = l

    def urgent(self, item: str):
        if item not in self.l:
            self.l.insert(0, item)

    def unnecessary(self, item: str):
        if item in self.l:
            while item in self.l:
                self.l.remove(item)

    def correct(self, old: str, new: str):
        if old in self.l:
            while old in self.l:
                idx = self.l.index(old)
                self.l.pop(idx)
                self.l.insert(idx, new)

    def rearrange(self, item: str):
        if item in self.l:
            old_counter = 0
            while item in self.l:
                self.l.remove(item)
                old_counter += 1
            for _ in range(old_counter):
                self.l.append(item)

    def __repr__(self) -> str:
        return f'{", ".join(self.l)}'


groceries = input().split('!')
g = ShoppingList(groceries)

while True:
    tokens = input()
    if tokens == 'Go Shopping!':
        break
    tokens = tokens.split()
    command = tokens[0]
    if command == 'Urgent':
        item = tokens[1]
        g.urgent(item)
    elif command == 'Unnecessary':
        item = tokens[1]
        g.unnecessary(item)
    elif command == 'Correct':
        old, new = tokens[1], tokens[2]
        g.correct(old, new)
    elif command == 'Rearrange':
        item = tokens[1]
        g.rearrange(item)

print(g)
