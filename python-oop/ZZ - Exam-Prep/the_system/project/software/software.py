class Software:
    name: str
    type: str
    capacity_consumption: int
    memory_consumption: int

    def __init__(self, name: str,
                 type: str,
                 capacity_consumption: int,
                 memory_consumption: int) -> None:
        self.name = name
        self.type = type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) \
            and o.name == self.name
