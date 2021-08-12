from typing import ClassVar


class Survivor:
    _name: str
    _age: int

    _health: int
    _needs: int

    _max_health: ClassVar[int] = 100
    _max_needs: ClassVar[int] = 100

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.health = self._max_health
        self.needs = self._max_needs

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    @property
    def name(self):
        """The name property."""
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name not valid!')
        self._name = value

    @property
    def age(self):
        """The age property."""
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('Age not valid!')
        self._age = value

    @property
    def health(self):
        """The health property."""
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError('Health not valid!')
        self._health = value if value < self._max_health else self._max_health

    @property
    def needs(self):
        """The needs property."""
        return self._needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError('Needs not valid!')
        self._needs = value if value < self._max_needs else self._max_needs

    @property
    def needs_sustenance(self) -> bool:
        return self.needs < self._max_needs

    @property
    def needs_healing(self) -> bool:
        return self.health < self._max_health
