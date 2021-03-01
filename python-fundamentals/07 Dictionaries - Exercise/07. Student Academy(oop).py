class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades = []
        self.av_grade = 0

    def add_grade(self, grade):
        self.grades.append(grade)


class Academy:
    def __init__(self) -> None:
        self.students = []
        self.filtered = []

    def enroll(self, name: str, grade: float):
        new_student = True
        for s in self.students:
            if s.name == name:
                new_student = False
                s.add_grade(grade)
        if new_student:
            student = Student(name)
            student.add_grade(grade)
            self.students.append(student)

    def filter(self, THRESHOLD: float):
        for student in self.students:
            student.av_grade += sum(student.grades)/len(student.grades)
            if student.av_grade >= THRESHOLD:
                self.filtered.append(student)

    def __repr__(self) -> str:

        def sort_desc(student: Student):
            return -student.av_grade

        nl = '\n'
        result = []
        for student in sorted(self.filtered, key=sort_desc):
            result.append(f'{student.name} -> {student.av_grade:.2f}')
        return nl.join(result)


THRESHOLD = 4.50
a = Academy()
n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    a.enroll(name, grade)

a.filter(THRESHOLD)
print(a)
