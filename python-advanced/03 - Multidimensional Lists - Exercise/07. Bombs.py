class Field:
    def __init__(self) -> None:
        self.field = None
        self.size = None

    def populate(self, n):
        self.field = [[int(x) for x in input().split()] for _ in range(n)]
        self.size = len(self.field)

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def detonate(self, i, j):
        attack_deltas = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        damage = self.field[i][j]
        self.field[i][j] = 0

        if damage <= 0:
            return

        for delta in attack_deltas:

            delta_i, delta_j = delta
            next_i, next_j = i + delta_i, j + delta_j

            while True:
                if not self.within_bounds(next_i, next_j):
                    break

                self.field[next_i][next_j] -= damage
                break
            return

    @property
    def alive_cels(self):
        return sum(1 for i in range(self.size) for j in range(self.size) if self.field[i][j] > 0)

    @property
    def field_sum(self):
        return sum(self.field[i][j] for i in range(self.size) for j in range(self.size))

    def __str__(self) -> str:
        res = []
        res.append(f'Alive cells: {self.alive_cels}')
        res.append(f'Sum: {self.field_sum}')
        for line in self.field:
            res.append(' '.join(map(str, line)))

        return '\n'.join(res)


def main():
    n = int(input())
    field = Field()
    field.populate(n)

    bomb_positions = input().split()
    for position in bomb_positions:
        i, j = position.split(',')
        i, j = int(i), int(j)
        field.detonate(i, j)

    print(field)


main()
