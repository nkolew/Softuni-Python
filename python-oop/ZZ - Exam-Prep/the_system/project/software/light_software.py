from typing import ClassVar

from project.software.software import Software


class LightSoftware(Software):
    _sw_type: ClassVar[str] = 'Light'
    _capacity_factor: ClassVar[float] = 1.5
    _memory_factor: ClassVar[float] = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int) -> None:
        type = self.__class__._sw_type
        capacity_consumption = int(
            capacity_consumption * self.__class__._capacity_factor)
        memory_consumption = int(
            memory_consumption * self.__class__._memory_factor)
        super().__init__(name, type, capacity_consumption, memory_consumption)
