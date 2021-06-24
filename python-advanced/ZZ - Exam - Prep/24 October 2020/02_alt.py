from typing import List, Optional, Sized

SIZE = 8
EMPTY = '.'
QUEEN = 'Q'
KING = 'K'


class Cell:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j


class EmptyCell(Cell):
    pass


class QueenCell(Cell):
    pass


class KingCell(Cell):
    pass


class King:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j


class Queen:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j

    def __repr__(self) -> str:
        return f'[{self.i}, {self.j}]'


class CellFactory:
    def create_cell(self, type: str, i: int, j: int):
        cells = {
            EMPTY: EmptyCell,
            QUEEN: QueenCell,
            KING: KingCell,
        }
        return cells[type](i, j)


class Field:
    def __init__(self) -> None:
        self._size = SIZE
        self._factory = CellFactory()

    def _get_raw_data(self):
        return [input().split() for _ in range(self._size)]

    def _populate_cells(self):
        raw_data = self._get_raw_data()

        self._cells = []
        for i in range(self._size):
            row = []
            for j in range(self._size):
                type = raw_data[i][j]
                if type == KING:
                    self._king_position = (i, j)
                row.append(self._factory.create_cell(type, i, j))
            self._cells.append(row)

    def _within_bounds(self, i: int, j: int) -> bool:
        return 0 <= i < self._size and 0 <= j < self._size

    def get_queens(self, king: King) -> List[Queen]:

        queens: List[Queen] = []
        ATTACK_DELTAS = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        for delta in ATTACK_DELTAS:
            i, j = king.i, king.j
            delta_i, delta_j = delta

            while True:
                i += delta_i
                j += delta_j

                if not self._within_bounds(i, j):
                    break

                next_cell = self._cells[i][j]

                if isinstance(next_cell, QueenCell):
                    queens.append(Queen(i, j))
                    break

        return queens


class Game:
    def __init__(self) -> None:
        self._field = Field()

    def setup(self):
        self._field._populate_cells()
        i, j = self._field._king_position
        self._king = King(i, j)

    def play(self):
        self._queens = self._field.get_queens(self._king)

    @property
    def info(self) -> str:
        message = []
        nl = '\n'
        for queen in self._queens:
            message.append(str(queen))

        return nl.join(message)


def main() -> None:
    check_mate = Game()
    check_mate.setup()
    check_mate.play()
    print(check_mate.info)


main()
