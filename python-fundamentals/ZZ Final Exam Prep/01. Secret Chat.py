def insert_space(s: str, i: int) -> str:
    s = s[:i] + ' ' + s[i:]
    print(s)
    return s


def reverse(s: str, substring: str) -> str:
    if substring in s:
        reversed_substring = substring[::-1]
        s = s.replace(substring, '', 1)
        s += reversed_substring
    else:
        print('error')
        return s
    print(s)
    return s


def change_all(s: str, old: str, new: str) -> str:
    if old in s:
        while old in s:
            s = s.replace(old, new)
    print(s)
    return s


message = input()

while True:
    data = input()
    if data == 'Reveal':
        break
    command, *tokens = data.split(':|:')
    if command == 'InsertSpace':
        index = int(''.join(tokens))
        message = insert_space(message, index)
    if command == 'Reverse':
        substring = ''.join(tokens)
        message = reverse(message, substring)
    if command == 'ChangeAll':
        substring, replacement = tokens
        message = change_all(message, substring, replacement)

print(f'You have a new text message: {message}')
