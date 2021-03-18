def valid_index(s: str, i: int) -> bool:
    """Checks if index is valid

    Args:
        s (str): String to check
        i (int): Index to check

    Returns:
        bool: True|False
    """
    return 0 <= i < len(s)


def add_stop(s: str, stop: str, i: int) -> str:
    """Insert the given string at that index only if the index is valid

    Args:
        s (str): String to change
        substring (str): substring to insert
        i (int): Index at which to insert

    Returns:
        str: Changed string
    """
    if valid_index(s, i):
        return s[:i]+stop+s[i:]
    return s


def remove_stop(s: str, start_i: int, end_i: int) -> str:
    """Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid

    Args:
        s (str): String to change
        start_i (int): Start index
        end_i (int): End index

    Returns:
        str: Changed string
    """
    if valid_index(s, start_i) and valid_index(s, end_i):
        return s[:start_i]+s[end_i+1:]
    return s


def switch(s: str, old: str, new: str) -> str:
    """If the old string is in the initial string, replace it with the new one. (all occurrences)

    Args:
        s (str): String to change
        old (str): Old substring
        new (str): New substring

    Returns:
        str: Changed string
    """
    if old in s:
        while old in s:
            s = s.replace(old, new)
    return s


stops = input()

while True:
    data = input()
    if data == 'Travel':
        break
    command, *tokens = data.split(':')
    if command == 'Add Stop':
        index, stop = tokens
        index = int(index)
        stops = add_stop(stops, stop, index)
        print(stops)
    elif command == 'Remove Stop':
        start_i, end_i = tokens
        start_i = int(start_i)
        end_i = int(end_i)
        stops = remove_stop(stops, start_i, end_i)
        print(stops)
    elif command == 'Switch':
        old, new = tokens
        stops = switch(stops, old, new)
        print(stops)

print(f'Ready for world tour! Planned stops: {stops}')
