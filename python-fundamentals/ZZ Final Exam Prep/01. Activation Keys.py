def contains(key: str, s: str) -> str:
    """Checks if given substring (s) is in the key provided.

    Args:
        s (str): Substring to be checked
        key (str): Key to be checked

    Returns:
        str: Formated string.
    """
    if s in key:
        return f'{key} contains {s}'
    return f'Substring not found!'


def flip(key: str, func: str, start_idx: int, end_idx: int) -> str:
    """Changes the substring between the given indices (the end index is exclusive) to upper or lower case. 

    Args:
        key (str): The key to be changed
        func (str): Method to be used: upper or lower
        start_idx (int): Starting index
        end_idx (int): End index

    Returns:
        key (str): Changed key
    """
    def method(c: str, func: str) -> str:
        """Converts char to upper or lower

        Args:
            s (str): character
            func (str): Upper / Lower

        Returns:
            str: Converted character
        """
        if func == 'Upper':
            return c.upper()
        return c.lower()

    for i in range(start_idx, end_idx):
        key = key[:i] + method(key[i], func) + key[i+1:]
    return key


def slice(key: str, start_idx: int, end_idx: int) -> str:
    """Deletes the characters between the start and end indices (end index is exclusive).

    Args:
        key (str): The key to be changed
        start_idx (int): Starting index
        end_idx (int): Ending index

    Returns:
        key (str): Changed key
    """
    return key[:start_idx] + key[end_idx:]


key = input()

while True:
    data = input()
    if data == 'Generate':
        break
    command, *tokens = data.split('>>>')
    if command == 'Contains':
        substring = ''.join(tokens)
        print(contains(key, substring))
    if command == 'Flip':
        method, start_idx, end_idx = tokens
        start_idx = int(start_idx)
        end_idx = int(end_idx)
        key = flip(key, method, start_idx, end_idx)
        print(key)
    if command == 'Slice':
        start_idx, end_idx = tokens
        start_idx = int(start_idx)
        end_idx = int(end_idx)
        key = slice(key, start_idx, end_idx)
        print(key)

print(f'Your activation key is: {key}')
