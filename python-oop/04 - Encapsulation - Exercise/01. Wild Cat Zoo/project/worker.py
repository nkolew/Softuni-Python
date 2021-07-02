class Worker:
    name: str
    age: int
    salary: int

    def __init__(self, name: str, age: int, salary: int) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'
