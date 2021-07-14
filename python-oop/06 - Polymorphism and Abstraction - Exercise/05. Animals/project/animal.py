from abc import ABC, abstractmethod


class Animal(ABC):
    name: str
    age: int
    gender: str

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self) -> str:
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

    @property
    @abstractmethod
    def _SOUND(self) -> str:
        ...

    def make_sound(self):
        return self._SOUND
