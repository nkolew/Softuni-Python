def decrypt(text: str, key: list) -> str:
    """Decrypt the text, according to the instructions

    Args:
        text (str): Text to be decrypted
        key (list): Key to be used for decryption

    Returns:
        str: Decrypted text
    """
    decrypted_text = ''
    i = 0
    k = 0
    while i < len(text):
        if k == len(key):
            k = 0
        char = chr(ord(text[i])-key[k])
        decrypted_text += char
        i += 1
        k += 1
    return decrypted_text


def get_treasure_and_coord(text: str) -> 'tuple[str]':
    """Get the treasure and the coordinates in text.

    Args:
        text (str): Decrypted text to be searched.

    Returns:
        tuple: Treasure and Coordinates as strings
    """
    treasure = ''
    coord = ''
    count = 0
    i = 0
    while i < len(text):
        if text[i] == '&':
            count += 1
            i += 1
            treasure += text[i]
            while i+1 < len(text):
                i += 1
                if text[i] == '&' and count > 0:
                    break
                treasure += text[i]
        if text[i] == '<':
            i += 1
            coord += text[i]
            while i+1 < len(text):
                i += 1
                if text[i] == '>':
                    break
                coord += text[i]
        i += 1
    return (treasure, coord)


key = list(map(int, input().split()))

while True:
    data = input()
    if data == 'find':
        break
    decrypted = decrypt(data, key)
    treasure, coord = get_treasure_and_coord(decrypted)
    print(f'Found {treasure} at {coord}')
