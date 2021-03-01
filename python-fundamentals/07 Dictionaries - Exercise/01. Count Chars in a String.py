from collections import defaultdict


string = input()
chars = defaultdict(int)

for c in list(string):
    if not c.isspace():
        chars[c] += 1

for k, v in chars.items():
    print(f'{k} -> {v}')
