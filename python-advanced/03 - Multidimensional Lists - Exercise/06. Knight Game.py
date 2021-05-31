from collections import defaultdict
from typing import DefaultDict


def read_arr():
    return [list(input()) for _ in range(int(input()))]


def get_knights(arr):
    n = len(arr)
    return [(i, j) for i in range(n)
            for j in range(n) if arr[i][j] == 'K']


def valid_positions(arr, x, y):
    n = len(arr)
    return 0 <= x < n and 0 <= y < n


def get_knights_histo(arr) -> DefaultDict:
    TARGET_DELTAS = [
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
    ]

    knights_histo = defaultdict(int)
    for i in range(len(get_knights(arr))):
        x, y = get_knights(arr)[i][0], get_knights(arr)[i][1]
        for j in range(len(TARGET_DELTAS)):
            delta_x, delta_y = TARGET_DELTAS[j][0], TARGET_DELTAS[j][1]
            pos_x, pos_y = x + delta_x, y + delta_y
            if valid_positions(arr, pos_x, pos_y):
                if arr[pos_x][pos_y] == 'K':
                    knights_histo[(x, y)] += 1
    return knights_histo


def remove_knight(arr, coord: tuple):
    x, y = coord
    arr[x][y] = 0
    return arr


def iterate_over_knights(arr):
    removed_knights = 0
    while True:
        knigthts_histo = get_knights_histo(arr)
        if not knigthts_histo:
            return removed_knights
        knights = [k for k, _ in sorted(
            knigthts_histo.items(),
            key=lambda x: -x[1])]
        best_knight = knights[0]
        arr = remove_knight(arr, best_knight)
        removed_knights += 1


def main():
    arr = read_arr()
    removed_knights = iterate_over_knights(arr)
    print(removed_knights)


main()
