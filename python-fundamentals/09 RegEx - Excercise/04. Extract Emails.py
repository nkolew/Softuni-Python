import re

data = input()
pattern = r'(^|(?<=\s))(?P<alnum>[A-Za-z0-9]+)([\._-])?[A-Za-z0-9]+@(?P<alpha>[A-Za-z]+)\-?[A-Za-z]+(\.[A-Za-z]+\-?[A-Za-z]+)+($|(?=\s))'

result = re.finditer(pattern, data)

for m in result:
    print(m.group())