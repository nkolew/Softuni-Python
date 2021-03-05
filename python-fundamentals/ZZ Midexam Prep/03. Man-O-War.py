pirateship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
pirateship_sunk = False
warship_sunk = False


def index_exists(l: list, i: int):
    if 0 <= i < len(l):
        return True
    return False


def fire(l: list, i: int, v: int):
    warship_sunk = False
    if index_exists(l, i):
        l[i] -= v
        if l[i] <= 0:
            warship_sunk = True
    return l, warship_sunk


def defend(l: list, i_s: int, i_e: int, v: int):
    pirateship_sunk = False
    if index_exists(l, i_s) and index_exists(l, i_e):
        for i in range(i_s, i_e+1):
            l[i] -= v
            if l[i] <= 0:
                pirateship_sunk = True
                break
    return l, pirateship_sunk


def repair(l: list, i: int, v: int):
    if index_exists(l, i):
        l[i] += v
        if l[i] > max_health:
            l[i] = max_health
    return l


def status(l: list):
    threshold = 0.2 * max_health
    need_repair = len([e for e in l if e < threshold])
    return f'{need_repair} sections need repair.'


while True:
    data = input()
    if data == 'Retire':
        break
    command, *tokens = data.split()
    if command == 'Fire':
        index, damage = int(tokens[0]), int(tokens[1])
        warship, warship_sunk = fire(warship, index, damage)
        if warship_sunk:
            print('You won! The enemy ship has sunken.')
            break
    elif command == 'Defend':
        index_s, index_e, damage = int(
            tokens[0]), int(tokens[1]), int(tokens[2])
        pirateship, pirateship_sunk = defend(
            pirateship, index_s, index_e, damage)
        if pirateship_sunk:
            print('You lost! The pirate ship has sunken.')
            break
    elif command == 'Repair':
        index, health = int(tokens[0]), int(tokens[1])
        pirateship = repair(pirateship, index, health)
    elif command == 'Status':
        print(status(pirateship))


if not pirateship_sunk and not warship_sunk:
    print(f'Pirate ship status: {sum(pirateship)}')
    print(f'Warship status: {sum(warship)}')
