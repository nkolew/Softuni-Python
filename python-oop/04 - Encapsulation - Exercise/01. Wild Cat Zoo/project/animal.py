from typing import ClassVar


class Animal:
    name: str
    gender: str
    age: int

    _NEEDS: ClassVar[int] = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

    def get_needs(self):
        return self.__class__._NEEDS
