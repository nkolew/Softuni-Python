courses = {}

while True:
    tokens = input()
    if tokens == 'end':
        break
    course_name, student = tokens.split(' : ')
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)

result = []

for course_name, students in sorted(courses.items(), key=lambda x: -len(x[1])):
    result.append(f'{course_name}: {len(students)}')
    for student in sorted(students):
        result.append(f'-- {student}')

print('\n'.join(result))
