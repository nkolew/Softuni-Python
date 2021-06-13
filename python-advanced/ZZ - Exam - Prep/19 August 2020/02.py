MINE = '*'


class MinesWeeper:
    def __init__(self) -> None:
        self.field = None
        self.size = None
        self.bombs = None

    def populate(self, n, bombs_count):
        self.field = [[0]*n for i in range(n)]
        self.size = n
        self.bombs = bombs_count

    def place_mine(self, i, j):
        self.field[i][j] = MINE

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def calc_cell_value(self, i, j):

        direction_deltas = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        cell_value = 0

        for direction in direction_deltas:
            delta_i, delta_j = direction
            next_i, next_j = i, j

            while True:
                next_i += delta_i
                next_j += delta_j

                if not self.within_bounds(next_i, next_j):
                    break

                if self.field[next_i][next_j] == MINE:
                    cell_value += 1

                break

        return cell_value

    def calc_field(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] != MINE:
                    cell_value = self.calc_cell_value(i, j)
                    self.field[i][j] = cell_value

    def __repr__(self) -> str:
        res = []
        for line in self.field:
            res.append(' '.join(str(x) for x in line))
        return '\n'.join(res)


def main():
    n = int(input())
    mines_count = int(input())
    mines = MinesWeeper()
    mines.populate(n, mines_count)

    for _ in range(mines_count):
        i, j = [int(x) for x in input()[1:-1].split(', ')]
        mines.place_mine(i, j)

    mines.calc_field()
    print(mines)


main()
