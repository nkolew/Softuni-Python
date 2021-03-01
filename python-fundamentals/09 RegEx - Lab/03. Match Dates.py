import re


pattern = r'(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'
data = input()

for i in re.finditer(pattern, data):
    print(f"Day: {i.groupdict()['day']}, Month: {i.groupdict()['month']}, Year: {i.groupdict()['year']}")