def read_matrix(n):
    return [[int(x) for x in input().split()] for _ in range(n)]


def index_valid(matrix, x, y):
    n = len(matrix)
    return 0 <= x < n and 0 <= y < n


def add(matrix, x, y, val):
    matrix[x][y] += int(val)
    return matrix


def subtract(matrix, x, y, val):
    matrix[x][y] -= int(val)
    return matrix


def parse_cmd(cmd, matrix, x, y, val):
    ops = {
        'Add': add,
        'Subtract': subtract
    }
    if index_valid(matrix, x, y):
        matrix = ops[cmd](matrix, x, y, val)
    else:
        print('Invalid coordinates')
    return matrix


def mod_matrix(matrix):
    for line in iter(input, 'END'):
        cmd, x, y, val = line.split()
        x, y, val = int(x), int(y), int(val)
        matrix = parse_cmd(cmd, matrix, x, y, val)
    return matrix


def fmt_output(matrix):
    return '\n'.join(" ".join(str(el) for el in row) for row in matrix)


def main():
    n = int(input())
    matrix = read_matrix(n)
    matrix = mod_matrix(matrix)
    print(fmt_output(matrix))


main()
