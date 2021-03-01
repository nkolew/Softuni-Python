cells = input().split('#')
water_amount = int(input())

HIGH_RANGE = range(81,126)
MEDIUM_RANGE = range(51,81)
LOW_RANGE = range(1,51)

effort = 0
putout_fires = []

for cell in cells:
    fire_type, fire_value = cell.split(' = ')
    fire_value = int(fire_value)

    if fire_type == 'High' and fire_value not in HIGH_RANGE:
        continue

    elif fire_type == 'Medium' and fire_value not in MEDIUM_RANGE:
        continue

    elif fire_type == 'Low' and fire_value not in LOW_RANGE:
        continue

    if water_amount >= fire_value:
        water_amount -= fire_value
        effort += fire_value * 0.25
        putout_fires.append(fire_value)
        
print('Cells:')
for cell in putout_fires:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(putout_fires)}')
