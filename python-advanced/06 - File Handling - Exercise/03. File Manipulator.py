import os

file_path = os.path.dirname(os.path.abspath(__file__))

for line in iter(input, 'End'):
    cmd, *tokens = line.split('-')
    if cmd == 'Create':
        filename = f'{file_path}/{tokens[0]}'
        with open(filename, 'w') as fh:
            pass
    elif cmd == 'Аdd':
        filename = f'{file_path}/{tokens[0]}'
        line = tokens[1]
        with open(filename, 'a') as fh:
            fh.write(line+'\n')
    elif cmd == 'Replace':
        name, old, new = tokens
        filename = f'{file_path}/{name}'
        try:
            with open(filename, 'r+') as fh:
                content = fh.read()
                content = content.replace(old, new)
                fh.write(content)
        except FileNotFoundError:
            print('An error occured')
            continue
    if cmd == 'Delete':
        try:
            filename = f'{file_path}/{tokens[0]}'
            os.remove(filename)
        except FileNotFoundError as e:
            print('An error occured')
