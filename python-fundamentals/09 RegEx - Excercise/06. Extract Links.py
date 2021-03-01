import re


pattern = r'(^|(?<=\s))w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))'

while True:
    line = input()
    if not line:
        break
    for m in re.finditer(pattern, line):
        print(m.group())
