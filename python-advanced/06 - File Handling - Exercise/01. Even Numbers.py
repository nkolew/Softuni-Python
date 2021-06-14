import string
import re
import os


file = f'{os.path.dirname(os.path.abspath(__file__))}/text.txt'
pattern = rf'[{string.punctuation}]'

with open(file, 'r') as fh:
    content = fh.readlines()

for i, line in enumerate(content):
    if i % 2 == 0:
        line = re.sub(pattern, '@', line)
        line = ' '.join(reversed(line.split()))
        print(line.strip())
