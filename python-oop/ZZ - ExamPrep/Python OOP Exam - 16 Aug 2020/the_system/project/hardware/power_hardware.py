from typing import ClassVar

from project import Hardware


class PowerHardware(Hardware):
    _TYPE: str = 'Power'
    _CAPACITY_FACTOR: ClassVar[float] = 0.25
    _MEMORY_FACTOR: ClassVar[float] = 1.75

    def __init__(self, name, capacity, memory):
        type = self.__class__._TYPE
        capacity *= self.__class__._CAPACITY_FACTOR
        memory *= self.__class__._MEMORY_FACTOR
        super().__init__(name, type, int(capacity), int(memory))
