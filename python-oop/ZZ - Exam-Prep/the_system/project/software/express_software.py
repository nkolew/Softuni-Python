from typing import ClassVar

from project.software.software import Software


class ExpressSoftware(Software):
    _sw_type: ClassVar[str] = 'Express'
    _capacity_factor: ClassVar[float] = 1.0
    _memory_factor: ClassVar[float] = 2.0

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int) -> None:
        type = self.__class__._sw_type
        capacity_consumption = int(
            capacity_consumption * self.__class__._capacity_factor)
        memory_consumption = int(
            memory_consumption * self.__class__._memory_factor)
        super().__init__(name, type, capacity_consumption, memory_consumption)
