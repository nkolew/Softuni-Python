class Player:
    __name: str
    __sprint: int
    __dribble: int
    __passing: int
    __shooting: int

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __eq__(self, o: object) -> bool:
        return isinstance(o, type(self)) and self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        self.__name = value

    def __str__(self) -> str:
        message = []
        NL = '\n'

        message.append(f'Player: {self.__name}')
        message.append(f'Sprint: {self.__sprint}')
        message.append(f'Dribble: {self.__dribble}')
        message.append(f'Passing: {self.__passing}')
        message.append(f'Shooting: {self.__shooting}')

        return NL.join(message)
