def extract_person(line: str) -> 'tuple[str]':
    '''Get person name and age in text

    Args:
        line (str): Line of text to be searched

    Returns:
        tuple: Name and age of the person in string format
    '''
    name = ''
    age = ''
    i = 0
    while i < len(line):
        if line[i] == '@':
            i += 1
            name += line[i]
            while i+1 < len(line):
                i += 1
                if line[i] == '|':
                    break
                name += line[i]
        if line[i] == '#':
            i += 1
            age += line[i]
            while i+1 < len(line):
                i += 1
                if line[i] == '*':
                    break
                age += line[i]
        i += 1
    return (name, age)


n = int(input())

for _ in range(n):
    data = input()
    name, age = extract_person(data)
    print(f'{name} is {age} years old.')
