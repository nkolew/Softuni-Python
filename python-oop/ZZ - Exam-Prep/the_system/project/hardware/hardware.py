from typing import List

from project.software.software import Software


class Hardware:
    name: str
    type: str  # ("Heavy" or "Power")
    capacity: int
    memory: int
    software_components: List[Software]

    def __init__(self, name: str,
                 type: str,
                 capacity: int,
                 memory: int) -> None:
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) \
            and self.name == o.name

    @property
    def _total_used_capacity(self) -> int:
        """The _total_used_capacity property."""
        return sum(s.capacity_consumption for s in self.software_components)

    @property
    def _total_used_memory(self):
        """The _total_used_memory property."""
        return sum(s.memory_consumption for s in self.software_components)

    @property
    def _free_capacity(self) -> int:
        """The _free_capacity property."""
        return self.capacity - self._total_used_capacity

    @property
    def _free_memory(self) -> int:
        """The _free_memory property."""
        return self.memory - self._total_used_memory

    def _has_enough_resources_to_install(self, software: Software) -> bool:
        return self._free_capacity >= software.capacity_consumption and \
            self._free_memory >= software.memory_consumption

    def install(self, software: Software) -> None:
        if not self._has_enough_resources_to_install(software):
            raise Exception('Software cannot be installed')
        self.software_components.append(software)

    def uninstall(self, software: Software) -> None:
        if software in self.software_components:
            self.software_components.remove(software)
