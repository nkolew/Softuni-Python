from collections import defaultdict

THRESHOLD = 250

map = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}

key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = defaultdict(int)

while True:
    item_is_ready = False
    tokens = input().split(' ')
    for i in range(0, len(tokens), 2):
        material = tokens[i+1].lower()
        quantity = int(tokens[i])
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= THRESHOLD:
                print(f'{map[material]} obtained!')
                key_materials[material] -= THRESHOLD
                item_is_ready = True
                break
        else:
            junk_items[material] += quantity
    if item_is_ready:
        break


for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f'{material}: {quantity}')

for material, quantity in sorted(junk_items.items(), key=lambda x: x[0]):
    print(f'{material}: {quantity}')
