from typing import List


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


def main() -> None:
    n, m = get_matrix_size(sep=', ')
    matrix = gen_matrix(n, m, sep=', ')
    matrix_sum = get_matrix_sum(matrix)
    print(matrix_sum)
    print(matrix)


main()
