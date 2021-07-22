class Hardware:
    name: str
    type: str
    capacity: int
    memory: int
    software_components: list

    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []


# __init__(name: str, type: str, capacity: int, memory: int)
# Set the attributes to the provided values
# install(software: Software)
# If there is enough capacity and memory, add the software object to the software_components. Otherwise, raise Exception with message "Software cannot be installed"
# uninstall(software: Software)
# Remove the software object from the software_components
# Note: Feel free to add any additional methods that might help you.
