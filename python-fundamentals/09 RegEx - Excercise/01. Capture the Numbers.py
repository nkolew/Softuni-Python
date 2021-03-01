import re

pattern = r'\d+'
numbers = []
line = input()

while line:
    numbers.extend(re.findall(pattern, line))
    line = input()

print(' '.join(numbers))