from collections import deque
from typing import Deque, List, Tuple


class Bomb:
    def __init__(self, i, j, damage) -> None:
        self.i = i
        self.j = j
        self.damage = damage

    def update_damage(self, damage: int):
        self.damage = damage

    @property
    def is_dead(self) -> bool:
        return self.damage <= 0

    def __repr__(self) -> str:
        return f'{"+" if not self.is_dead else "-"} ({self.i}, {self.j}) -> {self.damage}'


class Field:
    def __init__(self) -> None:
        self.__field: List[List[int]] = []
        self.__size: int = 0
        self.__bombs: Deque[Bomb] = deque()

    def populate_cells(self, n: int) -> None:
        self.__field = [
            [int(x) for x in input().split()]
            for _ in range(n)
        ]
        self.__size = n

    def set_bombs(self, data: str):
        self.__bombs = deque((
            self.__create_bomb(position)
            for position in self.get_positions_from_data(data)
        ))

    def __create_bomb(self, position: Tuple[int, int]):
        i, j = position
        damage: int = self.__field[i][j]
        return Bomb(i, j, damage)

    @staticmethod
    def get_positions_from_data(data: str) -> List[Tuple[int, int]]:
        bomb_positions = []
        bombs = data.split()
        for bomb in bombs:
            coordinates = bomb.split(',')
            i, j = int(coordinates[0]), int(coordinates[1])
            bomb_positions.append((i, j))

        return bomb_positions

    def engage_bombs(self):
        while self.__bombs:
            bomb = self.__bombs.popleft()
            self.__detonate_bomb(bomb)

    def __detonate_bomb(self, bomb: Bomb) -> None:

        damage = self.__field[bomb.i][bomb.j]
        bomb.update_damage(damage)

        if bomb.is_dead:
            return

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

        for delta in direction_deltas:
            delta_i, delta_j = delta
            next_i, next_j = bomb.i + delta_i, bomb.j + delta_j

            if not self.__cell_within_field(next_i, next_j) \
                    or not self.__cell_alive(next_i, next_j):
                continue

            self.__field[next_i][next_j] -= bomb.damage

        self.__field[bomb.i][bomb.j] = 0
        return

    def __cell_within_field(self, i: int, j: int) -> bool:
        return 0 <= i < self.__size and 0 <= j < self.__size

    def __cell_alive(self, i, j):
        return self.__field[i][j] > 0

    @ property
    def __alive_cells(self):
        return [self.__field[i][j]
                for i in range(self.__size)
                for j in range(self.__size)
                if self.__field[i][j] > 0]

    def __str__(self) -> str:
        message = []
        nl = '\n'
        alive_cels = self.__alive_cells

        message.append(f'Alive cells: {len(alive_cels)}')
        message.append(f'Sum: {sum(alive_cels)}')
        for row in self.__field:
            message.append(' '.join(map(str, row)))

        return nl.join(message)

    def __repr__(self) -> str:
        res = []
        nl = '\n'
        for row in self.__field:
            res.append(' '.join(map(str, row)))
        return nl.join(res)


def main():
    field = Field()
    n = int(input())
    field.populate_cells(n)
    bomb_data = input()
    field.set_bombs(bomb_data)
    field.engage_bombs()
    print(field)


main()
