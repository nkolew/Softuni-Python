from collections import defaultdict
from typing import DefaultDict, List, Tuple


class ChessBoard:
    def __init__(self) -> None:
        self.__board = [list(input()) for _ in range(int(input()))]
        self.size = len(self.__board)

    @property
    def knights(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(self.size)
                for j in range(self.size) if self.__board[i][j] == 'K']

    def valid_positions(self, x, y) -> bool:
        return 0 <= x < self.size and 0 <= y < self.size

    def get_knights_histo(self) -> DefaultDict[Tuple[int, int], int]:
        TARGET_DELTAS = [
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
        ]

        knights_histo = defaultdict(int)
        for i in range(len(self.knights)):
            x, y = self.knights[i][0], self.knights[i][1]
            for j in range(len(TARGET_DELTAS)):
                delta_x, delta_y = TARGET_DELTAS[j][0], TARGET_DELTAS[j][1]
                pos_x, pos_y = x + delta_x, y + delta_y
                if self.valid_positions(pos_x, pos_y):
                    if self.__board[pos_x][pos_y] == 'K':
                        knights_histo[(x, y)] += 1
        return knights_histo

    def remove_knight(self, coord: Tuple[int, int]) -> None:
        x, y = coord
        self.__board[x][y] = '0'

    def iterate_over_knights(self) -> int:
        removed_knights = 0
        while True:
            knigthts_histo = self.get_knights_histo()
            if not knigthts_histo:
                return removed_knights
            knights = [k for k, _ in sorted(
                knigthts_histo.items(),
                key=lambda x: -x[1])]
            best_knight = knights[0]
            self.remove_knight(best_knight)
            removed_knights += 1


def main():
    board = ChessBoard()
    removed_knights = board.iterate_over_knights()
    print(removed_knights)


main()
