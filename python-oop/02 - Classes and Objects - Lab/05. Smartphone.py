class Smartphone:
    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps: list = []
        self.is_on: bool = False
        self.used_memory = 0

    def power(self) -> None:
        self.is_on = not self.is_on
    
    def install(self, app_name: str, app_memory: int) -> str:
        if not self.is_on:
            return f'Turn on your phone to install {app_name}'
        
        if self.memory < self.used_memory + app_memory:
            return f'Not enough memory to install {app_name}'

        self.apps.append(app_name)
        self.used_memory += app_memory
        return f'Installing {app_name}'

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory - self.used_memory
        return f'Total apps: {total_apps_count}. Memory left: {memory_left}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
