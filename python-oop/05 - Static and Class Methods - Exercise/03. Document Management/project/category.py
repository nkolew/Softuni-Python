class Category:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def edit(self, new_name: str) -> None:
        self.name = new_name

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'Category {self.id}: {self.name}'
