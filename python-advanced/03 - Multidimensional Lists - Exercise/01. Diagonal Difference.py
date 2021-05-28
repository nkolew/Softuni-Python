# n = int(input())
# arr = [[int(x) for x in input().split()] for _ in range(n)]

# pri_diag_sum = 0
# sec_diag_sum = 0
# for i in range(n):
#     pri_diag_sum += arr[i][i]
#     sec_diag_sum += arr[i][n-i-1]

# print(abs(pri_diag_sum - sec_diag_sum))



from typing import Callable, List


def read_matrix(n: int):
    return [[int(i) for i in input().split()] for _ in range(n)]


def calc_diag_sum_in_matrix(matrix: List[List[int]], col_func: Callable[[int, int], int]):
    n = len(matrix)
    result = 0
    for x in range(n):
        y = col_func(x, n)
        result += matrix[x][y]
    return result


def calc_pri_diag_sum(matrix: List[List[int]]):
    return calc_diag_sum_in_matrix(matrix, lambda x, n: x)


def calc_sec_diag_sum(matrix: List[List[int]]):
    return calc_diag_sum_in_matrix(matrix, lambda x, n: n - x - 1)


def main() -> None:
    n = int(input())
    matrix = read_matrix(n)
    pri_sum = calc_pri_diag_sum(matrix)
    sec_sum = calc_sec_diag_sum(matrix)
    print(abs(pri_sum - sec_sum))


main()
