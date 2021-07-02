class Person:
    __name: str
    __age: int

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
