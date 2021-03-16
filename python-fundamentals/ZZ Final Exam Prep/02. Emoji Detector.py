from collections import defaultdict
from functools import reduce
import re


digits_pattern = r'(?P<dig>\d+)'
emojis_pattern = r'(?P<emoji>(?P<sign>[:]{2}|[*]{2})[A-Z][a-z]{2,}(?P=sign))'
data = input()
digits = ''
emojis = defaultdict(int)

for m in re.finditer(digits_pattern, data):
    digits += m.group('dig')
thresshold = reduce(lambda x, y: x*y, map(int, list(digits)))

for m in re.finditer(emojis_pattern, data):
    emoji = m.group('emoji')
    for c in emoji:
        if c.isalpha():
            emojis[emoji] += ord(c)

print(f'Cool threshold: {thresshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
[print(e) for e, v in emojis.items() if v > thresshold]
