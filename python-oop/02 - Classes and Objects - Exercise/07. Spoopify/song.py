class Song:
    def __init__(self, name: str, length: float, single: bool) -> None:
        self.name = name
        self.length = length
        self.single = single

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def get_info(self) -> str:
        return f'{self.name} - {self.length}'
