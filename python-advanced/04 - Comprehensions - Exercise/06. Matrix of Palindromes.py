def read_input():

    return [int(x) for x in input().split()]


def gen_element(i, j):
    OFFSET = ord('a')

    return f'{chr(i+OFFSET)}{chr(i+j+OFFSET)}{chr(i+OFFSET)}'


def gen_matrix(n, m):

    return ((gen_element(i, j)
             for j in range(m))
            for i in range(n)
            )


def fmt_matrix(matrix):

    return '\n'.join(
        ' '.join(i)
        for i in matrix
    )


n, m = read_input()
matrix = gen_matrix(n, m)
print(fmt_matrix(matrix))
