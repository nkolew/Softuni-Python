class Programmer:
    def __init__(self, name: str, language: str, skills: int) -> None:
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int):
        if language == self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language: str, skills_needed: int):
        if self.skills >= skills_needed:
            if self.language != new_language:
                previous_language = self.language
                self.language = new_language
                return f'{self.name} switched from {previous_language} to {self.language}'
            return f'{self.name} already knows {new_language}'
        return f'{self.name} needs {skills_needed-self.skills} more skills'


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
