w = float(input())
l = float(input())
h = float(input())
avg_h = float(input())

spacecraft_vol = w * l * h
room_vol = 2 * 2 * (avg_h + 0.40)
astronauts_count = int(spacecraft_vol / room_vol)

if astronauts_count < 3:
    print(f'The spacecraft is too small.')
elif 3 <= astronauts_count <= 10:
    print(f'The spacecraft holds {astronauts_count} astronauts.')
else:
    print(f'The spacecraft is too big.')