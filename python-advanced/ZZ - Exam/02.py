from collections import deque

SIZE = 5
PLAYER = 'A'
TARGET = 'x'
EMPTY = '.'


class ShotgunRange:
    def __init__(self) -> None:
        self._field = []
        self._player_i = 0
        self._player_j = 0
        self._targets = []
        self._targets_hit = []

    def _player_position(self):
        for i in range(self._size):
            for j in range(self._size):
                if self._field[i][j] == PLAYER:
                    return i, j
        return 0, 0

    def _get_targets(self):
        for i in range(self._size):
            for j in range(self._size):
                if self._field[i][j] == TARGET:
                    self._targets.append((i, j))

    def setup(self):
        self._size = SIZE
        self._field = [input().split() for _ in range(self._size)]
        self._player_i, self._player_j = self._player_position()
        self._get_targets()

    @property
    def has_targets(self):
        return len(self._targets) > 0

    def _move_is_within(self, i: int, j: int) -> bool:
        return 0 <= i < self._size and 0 <= j < self._size

    def _move(self, direction: str, steps: int):
        direction_deltas = {
            'left': (0, -steps),
            'up': (-steps, 0),
            'right': (0, steps),
            'down': (steps, 0),
        }

        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = self._player_i + delta_i, self._player_j + delta_j

        if not self._move_is_within(next_i, next_j):
            return

        if self._field[next_i][next_j] == EMPTY:
            self._field[self._player_i][self._player_j] = EMPTY
            self._field[next_i][next_j] = PLAYER
            self._player_i, self._player_j = next_i, next_j

    def _shoot(self, direction: str):
        direction_deltas = {
            'left': (0, -1),
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
        }

        delta_i, delta_j = direction_deltas[direction]
        next_i, next_j = self._player_i + delta_i, self._player_j + delta_j

        while True:

            if not self._move_is_within(next_i, next_j):
                return

            if self._field[next_i][next_j] == TARGET:
                self._field[next_i][next_j] = EMPTY
                self._targets.remove((next_i, next_j))
                self._targets_hit.append((next_i, next_j))
                return

            next_i, next_j = next_i + delta_i, next_j + delta_j

    def _execute(self, command, *args):
        commands = {
            'move': self._move,
            'shoot': self._shoot,
        }

        commands[command](*args)

    def tokens_are_valid(self, tokens):
        args = tokens.split()
        command = args[0]
        directions = ('left', 'up', 'right', 'down')
        if command == 'move':
            direction, steps = args[1], args[2]
            return direction in directions and steps.isdigit()
        elif command == 'shoot':
            direction = args[1]
            return direction in directions

    def _take_commands(self):
        commands = deque()
        cmd_count = int(input())
        command, direction, steps = None, None, None

        for _ in range(cmd_count):
            tokens = input()

            if not self.tokens_are_valid(tokens):
                continue

            if tokens.startswith('shoot '):
                command, direction = tokens.split()

            elif tokens.startswith('move '):
                command, direction, steps = tokens.split()
                steps = int(steps)

            commands.append((command, direction, steps)
                            if command == 'move' else (command, direction))

        return commands

    def play(self):
        commands = self._take_commands()

        while True:

            if not self.has_targets:
                return

            if not commands:
                return

            command, *tokens = commands.popleft()
            self._execute(command, *tokens)

    def __repr__(self) -> str:
        message = []
        nl = '\n'

        if not self.has_targets:
            message.append(
                f'Training completed! All {len(self._targets_hit)} targets hit.')
        else:
            message.append(
                f'Training not completed! {len(self._targets)} targets left.')
        for i, j in self._targets_hit:
            message.append(f'[{i}, {j}]')

        return nl.join(message)


def main():
    shoot_game = ShotgunRange()
    shoot_game.setup()
    shoot_game.play()
    print(shoot_game)


main()
