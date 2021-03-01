snowballs_count = int(input())

max_value = 0
max_snow = 0
max_time = 0
max_quality = 0

for snowall in range(1, snowballs_count + 1):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)

    if snowball_value > max_value:
        max_value = snowball_value
        max_snow = snowball_snow
        max_time = snowball_time
        max_quality = snowball_quality

print(f'{max_snow} : {max_time} = {max_value} ({max_quality})')
