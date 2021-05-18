def read_matrix():
    n, m = map(int, input().split())
    return [[int(x) for x in input().split()] for _ in range(n)]


def get_squares(matrix, n):
    sums_squres_map = {}
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    for i in range(rows_count-n+1):
        for j in range(cols_count-n+1):
            square = [matrix[row][j:j+n] for row in range(i, i+n)]
            square_sum = get_matrix_sum(square)
            sums_squres_map[square_sum] = square
    return sums_squres_map


def get_matrix_sum(matrix):
    return sum(sum(matrix[i]) for i in range(len(matrix)))


def get_max_sum_and_square(sums_squres_map):
    for sum, square in sorted(sums_squres_map.items(), key=lambda x: -x[0]):
        return sum, square


def fmt_output(max_sum, max_square):
    nl = '\n'
    result = []
    result.append(f'Sum = {max_sum}')
    for row in max_square:
        result.append(' '.join([str(x) for x in row]))
    return nl.join(result)


def main() -> None:
    N = 3
    matrix = read_matrix()
    sums_squares_map = get_squares(matrix, N)
    max_sum, max_square = get_max_sum_and_square(sums_squares_map)
    print(fmt_output(max_sum, max_square))


main()
