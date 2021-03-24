def add(d: dict, piece: str, composer: str, key: str) -> dict:
    if piece not in d:
        d[piece] = {'composer': composer, 'key': key}
        print(f'{piece} by {composer} in {key} added to the collection!')
    else:
        print(f'{piece} is already in the collection!')
    return d


def remove(d: dict, piece: str) -> dict:
    if piece not in d:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    else:
        d.pop(piece)
        print(f'Successfully removed {piece}!')
    return d


def change_key(d: dict, piece: str, new_key: str) -> dict:
    if piece not in d:
        print(f'Invalid operation! {piece} does not exist in the collection.')
    else:
        d[piece]['key'] = new_key
        print(f'Changed the key of {piece} to {new_key}!')
    return d


pieces = {}

n = int(input())
for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = {'composer': composer, 'key': key}

while True:
    data = input()
    if data == 'Stop':
        break
    if data.startswith('Add'):
        command, piece, composer, key = data.split('|')
        pieces = add(pieces, piece, composer, key)
    elif data.startswith('Remove'):
        command, piece = data.split('|')
        pieces = remove(pieces, piece)
    elif data.startswith('ChangeKey'):
        command, piece, new_key = data.split('|')
        pieces = change_key(pieces, piece, new_key)

for piece, stats in sorted(pieces.items(), key=lambda x: (x[0], x[1]['composer'])):
    print(f'{piece} -> Composer: {stats["composer"]}, Key: {stats["key"]}')
