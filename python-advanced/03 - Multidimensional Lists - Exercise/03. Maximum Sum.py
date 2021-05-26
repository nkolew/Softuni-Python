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
            sums_squres_map[(i, j)] = square_sum
    return sums_squres_map


def get_matrix_sum(matrix):
    return sum(sum(matrix[i]) for i in range(len(matrix)))


def get_top_point_and_sum_of_max_square(sums_squres_map):
    for top_point, square_sum in sorted(sums_squres_map.items(), key=lambda x: -x[1]):
        return top_point, square_sum


def fmt_output(matrix, n, max_sum, max_square_top_point):
    nl = '\n'
    result = []
    i, j = max_square_top_point
    result.append(f'Sum = {max_sum}')
    for row in range(i, i+n):
        result.append(' '.join([str(x) for x in matrix[row][j:j+n]]))
    return nl.join(result)


def main() -> None:
    N = 3
    matrix = read_matrix()
    sums_squares_map = get_squares(matrix, N)
    max_square_top_point, max_sum = get_top_point_and_sum_of_max_square(sums_squares_map)
    print(fmt_output(matrix, N, max_sum, max_square_top_point))


main()
