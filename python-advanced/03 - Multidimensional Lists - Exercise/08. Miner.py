from typing import Deque, List, Tuple
from collections import deque


EMPTY_CELL_MARKER = '*'
COAL_CELL_MARKER = 'c'
START_MARKER = 's'
END_MARKER = 'e'


class Cell:
    def __init__(self, type, i, j) -> None:
        self.type = type
        self.i = i
        self.j = j

    def __repr__(self) -> str:
        return f'{self.type} @ ({self.i}, {self.j})'


class Miner:
    def __init__(self, i: int, j: int) -> None:
        self.i = i
        self.j = j
        self.collected_coal = 0
        self.has_reached_end_marker = False

    def __repr__(self) -> str:
        return f'({self.i}, {self.j}), collected {self.collected_coal} coal'


class Field:
    def __init__(self) -> None:
        self.__field: List[List[Cell]] = []
        self.__size: int = 0
        self.__miner = None
        self.coals = 0

    @staticmethod
    def __read_input_lines(n: int) -> List[List[str]]:

        field_data = [
            input().split()
            for _ in range(n)
        ]

        return field_data

    def populate_cells(self, n: int) -> None:
        self.__size = n
        field_data = self.__read_input_lines(n)

        for i in range(self.__size):
            row = []
            for j in range(self.__size):
                cell = Cell(field_data[i][j], i, j)
                row.append(cell)
            self.__field.append(row)

    @property
    def coal_left(self) -> int:
        return len([
            COAL_CELL_MARKER
            for i in range(self.__size)
            for j in range(self.__size)
            if self.__field[i][j].type == COAL_CELL_MARKER
        ])

    @property
    def has_coal_left(self) -> bool:
        return self.coal_left > 0

    @property
    def __miner_start_position(self) -> Tuple[int, int]:
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__field[i][j].type == START_MARKER:
                    return i, j
        return (0, 0)

    def __place_miner(self) -> None:
        i, j = self.__miner_start_position
        self.__field[i][j].type = EMPTY_CELL_MARKER
        self.__miner = Miner(i, j)

    def __move_is_within(self, i: int, j: int):
        return 0 <= i < self.__size and 0 <= j < self.__size

    def __move_miner(self, direction) -> None:
        if not self.has_coal_left:
            return

        direction_deltas = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = self.__miner.i + delta_i, self.__miner.j + delta_j

        if not self.__move_is_within(next_i, next_j):
            return

        self.__miner.i, self.__miner.j = next_i, next_j
        next_cell = self.__field[next_i][next_j]

        if next_cell.type == COAL_CELL_MARKER:
            next_cell.type = EMPTY_CELL_MARKER
            self.__miner.collected_coal += 1
            if not self.has_coal_left:
                return

        if next_cell.type == END_MARKER:
            self.__miner.has_reached_end_marker = True
            next_cell.type = EMPTY_CELL_MARKER

        return

    def execute(self, directions: Deque[str]) -> None:
        self.__place_miner()

        while True:
            if self.__miner.has_reached_end_marker:
                break

            if not directions:
                break

            direction = directions.popleft()
            self.__move_miner(direction)

    def __str__(self) -> str:
        message = []
        nl = '\n'

        if self.has_coal_left and self.__miner.has_reached_end_marker:
            message.append(f'Game over! ({self.__miner.i}, {self.__miner.j})')
        elif not self.has_coal_left:
            message.append(
                f'You collected all coals! ({self.__miner.i}, {self.__miner.j})')
        if self.has_coal_left and not self.__miner.has_reached_end_marker:
            message.append(
                f'{self.coal_left} coals left. ({self.__miner.i}, {self.__miner.j})')

        return nl.join(message)


def main():
    n = int(input())
    directions = deque(input().split())
    field = Field()
    field.populate_cells(n)
    field.execute(directions)
    print(field)


main()
