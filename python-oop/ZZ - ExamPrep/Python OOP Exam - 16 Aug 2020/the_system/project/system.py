from typing import List

from project import (Software, Hardware, PowerHardware,
                     HeavyHardware, ExpressSoftware, LightSoftware)


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

# All described methods below should be static!

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        """Create a PowerHardware instance and add it to the hardware list"""

        __class__._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        """Create a HeavyHardware instance and add it to the hardware list"""

        __class__._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str,
                                  name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int):
        """
        •	If the hardware with the given name does NOT exist, 
            return a message "Hardware does not exist"
        •	Otherwise, create an ExpressSoftware instance, 
            install it on the hardware(if possible)
            and add it to the software list
            (if installed successfully)
        •	If the installation is not possible 
            return the message of the raised Exception
        """

        for h in __class__._hardware:
            if h.name == hardware_name:
                try:
                    sw = ExpressSoftware(
                        name, capacity_consumption, memory_consumption)
                    h.install(sw)
                    __class__._software.append(sw)

                except Exception as exc:
                    return f'{str(exc)}'

        return f'Hardware does not exist'

    @staticmethod
    def register_light_software(hardware_name: str,
                                name: str,
                                capacity_consumption: int,
                                memory_consumption: int):
        """
        •	If the hardware with the given name does NOT exist, 
            return a message "Hardware does not exist"
        •	Otherwise, create a LightSoftware instance,
            install it on the hardware(if possible)
            and add it to the software list(if installed successfully)
        •	If the installation is not possible 
            return the message of the raised Exception
        """

        for h in __class__._hardware:
            if h.name == hardware_name:
                try:
                    sw = LightSoftware(
                        name, capacity_consumption, memory_consumption)
                    h.install(sw)
                    __class__._software.append(sw)

                except Exception as exc:
                    return f'{str(exc)}'

        return f'Hardware does not exist'

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        """
        •	If both components exist on the system, 
            uninstall the software from the given hardware
        •	Otherwise, return a message 
            "Some of the components do not exist"
        """

        hw, sw = None, None

        for h in __class__._hardware:
            if h.name == hardware_name:
                hw = h

                for s in hw.software_components:
                    if s.name == software_name:
                        sw = s
                        hw.uninstall(sw)
                        __class__._software.pop(__class__._software.index(sw))

        if not sw or not hw:
            return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        """
        Return the following information(as a string). 
        The total memory and capacity used is calculated 
        of all hardware components in the system:
        System Analysis
        Hardware Components: {count of hardware components}
        Software Components: {count of software components}
        Total Operational Memory: {total used memory} / {total memory}
        Total Capacity Taken: {total used space} / {total capacity}
        """

        total_used_memory = sum(h._used_memory
                                for h in __class__._hardware)
        total_memory = sum((h.memory) for h in __class__._hardware)

        total_used_space = sum(h._used_capacity
                               for h in __class__._hardware)
        total_space = sum(h.capacity for h in __class__._hardware)

        rv = [
            'System Analysis',
            f'Hardware Components: {len(__class__._hardware)}',
            f'Software Components: {len(__class__._software)}',
            f'Total Operational Memory: {total_used_memory} / {total_memory}',
            f'Total Capacity Taken: {total_used_space} / {total_space}',
        ]

        return '\n'.join(rv)

    @staticmethod
    def system_split():
        """
        Return the following information(as a string) 
        for each hardware component:
        Hardware Component - {component name}
        Express Software Components: {number of the installed express software components}
        Light Software Components: {number of the installed light software components}
        Memory Usage: {total memory used of all installed software components} / {total memory of the hardware}
        Capacity Usage: {total capacity used of all installed software components} / {total capacity of the hardware}
        Type: {type}
        Software Components: {names of all software components separated by ', '} ( or 'None' if no software components)
        Note: Feel free to add any additional methods that might help you.
        """

        rv = [
            str(h) for h in __class__._hardware
        ]

        return '\n'.join(rv)
