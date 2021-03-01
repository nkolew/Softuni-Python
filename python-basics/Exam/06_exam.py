locations_count = int(input())

for location in range(locations_count):
    total_gold = 0
    avg_gold = 0
    target = float(input())
    days = int(input())
    for day in range(days):
        gold = float(input())
        total_gold += gold
    avg_gold = total_gold / days
    if avg_gold >= target:
        print(f'Good job! Average gold per day: {avg_gold:.2f}.')
    else:
        diff = abs(target - avg_gold)
        print(f'You need {diff:.2f} gold.')
