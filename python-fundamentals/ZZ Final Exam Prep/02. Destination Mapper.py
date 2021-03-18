import re


places = input()

pattern = r'(?P<sym>/|=)(?P<place>[A-Z][A-Za-z]{2,})(?P=sym)'
valid_places = []
for m in re.finditer(pattern, places):
    valid_places.append(m.group('place'))
travel_points = sum([len(place) for place in valid_places])
print(f'Destinations: {", ".join(valid_places)}')
print(f'Travel Points: {travel_points}')
