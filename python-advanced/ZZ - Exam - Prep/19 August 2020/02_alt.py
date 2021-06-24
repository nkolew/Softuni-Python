from collections import deque
from typing import Deque, Dict, List, Type

EMPTY = '0'
MINE = '*'


class Mine:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j


class Cell:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j


class MineCell(Cell):
    def __repr__(self) -> str:
        return '*'


class EmptyCell(Cell):
    def __init__(self, i: int, j: int) -> None:
        super().__init__(i, j)
        self._value = 0

    def __repr__(self) -> str:
        return f'{self._value}'


class CellFactory:
    def create_cell(self, type: str, i: int, j: int) -> Cell:

        cells: Dict[str, Type[Cell]] = {
            EMPTY: EmptyCell,
            MINE: MineCell,
        }

        return cells[type](i, j)


class Field:
    def __init__(self) -> None:
        self._factory = CellFactory()
        self._cells = []

    def _populate_cells(self, n: int) -> None:
        self._size = n
        self._cells: List[List[Cell]] = [
            [self._factory.create_cell(EMPTY, i, j) for j in range(n)]
            for i in range(n)
        ]

    def _within_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self._size and 0 <= j < self._size

    def _detonate_mine(self, i: int, j: int) -> None:

        DIRECTION_DELTAS = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        for delta in DIRECTION_DELTAS:
            delta_i, delta_j = delta

            next_i, next_j = i + delta_i, j + delta_j

            if not self._within_bounds(next_i, next_j):
                continue

            next_cell = self._cells[next_i][next_j]

            if isinstance(next_cell, EmptyCell):
                next_cell._value += 1

    def get_stats(self) -> str:
        message = []
        nl = '\n'

        for i in range(self._size):
            row = []
            for j in range(self._size):
                row.append(str(self._cells[i][j]))
            message.append(' '.join(row))

        return nl.join(message)


class MinesBox:
    def __init__(self) -> None:
        self._mines: Deque[Mine] = deque()

    def _load_mines(self, m: int) -> None:
        for _ in range(m):
            i, j = map(int, (input()[1:-1].split(', ')))
            self._mines.append(Mine(i, j))

    def _engage_mine(self):
        return self._mines.popleft()


class Game:
    def __init__(self) -> None:
        self._field = Field()
        self._mines_box = MinesBox()

    def setup(self) -> None:
        n = int(input())
        m = int(input())
        self._field._populate_cells(n)
        self._mines_box._load_mines(m)

    def play(self) -> None:
        while self._mines_box._mines:
            mine = self._mines_box._engage_mine()
            self._field._cells[mine.i][mine.j] = \
                self._field._factory.create_cell(MINE, mine.i, mine.j)
            self._field._detonate_mine(mine.i, mine.j)

    @property
    def stats(self) -> str:
        return self._field.get_stats()


def main() -> None:
    game = Game()
    game.setup()
    game.play()
    print(game.stats)


main()
