def change(s: str, char: str, repl: str) -> str:
    return s.replace(char, repl)


def includes(s: str, string: str) -> bool:
    return string in s


def end(s: str, string: str) -> bool:
    return s.endswith(string)


def uppercase(s: str) -> str:
    return s.upper()


def find_index(s: str, char: str) -> int:
    return s.index(char)


def cut(s: str, start_index: int, length: int) -> str:
    return s[start_index:start_index+length]


s = input()

while True:
    data = input().strip()
    if data == 'Done':
        break
    command, *tokens = data.split()
    if command == 'Change':
        char, repl = tokens
        s = change(s, char, repl)
        print(s)
    elif command == 'Includes':
        print(includes(s, *tokens))
    elif command == 'End':
        print(end(s, *tokens))
    elif command == 'Uppercase':
        s = uppercase(s)
        print(s)
    elif command == 'FindIndex':
        print(find_index(s, *tokens))
    elif command == 'Cut':
        start_index, length = tokens
        start_index = int(start_index)
        length = int(length)
        s = cut(s, start_index, length)
        print(s)
