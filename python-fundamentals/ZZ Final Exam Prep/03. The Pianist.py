from typing import List


class Piece:
    def __init__(self, name: str, composer: str, key: str) -> None:
        self.name = name
        self.composer = composer
        self.key = key

    def change_key(self, new_key: str) -> None:
        self.key = new_key

    def __str__(self) -> str:
        return f'{self.name} by {self.composer} in {self.key}'


class Collection:
    def __init__(self) -> None:
        self.pieces: List[Piece] = []

    def __piece_exists(self, name: str) -> 'tuple[bool,int]':
        for index, piece in enumerate(self.pieces):
            if piece.name == name:
                return True, index
        return False, 0

    def add(self, name: str, composer: str, key: str) -> str:
        piece_exists, index = self.__piece_exists(name)
        if piece_exists:
            return f'{name} is already in the collection!'
        self.pieces.append(Piece(name, composer, key))
        return f'{name} by {composer} in {key} added to the collection!'

    def remove(self, name: str) -> str:
        piece_exists, index = self.__piece_exists(name)
        if piece_exists:
            self.pieces.pop(index)
            return f'Successfully removed {name}!'
        return f'Invalid operation! {name} does not exist in the collection.'

    def change_key(self, name: str, new_key: str) -> str:
        piece_exists, index = self.__piece_exists(name)
        if piece_exists:
            self.pieces[index].change_key(new_key)
            return f'Changed the key of {name} to {new_key}!'
        return f'Invalid operation! {name} does not exist in the collection.'

    def __repr__(self) -> str:
        result = []
        nl = '\n'
        for piece in sorted(self.pieces, key=lambda x: (x.name, x.composer)):
            result.append(
                f'{piece.name} -> Composer: {piece.composer}, Key: {piece.key}')
        return nl.join(result)


col = Collection()
n = int(input())

for _ in range(n):
    name, composer, key = input().split('|')
    col.add(name, composer, key)

while True:
    data = input()
    if data == 'Stop':
        break
    command, *tokens = data.split('|')
    if command == 'Add':
        name, composer, key = tokens
        print(col.add(name, composer, key))
    elif command == 'Remove':
        name = ''.join(tokens)
        print(col.remove(name))
    elif command == 'ChangeKey':
        name, new_key = tokens
        print(col.change_key(name, new_key))

print(col)
