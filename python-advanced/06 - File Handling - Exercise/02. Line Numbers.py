import string
import os

input = f'{os.path.dirname(os.path.abspath(__file__))}/text.txt'
output = f'{os.path.dirname(os.path.abspath(__file__))}/output.txt'

with open(input, 'r') as fh:
    content = fh.readlines()

out = []
for index, line in enumerate(content):
    chars = {
        'punct': 0,
        'let': 0,
    }

    line_nr = f'Line {index+1}'
    line = line.strip()
    words = line.split()

    for word in words:
        for c in word:
            if c in string.punctuation:
                chars['punct'] += 1
            else:
                chars['let'] += 1

    out.append(f'{line_nr}: {line} ({chars["let"]})({chars["punct"]})')
out = '\n'.join(out)

with open(output, 'w') as fh:
    fh.write(out)
