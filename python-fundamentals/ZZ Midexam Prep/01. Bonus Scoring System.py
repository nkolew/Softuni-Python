students_count = int(input())
course_lectures = int(input())
bonus = int(input())
total_bonus = 0
max_bonus = 0
attendance_max_bonus = 0

for student in range(students_count):
    student_attendances = int(input())
    total_bonus = student_attendances / course_lectures * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendance_max_bonus = student_attendances

print(
    f'Max Bonus: {round(max_bonus)}.\nThe student has attended {round(attendance_max_bonus)} lectures.')
