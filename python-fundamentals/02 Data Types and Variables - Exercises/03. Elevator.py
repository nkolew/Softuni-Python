from math import ceil

people_count = int(input())
elevator_capacity = int(input())

courses = ceil(people_count / elevator_capacity)
print(courses)
