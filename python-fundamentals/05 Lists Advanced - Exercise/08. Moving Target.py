def index_exists(l: list, i: int, v: int = 0):
    if 0 <= i - v and i + v < len(l):
        return True

    return False


def shoot(l: list, i: int, v: int):
    if index_exists(l, i):
        l[i] -= v
        if l[i] <= 0:
            l.pop(i)

    return l


def add(l: list, i: int, v: int):
    if index_exists(l, i):
        l.insert(i, v)
    else:
        print('Invalid placement!')

    return l


def strike(l: list, i: int, v: int):
    if index_exists(l, i, v):
        l = l[:i-v] + l[i+v+1:]
    else:
        print('Strike missed!')

    return l


targets = list(map(int, input().split()))

command_data = input()

while command_data != 'End':
    command, index, value = command_data.split()
    index = int(index)
    value = int(value)

    if command == 'Shoot':
        targets = shoot(targets, index, value)

    elif command == 'Add':
        targets = add(targets, index, value)

    elif command == 'Strike':
        targets = strike(targets, index, value)

    command_data = input()


print('|'.join(map(str, targets)))
