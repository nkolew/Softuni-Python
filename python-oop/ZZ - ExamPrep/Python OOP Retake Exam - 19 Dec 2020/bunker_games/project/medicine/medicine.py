from abc import ABC, abstractmethod

from project import Survivor


class Medicine(ABC):
    __health_increase: int

    def __init__(self, health_increase: int) -> None:
        self.health_increase = health_increase

    @property
    @abstractmethod
    def _HEALTH_INCREASE(self) -> int:
        ...

    @property
    def health_increase(self):
        """The health_increase property."""
        return self.__health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError('Health increase cannot be less than zero.')

        self.__health_increase = value

    def apply(self, survivor: Survivor) -> None:
        survivor.health += self.health_increase
