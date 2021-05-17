from typing import List


def gen_matrix(n: int, sep: str = ' ') -> List[List[int]]:
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(sep)]
        matrix.append(row)
    return matrix


def get_primary_diagonal_sum(matrix: List[List[int]]) -> int:
    return sum([matrix[i][i] for i in range(len(matrix))])


def main() -> None:
    n = int(input())
    matrix = gen_matrix(n)
    result = get_primary_diagonal_sum(matrix)
    print(result)


main()
