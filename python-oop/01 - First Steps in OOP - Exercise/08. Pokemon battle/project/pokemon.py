class Pokemon:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.name == o.name

    def pokemon_details(self):
        return f'{self.name} with health {self.health}'
