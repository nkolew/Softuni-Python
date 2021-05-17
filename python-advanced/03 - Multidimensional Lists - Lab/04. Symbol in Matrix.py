from typing import List, Optional, Tuple


def gen_matrix(n: int) -> List[List[str]]:
    matrix = []
    for _ in range(n):
        row = list(input())
        matrix.append(row)
    return matrix


def get_location_in_matrix(matrix: List[List[str]], search_term: str) -> Optional[Tuple[int, int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == search_term:
                return i, j


def main() -> None:
    n = int(input())
    matrix = gen_matrix(n)
    search_term = input()
    location = get_location_in_matrix(matrix, search_term)
    if location:
        print(location)
    else:
        print(f'{search_term} does not occur in the matrix')


main()
