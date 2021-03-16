import re


pattern = r'(^|(?<=\s))(?P<day>\d\d)(?P<sep>[\./-])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>\d{4})($|,|(?=\s))'
data = input()

for match in re.finditer(pattern, data):
    print(
        f'Day: {match.group("day")}, Month: {match.group("month")}, Year: {match.group("year")}')
