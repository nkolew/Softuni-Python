def jump(l: list, v: int, idx: list):
    if not idx:
        i = 0
    else:
        i = idx[-1]

    i += v
    if i >= len(l):
        i = 0
    idx.append(i)
    if l[i] == 0:
        print(f"Place {i} already had Valentine's day.")
    else:
        l[i] -= 2
        if l[i] <= 0:
            l[i] = 0
            print(f"Place {i} has Valentine's day.")

    return (l, idx)


hood = list(map(int, input().split('@')))
indexes = []

command_data = input()
while command_data != 'Love!':
    command, value = command_data.split()
    value = int(value)
    if command == 'Jump':
        hood, indexes = jump(hood, value, indexes)
    command_data = input()


if not any(hood):
    print(f"Cupid's last position was {indexes[-1]}.")
    print("Mission was successful.")

else:
    print(f"Cupid's last position was {indexes[-1]}.")
    print(f'Cupid has failed {len([h for h in hood if h!=0])} places.')
