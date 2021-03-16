import re


data = input()
pattern = r'(^|(?<=\s))(?P<number>\+359(?P<sep>\s|\-)2(?P=sep)\d{3}(?P=sep)\d{4})((?=,)|$)'

matches = []
for i in re.finditer(pattern, data):
    matches.append(i.group('number'))
print(', '.join(matches))
