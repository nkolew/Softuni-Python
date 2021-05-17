from typing import List, Optional


def get_matrix_size(sep: str = ' ') -> List[int]:
    return [int(x) for x in input().split(sep)]


def gen_matrix(n: int, m: int, sep: str = ' ') -> List[List[int]]:
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(sep)]
        assert m == len(row), f'Expected {m}, got {len(row)} values'
        matrix.append(row)
    return matrix


def get_matrix_sum(matrix: List[List[int]]) -> int:
    return sum([
        sum(matrix[i])
        for i in range(len(matrix))
    ])


def gen_squares(matrix: List[List[int]]) -> List[List[List[int]]]:
    squares = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            squares.append([
                [matrix[i][j], matrix[i][j+1]],
                [matrix[i+1][j], matrix[i+1][j+1]],
            ])
    return squares


def get_max_square(squares: List[List[List[int]]]) -> Optional[List[List[int]]]:
    for square in squares:
        if get_matrix_sum(square) == max([get_matrix_sum(x) for x in squares]):
            return square


def main() -> None:
    n, m = get_matrix_size(sep=', ')
    matrix = gen_matrix(n, m, sep=', ')
    squares = gen_squares(matrix)
    max_square = get_max_square(squares)
    if max_square:
        print('\n'.join([' '.join(map(str, row)) for row in max_square]))
        print(get_matrix_sum(max_square))


main()
