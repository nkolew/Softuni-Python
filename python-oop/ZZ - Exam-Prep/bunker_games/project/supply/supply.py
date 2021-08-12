from abc import ABC, abstractmethod

from project.survivor import Survivor


class Supply(ABC):
    __needs_increase: int

    @property
    @abstractmethod
    def _default_needs_increase(self) -> int:
        ...

    def __init__(self) -> None:
        self.needs_increase = self._default_needs_increase

    @property
    def needs_increase(self):
        """The need_increase property."""
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError('Needs increase cannot be less than zero.')

        self.__needs_increase = value

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
