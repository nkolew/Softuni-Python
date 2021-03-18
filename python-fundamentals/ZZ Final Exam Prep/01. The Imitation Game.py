def move(s: str, count: int) -> str:
    return s[count:] + s[:count]


def insert(s: str, i: int, v: str) -> str:
    if 0 <= i <= len(s):
        return s[:i] + v + s[i:]
    return s


def change_all(s: str, old: str, new: str) -> str:
    if old in s:
        while old in s:
            s = s.replace(old, new)
    return s


message = input()

while True:
    data = input()
    if data == 'Decode':
        break
    command, *tokens = data.split('|')
    if command == 'Move':
        count = int(''.join(tokens))
        message = move(message, count)
    elif command == 'Insert':
        index, value = tokens
        index = int(index)
        message = insert(message, index, value)
    elif command == 'ChangeAll':
        old, new = tokens
        message = change_all(message, old, new)

print(f'The decrypted message is: {message}')
