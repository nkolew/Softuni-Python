from typing import ClassVar

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    _hw_type: ClassVar[str] = 'Power'
    _capacity_factor: ClassVar[float] = 0.25
    _memory_factor: ClassVar[float] = 1.75

    def __init__(self, name: str, capacity: int, memory: int) -> None:
        type = self.__class__._hw_type
        capacity = int(capacity * self.__class__._capacity_factor)
        memory = int(memory * self.__class__._memory_factor)
        super().__init__(name, type, capacity, memory)

