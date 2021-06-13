PLAYER = 'P'
EMPTY = '-'


class Field:
    def __init__(self) -> None:
        self._field = None
        self.size = None
        self.player = (None, None)
        self.chars = []

    def read_field(self, n, init_chars):
        self.field = [list(input()) for _ in range(n)]
        self.chars.extend(init_chars)
        self.size = len(self.field)

    @property
    def player_position(self):
        for i, row in enumerate(self.field):
            if PLAYER in row:
                j = row.index(PLAYER)
                return (i, j)
        return (None, None)

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def move(self, direction):
        direction_deltas = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        if not all(self.player):
            self.player = self.player_position

        i, y = self.player
        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = i + delta_i, y + delta_j

        if not self.within_bounds(next_i, next_j):
            self.chars.pop()
            return

        next_move = self.field[next_i][next_j]
        if next_move != EMPTY:
            self.chars.append(next_move)

        self.player = (next_i, next_j)
        self.field[i][y] = '-'
        self.field[next_i][next_j] = PLAYER

    def __repr__(self) -> str:
        res = []
        res.append(''.join(self.chars))
        for row in self.field:
            res.append(''.join(row))
        return '\n'.join(res)


def main():

    init_chars = list(input())
    n = int(input())

    field = Field()

    field.read_field(n, init_chars)

    m = int(input())
    for _ in range(m):
        direction = input()
        field.move(direction)

    print(field)


main()
