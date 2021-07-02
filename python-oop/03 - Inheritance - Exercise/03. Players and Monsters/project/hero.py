class Hero:
    username: str
    level: int

    def __init__(self, username, level) -> None:
        self.username = username
        self.level = level

    def __str__(self) -> str:
        return f'{self.username} of type {self.__class__.__name__} has level {self.level}'
