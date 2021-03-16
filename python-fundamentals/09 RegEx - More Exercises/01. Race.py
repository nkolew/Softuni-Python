import re

l_pattern = r'[A-Za-z]'
d_pattern = r'\d'

participants = input().split(', ')
race = {name: 0 for name in participants}

while True:
    data = input()
    if data == 'end of race':
        break
    letters = re.findall(l_pattern, data)
    digits = re.findall(d_pattern, data)
    name = ''.join(letters)
    distance = sum(map(int, digits))
    if name in race:
        race[name] += distance

count = 1
position = ''
for participant, distance in sorted(race.items(), key=lambda x: -x[1]):
    if count == 4:
        break
    position = '1st' if count == 1 else ('2nd' if count == 2 else '3rd')
    print(f'{position} place: {participant}')
    count += 1
