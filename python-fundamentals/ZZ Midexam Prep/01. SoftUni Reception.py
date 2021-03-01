е1 = int(input())
е2 = int(input())
е3 = int(input())
students_count = int(input())

students_per_hour = sum([е1, е2, е3])

hour = 0
while students_count > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    students_count -= students_per_hour

print(f'Time needed: {hour}h.')
