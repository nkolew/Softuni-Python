import re


pattern = r'(^|(?<=\s))(?P<num>-?\d+(\.[\d]+)?)($|(?=\s))'
data = input()

matches = re.finditer(pattern, data)

numbers = [n.group('num') for n in matches]
print(*numbers)