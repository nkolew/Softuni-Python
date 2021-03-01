class Party:
    def __init__(self) -> None:
        self.people = []

    def go(self, name):
        self.name = name
        self.people.append(name)

    def get_going(self):
        return f'Going: {", ".join(self.people)}'

    def get_count(self):
        return f'Total: {len(self.people)}'


p = Party()

while True:
    name = input()
    if name == 'End':
        break

    p.go(name)


print(p.get_going())
print(p.get_count())
