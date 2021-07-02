class Product:
    name: str
    quantity: int

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        return f'{self.name}: {self.quantity}'

    def decrease(self, quantity: int) -> None:
        if quantity <= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity
