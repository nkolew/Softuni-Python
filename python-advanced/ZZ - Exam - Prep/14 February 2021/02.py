PLAYER = 'P'
WALL = 'X'


class Field:
    def __init__(self) -> None:
        self.field = []
        self.size = 0
        self.player = (0, 0)
        self.player_path = []
        self.coins = 0
        self.player_won = False

    def read_field(self, n):
        self.field = [input().split() for _ in range(n)]
        self.size = len(self.field)

    @property
    def player_position(self):
        for i, row in enumerate(self.field):
            if PLAYER in row:
                j = row.index(PLAYER)
                return (i, j)
        return (0, 0)

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def move(self, direction):
        game_on = True

        direction_deltas = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        if direction in direction_deltas:
            if not all(self.player):
                self.player = self.player_position

            i, j = self.player
            delta_i, delta_j = direction_deltas[direction]
            next_i, next_j = i + delta_i, j + delta_j

            if not self.within_bounds(next_i, next_j) or \
                    self.field[next_i][next_j] == WALL:
                self.coins //= 2
                game_on = False
                return game_on

            next_move = self.field[next_i][next_j]
            self.player = (next_i, next_j)
            self.player_path.append(self.player)
            self.field[i][j] = '0'
            self.field[next_i][next_j] = PLAYER
            self.coins += int(next_move)

            if self.coins >= 100:
                game_on = False
                self.player_won = True
                return game_on
        return game_on

    def get_path(self):
        return '\n'.join(f'[{i[0]}, {i[1]}]' for i in self.player_path)

    def __repr__(self) -> str:
        res = []
        if self.player_won:
            res.append(f"You won! You've collected {self.coins} coins.")
        else:
            res.append(f"Game over! You've collected {self.coins} coins.")
        res.append('Your path:')
        res.append(self.get_path())
        return '\n'.join(res)


def main():
    n = int(input())
    field = Field()
    field.read_field(n)

    game_on = True
    while game_on:
        direction = input()
        game_on = field.move(direction)

    print(field)


main()
