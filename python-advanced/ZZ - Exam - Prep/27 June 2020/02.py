SNAKE = 'S'
FOOD = '*'
BURROW = 'B'
EMPTY = '-'
TRAIL = '.'
FOOD_TARGET = 10


class Field:
    def __init__(self) -> None:
        self.field = None
        self.size = None
        self.snake = (None, None)
        self.lair = []
        self.food = 0

    def populate(self, n):
        self.field = [list(input()) for _ in range(n)]
        self.size = n
        self.snake = self.get_snake()
        self.lair = self.get_lair()

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def get_snake(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == SNAKE:
                    return (i, j)

    def get_lair(self):
        burrows = []
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == BURROW:
                    burrows.append((i, j))

        return burrows

    @property
    def snake_full(self):
        return self.food >= FOOD_TARGET

    def eat(self, current_position, next_position):
        i, j = current_position
        next_i, next_j = next_position
        self.snake = (next_i, next_j)
        self.field[next_i][next_j] = SNAKE
        self.field[i][j] = TRAIL

    def hide(self, current_position, current_burrow, next_burrow):
        i, j = current_position
        next_i, next_j = current_burrow
        jump_i, jump_j = next_burrow
        self.snake = next_burrow
        self.field[jump_i][jump_j] = SNAKE
        self.field[i][j] = TRAIL
        self.field[next_i][next_j] = TRAIL
        self.lair = []

    def move(self, direction) -> bool:
        game_on = True

        direction_deltas = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        i, j = self.snake
        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = i + delta_i, j + delta_j

        if not self.within_bounds(next_i, next_j):
            game_on = False
            self.field[i][j] = TRAIL
            return game_on

        next_position = (next_i, next_j)
        next_cell = self.field[next_i][next_j]

        if next_cell == FOOD:
            self.eat(self.snake, next_position)
            self.food += 1
            if self.snake_full:
                game_on = False
            return game_on

        elif next_cell == EMPTY:
            self.eat(self.snake, next_position)
            return game_on

        elif next_cell == BURROW:
            for i, current_burrow in enumerate(self.lair):
                if next_position == current_burrow:
                    next_burrow = self.lair[1] if i == 0 else self.lair[0]
                    self.hide(self.snake, current_burrow, next_burrow)
            return game_on

        return game_on

    def execute_commands(self):
        game_on = True
        while game_on:
            direction = input()
            game_on = self.move(direction)

    def __str__(self) -> str:
        res = []
        nl = '\n'
        if self.snake_full:
            res.append('You won! You fed the snake.')
        else:
            res.append('Game over!')
        res.append(f'Food eaten: {self.food}')
        for line in self.field:
            res.append(''.join(line))
        return nl.join(res)

    def __repr__(self) -> str:
        return f'{self.food}'


def main():
    field = Field()
    n = int(input())
    field.populate(n)
    field.execute_commands()
    print(field)


main()
