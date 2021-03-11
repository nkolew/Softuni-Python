from collections import defaultdict


class Dwarf:
    def __init__(self, name: str, color: str, physics: int) -> None:
        self.name = name
        self.color = color
        self.id = (name, color)
        self.physics = physics
        self.count = 0

    def update(self, new_physics: int):
        self.physics = new_physics

    def set_count(self, c: int):
        self.count = c

    def __repr__(self) -> str:
        return f'{self.color}) {self.name} <-> {self.physics}'


class Order:
    def __init__(self) -> None:
        self.dwarfs = []

    def add(self, d: Dwarf):
        new = True
        for dwarf in self.dwarfs:
            if dwarf.id == d.id:
                new = False
                if dwarf.physics < d.physics:
                    dwarf.update(d.physics)
        if new:
            self.dwarfs.append(d)

    def __repr__(self) -> str:
        dwarfs_colors = defaultdict(int)
        for d in self.dwarfs:
            dwarfs_colors[d.color] += 1

        for dwarf in self.dwarfs:
            dwarf.set_count(dwarfs_colors[dwarf.color])

        result = []
        for dwarf in sorted(self.dwarfs, key=lambda x: (-x.physics, -x.count)):
            result.append(f'({dwarf.color}) {dwarf.name} <-> {dwarf.physics}')
        nl = '\n'
        return nl.join(result)


o = Order()

while True:
    data = input()
    if data == 'Once upon a time':
        break
    name, color, physics = data.split(' <:> ')
    physics = int(physics)
    o.add(Dwarf(name, color, physics))

print(o)
