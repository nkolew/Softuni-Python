from typing import ClassVar


class Survivor:
    _MAX_HEALTH: ClassVar[int] = 100
    _MAX_NEEDS: ClassVar[int] = 100

    __name: str
    __age: int
    __health: int
    __needs: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.health = self.__class__._MAX_HEALTH
        self.needs = self.__class__._MAX_NEEDS

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    def __hash__(self) -> int:
        return hash(self.name)

    @property
    def name(self) -> str:
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value) -> None:
        if value == '':
            raise ValueError('Name not valid!')

        self.__name = value

    @property
    def age(self) -> int:
        """The age property."""
        return self.__age

    @age.setter
    def age(self, value) -> None:
        if value < 0:
            raise ValueError("Age not valid!")

        self.__age = value

    @property
    def health(self) -> int:
        """The health property."""
        return self.__health

    @health.setter
    def health(self, value) -> None:
        if value < 0:
            raise ValueError("Health not valid!")

        value = value if value < self.__class__._MAX_HEALTH else self.__class__._MAX_HEALTH
        # value = min(value, self.__class__._MAX_HEALTH)

        self.__health = value

    @property
    def needs(self) -> int:
        """The needs property."""
        return self.__needs

    @needs.setter
    def needs(self, value) -> None:
        if value < 0:
            raise ValueError("Needs not valid!")

        value = value if value < self.__class__._MAX_NEEDS else self.__class__._MAX_NEEDS
        # value = min(value, self.__class__._MAX_NEEDS)

        self.__needs = value

    @property
    def needs_sustenance(self) -> bool:
        """The needs_sustenance property."""
        return self.needs < self.__class__._MAX_NEEDS

    @property
    def needs_healing(self) -> bool:
        """The needs_healing property."""
        return self.health < self.__class__._MAX_HEALTH
