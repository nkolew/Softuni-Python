from collections import defaultdict


class Student:
    def __init__(self, name: str) -> None:
        self.name = name


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.students = []

    def enroll(self, student: Student):
        self.students.append(student)


class Program:
    def __init__(self) -> None:
        self.courses = defaultdict(list)

    def add_course(self, c_name: str, s_name: str):
        new_course = True
        for name, value in self.courses.items():
            course = value[0]
            if name == c_name:
                new_course = False
                course.enroll(Student(s_name))
        if new_course:
            course = Course(c_name)
            course.enroll(Student(s_name))
            self.courses[c_name].append(course)

    def __repr__(self) -> str:

        def len_sort_fn(value: list):
            course = value[0]
            return -len(course.students)

        def ab_sort_fn(student: Student):
            return student.name

        result = []
        for value in sorted(self.courses.values(), key=len_sort_fn):
            course = value[0]
            result.append(f'{course.name}: {len(course.students)}')
            for student in sorted(course.students, key=ab_sort_fn):
                result.append(f'-- {student.name}')
        result = '\n'.join(result)
        return result


p = Program()

while True:
    tokens = input()
    if tokens == 'end':
        break
    course_name, student_name = tokens.split(' : ')
    p.add_course(course_name, student_name)

print(p)
