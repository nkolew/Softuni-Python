N = 7
STARTING_SCORE = 501


def get_dartboard():
    return [input().split() for _ in range(N)]


def get_hit():
    return [int(x) for x in input()[1:-1].split(', ')]


def inside_bounds(x, y):
    return 0 <= x < N and 0 <= y < N


def get_score(dartboard, x, y):
    scores = {
        'D': lambda point_sum: 2 * point_sum,
        'T': lambda point_sum: 3 * point_sum,
        'B': lambda point_sum: STARTING_SCORE
    }
    if not inside_bounds(x, y):
        return 0

    hit = dartboard[x][y]
    if hit.isnumeric():
        return int(hit)
    else:
        points_sum = sum((int(dartboard[x][0]), int(dartboard[0][y]),
                          int(dartboard[x][N-1]), int(dartboard[N-1][y])))
        return scores[hit](points_sum)


def main():
    player1, player2 = input().split(', ')
    player1_score, player2_score = STARTING_SCORE, STARTING_SCORE
    dartboard = get_dartboard()

    winner = None
    hit_count = None
    player1_hit_count = 0
    player2_hit_count = 0

    i = 0
    while True:
        hit = get_hit()
        x, y = hit
        current_score = get_score(
            dartboard, x, y)
        i += 1
        if i % 2 != 0:
            player1_hit_count += 1
            player1_score -= current_score
            if player1_score <= 0:
                winner = player1
                hit_count = player1_hit_count
                break
        else:
            player2_hit_count += 1
            player2_score -= current_score
            if player2_score <= 0:
                winner = player2
                hit_count = player2_hit_count
                break

    print(f'{winner} won the game with {hit_count} throws!')


main()
