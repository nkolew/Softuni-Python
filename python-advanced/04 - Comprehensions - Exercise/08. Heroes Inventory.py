names = input().split(', ')
inventory = {name: {} for name in names}

for line in iter(input, 'End'):
    name, item, cost = line.split('-')
    if item not in inventory[name]:
        inventory[name][item] = int(cost)

print('\n'.join(
    (f'{name} -> Items: {len(data)}, Cost: {sum(data.values())}' for name,
     data in inventory.items())
))
