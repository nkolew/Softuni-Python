import re
from collections import defaultdict


planets = defaultdict(list)


def decrypt_message(message: str) -> str:
    """Decrypt message

    Args:
        message (str): Message to be decrypted

    Returns:
        message (str): Decrypted message
    """
    let_pattern = r'(?i)[s,t,a,r]'
    letters = re.findall(let_pattern, message)
    factor = len(letters)
    for i, c in enumerate(message):
        message = message[:i]+chr(ord(c)-factor)+message[i+1:]
    return message


def get_message_info(message: str, planets: dict) -> dict:
    """Add planets to the dictionary

    Args:
        message (str): Decrypted message
        planets (dict): Planets dict

    Returns:
        planets (dict): Updated Planets dict
    """
    pattern = r'(?:(?<=\@)(?P<name>[A-Za-z]+).*(?<=\:)(?P<population>\d+).*(?<=\!)(?P<attack>[AD])(?=\!).*(?<=\-\>)(?P<soldiers>[\d]+))'
    m = re.search(pattern, message)

    if m:
        if m.group('attack') == 'A':
            planets['Attacked'].append(m.group('name'))
        if m.group('attack') == 'D':
            planets['Destroyed'].append(m.group('name'))
    return planets


n = int(input())

for _ in range(n):
    message = input()
    decrypted = decrypt_message(message)
    planets = get_message_info(decrypted, planets)

print(f'Attacked planets: {len(planets["Attacked"])}')
if planets['Attacked']:
    for attacked in sorted(planets['Attacked']):
        print(f'-> {attacked}')
print(f'Destroyed planets: {(len(planets["Destroyed"]))}')
if planets['Destroyed']:
    for destroyed in sorted(planets['Destroyed']):
        print(f'-> {destroyed}')
