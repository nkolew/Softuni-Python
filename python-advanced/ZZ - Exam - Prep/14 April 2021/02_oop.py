from collections import deque
from typing import Deque, List, Tuple


STARTING_SCORE = 501
BOARD_SIZE = 7
DOUBLE = 'D'
TRIPLE = 'T'
BULL = 'B'


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.throws_count: int = 0
        self.score: int = STARTING_SCORE
        self.is_winner: bool = False

    @property
    def _throw_position(self) -> Tuple[int, int]:
        i, j = [int(x) for x in input()[1:-1].split(', ')]
        return (i, j)

    def __repr__(self) -> str:
        return f'Winner: {self.is_winner} -> {self.name}, Score: {self.score}, Throws: {self.throws_count}'


class DartsGame:
    def __init__(self) -> None:
        self.__size = BOARD_SIZE
        self.__board: List[List[str]] = []
        self.__players: Deque[Player] = deque()

    def __populate_players(self) -> None:
        self.__players = deque(Player(x) for x in input().split(', '))

    def __populate_board(self) -> None:
        self.__board = [input().split() for n in range(self.__size)]

    def __throw_inside(self, i: int, j: int) -> bool:
        return 0 <= i < self.__size and 0 <= j < self.__size

    def __get_hit_score(self, i: int, j: int) -> int:

        base_score = sum(
            map(int,
                [
                    self.__board[i][0],
                    self.__board[i][self.__size-1],
                    self.__board[0][j],
                    self.__board[self.__size-1][j],
                ]
                ))

        score_factors = {
            DOUBLE: lambda x: 2*x,
            TRIPLE: lambda x: 3*x,
            BULL: lambda x: STARTING_SCORE
        }

        hit = self.__board[i][j]
        if hit.isdigit():
            return int(hit)

        return score_factors[hit](base_score)

    def play(self) -> None:
        self.__populate_players()
        self.__populate_board()

        while True:

            player = self.__players.popleft()
            player.throws_count += 1
            i, j = player._throw_position

            if not self.__throw_inside(i, j):
                self.__players.append(player)
                continue

            player.score -= self.__get_hit_score(i, j)
            if player.score <= 0:
                player.is_winner = True
                self.__players.append(player)
                return

    def __str__(self) -> str:
        message = []
        nl = '\nl'

        while self.__players:
            player = self.__players.popleft()
            if player.is_winner:
                message.append(
                    f'{player.name} won the game with {player.throws_count} throws!')

        return nl.join(message)


def main() -> None:
    game = DartsGame()
    game.play()
    print(game)


main()
