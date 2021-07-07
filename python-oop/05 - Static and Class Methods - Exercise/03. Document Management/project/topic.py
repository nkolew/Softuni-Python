class Topic:
    id: int
    topic: str
    storage_folder: str

    def __init__(self, id: int, topic: str, storage_folder: str) -> None:
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str) -> None:
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.id == o.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'Topic {self.id}: {self.topic} in {self.storage_folder}'
