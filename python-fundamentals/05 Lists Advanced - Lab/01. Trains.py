def add_people(l: list, n: int):
    l[-1] += n

    return l


def insert_people(l: list, i: int, n: int):
    l[i] += n

    return l


def remove_people(l: list, i: int, n: int):
    l[i] -= n

    return l


wagons_count = int(input())
train = [0] * wagons_count

command_data = input()

while command_data != 'End':

    if 'add' in command_data:
        command, num = command_data.split()
        num = int(num)
        train = add_people(train, num)

    elif 'insert' in command_data:
        command, idx, num = command_data.split()
        idx = int(idx)
        num = int(num)
        train = insert_people(train, idx, num)

    elif 'leave' in command_data:
        command, idx, num = command_data.split()
        idx = int(idx)
        num = int(num)
        train = remove_people(train, idx, num)

    command_data = input()

print(train)
