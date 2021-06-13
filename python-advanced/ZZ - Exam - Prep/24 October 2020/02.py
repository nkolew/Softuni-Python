KING = 'K'
QUEEN = 'Q'
EMPTY = '.'
SIZE = 8


class ChessBoard:
    def __init__(self) -> None:
        self.board = None
        self.size = SIZE
        self.king = (None, None)

    def read_board(self):
        self.board = [input().split() for _ in range(SIZE)]

    @property
    def king_position(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == KING:
                    return (i, j)

    def within_bounds(self, i, j):
        return 0 <= i < self.size and 0 <= j < self.size

    def get_attackers(self):
        attack_deltas = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]

        if not all(self.king):
            self.king = self.king_position

        attackers = []
        for delta in attack_deltas:
            i, j = self.king
            delta_i, delta_j = delta

            while True:
                if not self.within_bounds(i, j):
                    break
                
                if self.board[i][j] == QUEEN:
                    attackers.append((i, j))
                    break

                i += delta_i
                j += delta_j

        return attackers

    def __repr__(self) -> str:
        res = []
        attackers = self.get_attackers()
        if attackers:
            for a in attackers:
                res.append(f'[{a[0]}, {a[1]}]')
        else:
            res.append('The king is safe!')

        return '\n'.join(res)


def main():
    board = ChessBoard()
    board.read_board()
    print(board)


main()
