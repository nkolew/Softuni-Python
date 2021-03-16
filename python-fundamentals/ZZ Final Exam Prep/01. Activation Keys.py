def contains(s: str, key: str) -> str:
    """Checks if given substring (s) is in the key provided.

    Args:
        s (str): Substring to be checked
        key (str): Key to be checked

    Returns:
        str: Formated string.
    """
    if s in key:
        return f'{key} contains {s}'
    return f'Substring not found'


def flip(upper, lower, start_idx, end_idx, key:str)

key = input()
while True:
    data = input()
    if data == 'Generate':
        break
    command, *tokens = data.split('>>>')
    if command == 'Contains':
        contains(*tokens, key)
    if command == 'Flip':
        upper, lower, start_idx, end_idx = tokens

