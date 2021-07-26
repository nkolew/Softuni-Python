from typing import ClassVar

from project import Software


class LightSoftware(Software):
    _TYPE: str = 'Light'
    _CAPACITY_FACTOR: ClassVar[float] = 1.5
    _MEMORY_FACTOR: ClassVar[float] = 0.5

    def __init__(self, name: str, capacity_consumption: float, memory_consumption: float) -> None:
        type = self.__class__._TYPE
        capacity_consumption *= self.__class__._CAPACITY_FACTOR
        memory_consumption *= self.__class__._MEMORY_FACTOR
        super().__init__(name, type, int(capacity_consumption), int(memory_consumption))
