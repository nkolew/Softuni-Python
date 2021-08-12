from typing import ClassVar, List, Optional, Union

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: ClassVar[List[Hardware]] = []
    _software: ClassVar[List[Software]] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        __class__._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        __class__._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def _find_obj_by_type_and_name(obj_type: str, obj_name: str) -> Optional[Union[Software, Hardware]]:
        objects = {
            'Hardware': __class__._hardware,
            'Software': __class__._software
        }

        for o in objects[obj_type]:
            if o.name == obj_name:
                return o

        return None

    @staticmethod
    def _register_software(hardware_name: str, s: Software):
        h = __class__._find_obj_by_type_and_name('Hardware', hardware_name)
        if not h or not isinstance(h, Hardware):
            return 'Hardware does not exist'
        try:
            h.install(s)
            __class__._software.append(s)
        except Exception as exc:
            return str(exc)

    @staticmethod
    def register_express_software(hardware_name: str,
                                  name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int) -> Union[None, str]:

        s = ExpressSoftware(name, capacity_consumption, memory_consumption)
        return __class__._register_software(hardware_name, s)

    @staticmethod
    def register_light_software(hardware_name: str,
                                name: str,
                                capacity_consumption: int,
                                memory_consumption: int) -> Union[None, str]:
        s = LightSoftware(name, capacity_consumption, memory_consumption)
        return __class__._register_software(hardware_name, s)

    @staticmethod
    def _apply_software_component_removal(h: Hardware, s: Software) -> None:
        h.uninstall(s)
        __class__._software.remove(s)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str) -> Union[None, str]:
        h = __class__._find_obj_by_type_and_name('Hardware', hardware_name)
        s = __class__._find_obj_by_type_and_name('Software', software_name)
        if not (h or s) or not isinstance(h, Hardware) or not isinstance(s, Software):
            return 'Some of the components do not exist'
        __class__._apply_software_component_removal(h, s)

    @staticmethod
    def _total_used_memory():
        return sum(h._total_used_memory for h in __class__._hardware)

    @staticmethod
    def _total_memory():
        return sum(h.memory for h in __class__._hardware)

    @staticmethod
    def _total_used_capacity():
        return sum(h._total_used_capacity for h in __class__._hardware)

    @staticmethod
    def _total_capacity():
        return sum(h.capacity for h in __class__._hardware)

    @staticmethod
    def analyze():
        return '\n'.join(
            ['System Analysis',
             f'Hardware Components: {len(__class__._hardware)}',
             f'Software Components: {len(__class__._software)}',
             f'Total Operational Memory: {__class__._total_used_memory()} / {__class__._total_memory()}',
             f'Total Capacity Taken: {__class__._total_used_capacity()} / {__class__._total_capacity()}',
             ]
        )

    @staticmethod
    def system_split():
        return ''.join(
            ['\n'.join(
                [
                    f'Hardware Component - {h.name}',
                    f'Express Software Components: {len([s for s in h.software_components if isinstance(s, ExpressSoftware)])}',
                    f'Light Software Components: {len([s for s in h.software_components if isinstance(s, LightSoftware)])}',
                    f'Memory Usage: {sum(s.memory_consumption for s in h.software_components)} / {h.memory}',
                    f'Capacity Usage: {sum(s.capacity_consumption for s in h.software_components)} / {h.capacity}',
                    f'Type: {h.type}',
                    f'Software Components: {", ".join([s.name for s in h.software_components]) or "None"}',
                ])
                for h in __class__._hardware
             ])
