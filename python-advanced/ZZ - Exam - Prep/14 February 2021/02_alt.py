from typing import List, Tuple

PLAYER_MARKER = 'P'
WALL_MARKER = 'X'
COINS_TARGET = 100
EMPTY = '0'


class Player:
    def __init__(self) -> None:
        self.coins = 0
        self.__path = []
        self.has_lost = False

    def _set_position(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def _move(self, next_i: int, next_j: int) -> None:
        self.i = next_i
        self.j = next_j

    def collect_coins(self, value: int, position: Tuple[int, int]) -> None:
        self.coins += value
        self.__path.append(position)

    @property
    def _has_enough_coins(self) -> bool:
        return self.coins >= COINS_TARGET

    def __apply_penalty(self) -> None:
        self.coins //= 2

    def _lose_game(self) -> None:
        self.has_lost = True
        self.__apply_penalty()

    def _get_player_path(self) -> List:
        return [f'[{p[0]}, {p[1]}]' for p in self.__path]


class Game:
    def __init__(self) -> None:
        self.__field = []
        self.__player = Player()

    def __read_field_size(self) -> int:
        return int(input())

    def __populate_field(self, n: int):
        self.__size = n
        self.__field = [input().split() for _ in range(n)]

    def __get_player_position(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__field[i][j] == PLAYER_MARKER:
                    return i, j

    def setup(self):
        n = self.__read_field_size()
        self.__populate_field(n)
        self.__player._set_position(*self.__get_player_position())

    def __move_is_within(self, i: int, j: int) -> bool:
        return 0 <= i < self.__size and 0 <= j < self.__size

    def __player_make_turn(self, position: Tuple[int, int], new_position: Tuple[int, int]) -> None:
        i, j = position
        next_i, next_j = new_position
        self.__player._move(next_i, next_j)
        self.__field[next_i][next_j] = PLAYER_MARKER
        self.__field[i][j] = EMPTY

    def __player_take_coins(self, *args) -> None:
        (i, j), (next_i, next_j) = args[0], args[1]

        value = int(self.__field[next_i][next_j])
        position = (next_i, next_j)

        self.__player.collect_coins(value, position)
        self.__player_make_turn(*args)

    def __player_hit_wall(self, *args) -> None:
        self.__player_make_turn(*args)
        self.__player._lose_game()

    @staticmethod
    def __cell_has_coins(x: str) -> bool:
        return x.isdecimal()

    def __move_player(self, direction: str):
        i, j = self.__player.i, self.__player.j

        DELTAS = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        delta_i, delta_j = DELTAS[direction]
        next_i, next_j = self.__player.i + delta_i, self.__player.j + delta_j

        if not self.__move_is_within(next_i, next_j):
            self.__player._lose_game()

        next_cell = self.__field[next_i][next_j]

        if next_cell == WALL_MARKER:
            self.__player_hit_wall((i, j), (next_i, next_j))

        elif self.__cell_has_coins(next_cell):
            self.__player_take_coins((i, j), (next_i, next_j))

    def play(self) -> None:
        while True:
            if self.__player._has_enough_coins or self.__player.has_lost:
                return

            direction = input()
            self.__move_player(direction)

    def __str__(self) -> str:
        message = []
        nl = '\n'

        if self.__player.has_lost:
            message.append(
                f"Game over! You've collected {self.__player.coins} coins.")
        else:
            message.append(
                f"You won! You've collected {self.__player.coins} coins.")
        message.append('Your path:')
        message.extend(self.__player._get_player_path())

        return nl.join(message)


def main() -> None:
    game = Game()
    game.setup()
    game.play()
    print(game)


main()
