import re


s = input()
pattern = r'(?P<pair>(?P<sym>#|@)(?P<w1>[A-Za-z]{3,})(?P=sym){2}(?P<w2>[A-Za-z]{3,})(?P=sym))'
pairs_found = []
mirror_words = []

for m in re.finditer(pattern, s):
    pairs_found.append(m.group('pair'))
    if m.group('w1') == m.group('w2')[::-1]:
        mirror_words.append(f"{m.group('w1')} <=> {m.group('w2')}")

if len(pairs_found) == 0:
    print('No word pairs found!')
    print('No mirror words!')
else:
    print(f'{len(pairs_found)} word pairs found!')
    if len(mirror_words) == 0:
        print(f'No mirror words!')
    else:
        print('The mirror words are:')
        print(f'{", ".join(mirror_words)}')
