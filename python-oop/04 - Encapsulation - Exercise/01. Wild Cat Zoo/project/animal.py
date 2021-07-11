class Animal:
    name: str
    gender: str
    age: int
    money_for_care: int

    def __init__(self, name: str, gender: str, age: int, money_for_care: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'
