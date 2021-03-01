import re


pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
data = input()

matches = re.finditer(pattern, data)

numbers = [n.group() for n in matches]
print(*numbers)