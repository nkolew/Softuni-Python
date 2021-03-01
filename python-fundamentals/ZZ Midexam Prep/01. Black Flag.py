days = int(input())
daily_loot = int(input())
expected_loot = int(input())
total_loot = 0

for day in range(1, days+1):
    total_loot += daily_loot
    if day % 3 == 0:
        total_loot += 0.5 * daily_loot
    if day % 5 == 0:
        total_loot *= 0.7

if total_loot >= expected_loot:
    print(f'Ahoy! {total_loot:.2f} plunder gained.')
else:
    print(
        f'Collected only {total_loot * 100 / expected_loot:.2f}% of the plunder.')
