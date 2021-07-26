from typing import List

from project import Software, ExpressSoftware, LightSoftware


class Hardware:
    name: str
    type: str
    capacity: int
    memory: int
    software_components: List[Software]

    # _VALID_TYPES: ClassVar[List[str]] = ['Heavy', 'Power']

    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = int(capacity)
        self.memory = int(memory)
        self.software_components = []

    @property
    def _available_memory(self):
        return self.memory - sum(s.memory_consumption for s in self.software_components)

    @property
    def _available_capacity(self):
        return self.capacity - sum(s.capacity_consumption for s in self.software_components)

    def _has_enough_resources(self, software: Software):
        return software.capacity_consumption <= self._available_capacity \
            and software.memory_consumption <= self._available_memory

    @property
    def _used_memory(self):
        return self.memory-self._available_memory

    @property
    def _used_capacity(self):
        return self.capacity-self._available_capacity

    def install(self, software: Software) -> None:
        """
        If there is enough capacity and memory, 
        add the software object to the software_components. 
        Otherwise, raise Exception with message 
        "Software cannot be installed"
        """

        if not self._has_enough_resources(software):
            raise Exception('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        """Remove the software object from the software_components"""

        if software in self.software_components:
            self.software_components.remove(software)

    def __str__(self) -> str:
        """
        Hardware Component - {component name}
        Express Software Components: {number of the installed express software components}
        Light Software Components: {number of the installed light software components}
        Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
        Capacity Usage: {total capacity used of all installed software components} / {total capacity of the hardware}
        Type: {type}
        Software Components: {names of all software components separated by ', '} ( or 'None' if no software components)
        """

        rv = [
            f'Hardware Component - {self.name}',
            f'Express Software Components: {len([s for s in self.software_components if isinstance(s, ExpressSoftware)])}',
            f'Light Software Components: {len([s for s in self.software_components if isinstance(s, LightSoftware)])}',
            f'Memory Usage: {self._used_memory} / {self.memory}',
            f'Capacity Usage: {self._used_capacity} / {self.capacity}',
            f'Type: {self.type}',
            f'Software Components: {", ".join(s.name for s in self.software_components) or "None"}'
        ]

        return '\n'.join(rv)
