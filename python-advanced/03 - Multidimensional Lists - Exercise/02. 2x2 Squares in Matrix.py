def read_matrix(sep):
    n, m = map(int, input().split(sep))
    return [input().split(sep) for _ in range(n)]


def get_2x2_squares_count(matrix):
    squares_count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n - 1):
        for j in range(m - 1):
            if matrix[i][j] == matrix[i][j+1] == \
                    matrix[i+1][j] == matrix[i+1][j+1]:
                squares_count += 1
    return squares_count


def main() -> None:
    matrix = read_matrix(' ')
    print(get_2x2_squares_count(matrix))


main()
