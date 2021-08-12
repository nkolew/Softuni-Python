from abc import ABC, abstractmethod

from project.survivor import Survivor


class Medicine(ABC):
    __health_increase: int

    @property
    @abstractmethod
    def _default_health_increase(self) -> int:
        ...

    def __init__(self) -> None:
        self.health_increase = self._default_health_increase

    @property
    def health_increase(self):
        """The health_increase property."""
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError('Health increase cannot be less than zero.')

        self.__health_increase = value

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase
