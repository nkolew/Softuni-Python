from collections import deque
from typing import Dict, List, Tuple

PLAYER_MARKER = 'P'
EMPTY_MARKER = '-'


class Cell:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j


class PlayerCell(Cell):
    def __repr__(self) -> str:
        return PLAYER_MARKER


class EmptyCell(Cell):
    def __repr__(self) -> str:
        return EMPTY_MARKER


class LetterCell(Cell):
    def __init__(self, char: str, i: int, j: int) -> None:
        super().__init__(i, j)
        self.char = char

    def __repr__(self) -> str:
        return f'{self.char}'


class CellFactory:
    def create_cell(self, char: str, i: int, j: int) -> Cell:
        if char == PLAYER_MARKER:
            cell = PlayerCell(i, j)
        elif char == EMPTY_MARKER:
            cell = EmptyCell(i, j)
        else:
            cell = LetterCell(char, i, j)

        return cell


class Player:
    def __init__(self, initial: str, i: int, j: int) -> None:
        self.i = i
        self.j = j
        self._inventory = deque(initial)

    def take_reward(self, char: str) -> None:
        self._inventory.append(char)

    def take_penalty(self) -> None:
        if self._inventory:
            self._inventory.pop()

    @property
    def inventory(self) -> str:
        return f'{"".join(self._inventory)}'


class Game:
    def __init__(self) -> None:
        self._factory = CellFactory()

    def _init_field(self) -> None:
        self._size = int(input())
        self._field: List[List[Cell]] = []
        raw_data = [list(input()) for _ in range(self._size)]
        for i, row in enumerate(raw_data):
            cells: List[Cell] = []
            for j, char in enumerate(row):
                cells.append(self._factory.create_cell(char, i, j))
            self._field.append(cells)

    def _init_player(self, initial_chars):
        i, j = self._get_player_position()
        self._player = Player(initial_chars, i, j)

    def _get_player_position(self) -> Tuple[int, int]:
        for i in range(self._size):
            for j in range(self._size):
                if isinstance(self._field[i][j], PlayerCell):
                    return (i, j)
        return (0, 0)

    def setup(self) -> None:
        initial_chars = input()
        self._init_field()
        self._init_player(initial_chars)

    def _move_is_within(self, i: int, j: int) -> bool:
        return 0 <= i < self._size and 0 <= j < self._size

    def _step(self, next_cell: Cell):
        i, j = self._player.i, self._player.j
        next_i, next_j = next_cell.i, next_cell.j
        self._field[i][j] = self._factory.create_cell(EMPTY_MARKER, i, j)
        self._field[next_i][next_j] = self._factory.create_cell(
            PLAYER_MARKER, next_i, next_j)
        self._player.i, self._player.j = next_i, next_j

    def _step_on_letter(self, next_cell: LetterCell):
        self._player.take_reward(next_cell.char)
        self._step(next_cell)

    def _execute(self, direction):

        direction_deltas: Dict[str, Tuple[int, int]] = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = self._player.i + delta_i, \
            self._player.j + delta_j

        if not self._move_is_within(next_i, next_j):
            self._player.take_penalty()
            return

        next_cell = self._field[next_i][next_j]

        if isinstance(next_cell, LetterCell):
            self._step_on_letter(next_cell)
            return

        elif isinstance(next_cell, EmptyCell):
            self._step(next_cell)
            return

        return

    def play(self):

        directions = deque(input() for _ in range(int(input())))

        while directions:
            direction = directions.popleft()
            self._execute(direction)

    def get_stats(self) -> str:
        stats: List[str] = []
        nl = '\n'

        stats.append(self._player.inventory)

        for i in range(self._size):
            row = []
            for j in range(self._size):
                row.append(str(self._field[i][j]))
            stats.append(''.join(row))

        return nl.join(stats)


def main() -> None:
    game = Game()
    game.setup()
    game.play()
    print(game.get_stats())


main()
