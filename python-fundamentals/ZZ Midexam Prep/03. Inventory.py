items = input().split(', ')

while True:
    tokens = input()
    if tokens == 'Craft!':
        break

    command, item = tokens.split(' - ')
    if command == 'Collect':
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        if item in items:
            items.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in items:
            for i, v in enumerate(items):
                if v == old_item:
                    items.insert(i+1, new_item)
    elif command == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)

print(f'{", ".join(items)}')
