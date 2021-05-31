def val_coord(x: int, y: int, n: int, m: int) -> bool:
    return 0 <= x < n and 0 <= y < m


def read_arr():
    n, m = [int(x) for x in input().split()]
    arr = [input().split() for _ in range(n)]
    return arr


def print_arr(arr):
    for line in arr:
        print(*line)


def main():
    arr = read_arr()
    n = len(arr)
    m = len(arr[0])
    while True:
        cmd = input()
        if cmd == 'END':
            break
        tokens = cmd.split()
        if tokens[0] != 'swap' or len(tokens) != 5:
            print('Invalid input!')
            continue
        row1, col1, row2, col2 = [
            int(x) for x in
            (tokens[1], tokens[2], tokens[3], tokens[4])
        ]
        if val_coord(row1, col1, n, m) and \
                val_coord(row2, col2, n, m):
            arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]
            print_arr(arr)
        else:
            print('Invalid input!')


main()
