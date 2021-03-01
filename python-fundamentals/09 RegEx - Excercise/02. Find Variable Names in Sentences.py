import re


pattern = r'((?<=^_)|(?<=\s_))(?P<vname>[A-Za-z0-9]+)\b'
data = input()

matches = [m.group() for m in re.finditer(pattern, data)]
print(','.join(matches))