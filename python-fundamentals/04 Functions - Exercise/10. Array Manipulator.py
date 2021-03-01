def exchange(data: list, idx: int):

    if 0 <= idx < len(data):
        return data[idx+1:] + data[:idx+1]

    print('Invalid index')
    return data


def get_fdata(typ: str, data: list):

    fdata = []

    if typ == 'odd':
        fdata = list(filter(lambda x: x % 2 == 1, data))

    elif typ == 'even':
        fdata = list(filter(lambda x: x % 2 == 0, data))

    return fdata


def max_min(com: str, typ: str, data: list):

    fdata = get_fdata(typ, data)

    if len(fdata) == 0:
        return 'No matches'

    if com == 'max':
        for idx in range(len(data)-1, -1, -1):
            if data[idx] == max(fdata):
                return idx

    elif com == 'min':
        for idx in range(len(data)-1, -1, -1):
            if data[idx] == min(fdata):
                return idx


def first_last(comm: str, cnt: int, typ: str, data: list):

    fdata = get_fdata(typ, data)

    if cnt > len(data):
        return 'Invalid count'

    if len(fdata) == 0:
        return []

    if cnt > len(fdata):
        cnt = len(fdata)

    if comm == 'first':

        return fdata[:cnt]

    elif comm == 'last':
        fdata_rev = fdata[::-1]

        return list(reversed(fdata_rev[:cnt]))


data = list(map(int, input().split()))
command = input()

while command != 'end':

    if 'exchange' in command:
        command, idx = command.split()
        idx = int(idx)
        data = exchange(data, idx)

    elif 'max' in command or 'min' in command:
        command, num_type = command.split()
        print(max_min(command, num_type, data))

    elif 'first' in command or 'last' in command:
        command, count, num_type = command.split()
        count = int(count)
        print(first_last(command, count, num_type, data))

    command = input()

print(data)
