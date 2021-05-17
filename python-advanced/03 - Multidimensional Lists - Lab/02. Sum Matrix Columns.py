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


def get_matrix_columns_sum(matrix: List[List[int]]) -> List[int]:
    col_sums = [0]*len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            col_sums[col] += matrix[row][col]
    return col_sums


def fmt_output(l: List[int]) -> str:
    return '\n'.join(map(str, l))


def main() -> None:
    n, m = get_matrix_size(sep=', ')
    matrix = gen_matrix(n, m)
    columns_sum = get_matrix_columns_sum(matrix)
    print(fmt_output(columns_sum))


main()
