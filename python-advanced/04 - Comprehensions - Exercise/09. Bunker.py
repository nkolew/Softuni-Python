categories = input().split(', ')
n = int(input())
bunker = {cat: [] for cat in categories}

for _ in range(n):
    cmd = input()
    cat, item, rawdata = cmd.split(' - ')
    qtty, qlty = rawdata.split(';')
    qtty, qlty = int(qtty.split(':')[1]), int(qlty.split(':')[1])
    bunker[cat].append({'name': item, 'qtty': qtty, 'qlty': qlty})

items_count = sum(item['qtty']
                  for items in bunker.values()
                  for item in items)

avg_qlty = sum(item['qlty']
               for items in bunker.values()
               for item in items) / len(categories)


print(f'Count of items: {items_count}')
print(f'Average quality: {avg_qlty:.2f}')
print('\n'.join(
    f'{category} -> {", ".join(item["name"] for item in bunker[category])}'
    for category in categories))
