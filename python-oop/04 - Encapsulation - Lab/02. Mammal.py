from typing import ClassVar


class Mammal:
    kingdom: ClassVar[str] = 'animals'
    name: str
    type_: str
    sound: str

    def __init__(self, name: str, type_: str, sound: str) -> None:
        self.name = name
        self.type_ = type_
        self.sound = sound

    def make_sound(self) -> str:
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__class__.kingdom

    def info(self) -> str:
        return f'{self.name} is of type {self.type_}'


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
