# from typing import ClassVar, List


class Software:
    name: str
    type: str
    capacity_consumption: int
    memory_consumption: int

    # _VALID_TYPES: ClassVar[List[str]] = ['Express', 'Light']

    def __init__(self, name: str, type: str,
                 capacity_consumption: int,
                 memory_consumption: int) -> None:
        self.name = name
        self.type = type
        self.capacity_consumption = int(capacity_consumption)
        self.memory_consumption = int(memory_consumption)
