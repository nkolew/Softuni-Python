def add(l: list, v: int) -> list:
    l.append(v)
    return l


def remove(l: list, v: int) -> list:
    for i in range(len(l)):
        if l[i] == v:
            l.pop(i)
            break
    return l


def replace(l: list, v: int, r: int) -> list:
    for i in range(len(l)):
        if l[i] == v:
            l.pop(i)
            l.insert(i, r)
            break
    return l


def collapse(l: list, v: int) -> list:
    for i in range(len(l)-1, -1, -1):
        if l[i] < v:
            l.pop(i)
    return l


def repr_l(l: list) -> str:
    return ' '.join(map(str, l))


sugar_cubes = list(map(int, input().split()))

while True:
    data = input()
    if data == 'Mort':
        print(repr_l(sugar_cubes))
        break
    command, *token = data.split()
    if command == 'Add':
        value = int(*token)
        sugar_cubes = add(sugar_cubes, value)
    elif command == 'Remove':
        value = int(*token)
        sugar_cubes = remove(sugar_cubes, value)
    elif command == 'Replace':
        value, replacement = int(token[0]), int(token[1])
        sugar_cubes = replace(sugar_cubes, value, replacement)
    elif command == 'Collapse':
        value = int(*token)
        sugar_cubes = collapse(sugar_cubes, value)
