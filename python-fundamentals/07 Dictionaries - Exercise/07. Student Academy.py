students = {}

n = int(input())

for _ in range(n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = [student_grade]
    else:
        students[student_name].append(student_grade)

filtered_students = {}

for student_name, student_grades in students.items():
    av_grade = sum(student_grades) / len(student_grades)
    if av_grade >= 4.50:
        filtered_students[student_name] = av_grade

result = []
for student_name, av_grade in sorted(filtered_students.items(), key=lambda x: -x[1]):
    result.append(f'{student_name} -> {av_grade:.2f}')
print('\n'.join(result))
