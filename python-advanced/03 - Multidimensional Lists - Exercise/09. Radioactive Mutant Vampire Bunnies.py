from collections import deque
from typing import Deque, List, Tuple


PLAYER_MARKER = 'P'
BUNNY_MARKER = 'B'
EMPTY_MARKER = '.'


class Cell:
    def __init__(self, i, j) -> None:
        self.i: int = i
        self.j: int = j


class EmptyCell(Cell):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)
        self.marker = EMPTY_MARKER

    def __repr__(self) -> str:
        return f'{self.marker}'


class PlayerCell(Cell):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)
        self.marker = PLAYER_MARKER

    def __repr__(self) -> str:
        return f'{self.marker}'


class BunnyCell(Cell):
    def __init__(self, i, j) -> None:
        super().__init__(i, j)
        self.marker = BUNNY_MARKER

    def __repr__(self) -> str:
        return f'{self.marker}'


class CellFactory:
    def create_cell(self, type: str, i: int, j: int) -> Cell:

        cell_types = {
            'P': PlayerCell,
            'B': BunnyCell,
            '.': EmptyCell,
        }

        return cell_types[type](i, j)


class Lair:
    def __init__(self) -> None:
        self._cells = []
        self._factory = CellFactory()

    def populate_cells(self, field_data: List[List[str]]) -> None:

        self._rows = len(field_data)
        self._cols = len(field_data[0])

        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                type = field_data[i][j]
                cell = self._factory.create_cell(type, i, j)
                row.append(cell)
            self._cells.append(row)


class Player:
    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j
        self.is_dead = False
        self.has_escaped = False


class Game:
    def __init__(self) -> None:
        self.__player = None
        self.__lair = Lair()
        self.stats = GameStats()

    def parse_input_lines(self, n: int) -> None:

        field_data = [
            list(input())
            for _ in range(n)
        ]

        self.__lair.populate_cells(field_data)
        self.__place_player()

    @property
    def __player_start_position(self) -> Tuple[int, int]:
        for i in range(self.__lair._rows):
            for j in range(self.__lair._cols):
                cell = self.__lair._cells[i][j]
                if isinstance(cell, PlayerCell):
                    return i, j
        return (0, 0)

    def __place_player(self) -> None:
        i, j = self.__player_start_position
        self.__player = Player(i, j)

    def __move_is_within(self, i: int, j: int):
        return 0 <= i < self.__lair._rows and 0 <= j < self.__lair._cols

    def __move_player(self, direction) -> None:

        direction_deltas = {
            'L': (0, -1),
            'U': (-1, 0),
            'R': (0, 1),
            'D': (1, 0),
        }

        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = self.__player.i + delta_i, self.__player.j + delta_j

        if not self.__move_is_within(next_i, next_j):
            self.__player.has_escaped = True
            self.__lair._cells[self.__player.i][self.__player.j] = \
                self.__lair._factory.create_cell(
                    EMPTY_MARKER, self.__player.i, self.__player.i)
            return

        next_cell = self.__lair._cells[next_i][next_j]

        if isinstance(next_cell, EmptyCell):

            self.__lair._cells[next_i][next_j] = \
                self.__lair._factory.create_cell(PLAYER_MARKER, next_i, next_j)
            self.__lair._cells[self.__player.i][self.__player.j] = \
                self.__lair._factory.create_cell(
                    EMPTY_MARKER, self.__player.i, self.__player.i)
            self.__player.i = next_i
            self.__player.j = next_j

            return

        elif isinstance(next_cell, BunnyCell):

            self.__lair._cells[next_i][next_j] = \
                self.__lair._factory.create_cell(BUNNY_MARKER, next_i, next_j)
            self.__lair._cells[self.__player.i][self.__player.j] = \
                self.__lair._factory.create_cell(
                    EMPTY_MARKER, self.__player.i, self.__player.i)
            self.__player.i = next_i
            self.__player.j = next_j
            self.__player.is_dead = True

            return

        return

    @property
    def __bunnies(self) -> List[BunnyCell]:
        return [self.__lair._cells[i][j]
                for i in range(self.__lair._rows)
                for j in range(self.__lair._cols)
                if isinstance(self.__lair._cells[i][j], BunnyCell)]

    def __spread_bunnies(self) -> None:

        spread_direction_deltas = [
            (0, -1),
            (-1, 0),
            (0, 1),
            (1, 0),
        ]

        bunnies: Deque[BunnyCell] = deque(self.__bunnies)

        while True:
            if not bunnies:
                break

            bunny = bunnies.popleft()

            for delta in spread_direction_deltas:

                delta_i, delta_j = delta
                next_i, next_j = bunny.i + delta_i, bunny.j + delta_j

                if not self.__move_is_within(next_i, next_j):
                    continue

                next_cell = self.__lair._cells[next_i][next_j]

                if isinstance(next_cell, EmptyCell):
                    self.__lair._cells[next_i][next_j] = \
                        self.__lair._factory.create_cell(
                            BUNNY_MARKER, next_i, next_j)

                elif isinstance(next_cell, PlayerCell):
                    self.__player.is_dead = True
                    self.__lair._cells[next_i][next_j] = \
                        self.__lair._factory.create_cell(
                            BUNNY_MARKER, next_i, next_j)

    def __decide_outcome(self) -> None:
        GAME_WON = 'won'
        GAME_LOST = 'dead'

        if self.__player.has_escaped:
            self.stats.set_outcome(GAME_WON)
        else:
            self.stats.set_outcome(GAME_LOST)

    @property
    def __final_state(self) -> List[List[str]]:
        final_state = []
        for i in range(self.__lair._rows):
            row = []
            for j in range(self.__lair._cols):
                row.append(str(self.__lair._cells[i][j]))
            final_state.append(row)
        return final_state

    def __pass_final_state(self) -> None:
        self.stats.set_final_state(
            self.__final_state, self.__player.i, self.__player.j)

    def play(self, directions: Deque[str]) -> None:
        while True:
            if self.__player.is_dead or \
                    self.__player.has_escaped:
                break

            direction = directions.popleft()
            self.__move_player(direction)

            self.__spread_bunnies()
            if self.__player.is_dead:
                break

        self.__decide_outcome()
        self.__pass_final_state()


class GameStats:
    def set_outcome(self, outcome: str) -> None:
        self.outcome = outcome

    def set_final_state(self, final_state: List[List[str]], i: int, j: int) -> None:
        self.final_state = final_state
        self.player_i = i
        self.player_j = j

    def __str__(self) -> str:
        message = []
        nl = '\n'

        for row in self.final_state:
            message.append(''.join(row))

        message.append(f'{self.outcome}: {self.player_i} {self.player_j}')

        return nl.join(message)


def main() -> None:
    game = Game()
    n, _ = [int(x) for x in input().split()]
    game.parse_input_lines(n)
    directions = deque(input())
    game.play(directions)
    print(game.stats)


main()
