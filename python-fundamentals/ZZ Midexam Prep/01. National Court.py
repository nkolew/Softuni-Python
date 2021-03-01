emp1_eff = int(input())
emp2_eff = int(input())
emp3_eff = int(input())
total_people_count = int(input())

people_answered_per_hour = sum([emp1_eff, emp2_eff, emp3_eff])

hour = 0
while total_people_count > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    total_people_count -= people_answered_per_hour

print(f'Time needed: {hour}h.')
