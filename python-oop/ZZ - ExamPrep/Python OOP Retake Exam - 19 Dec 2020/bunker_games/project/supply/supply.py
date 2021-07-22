from abc import ABC, abstractmethod

from project import Survivor


class Supply(ABC):
    __needs_increase: int

    def __init__(self, needs_increase: int) -> None:
        self.needs_increase = needs_increase

    @property
    @abstractmethod
    def _NEEDS_INCREASE(self) -> int:
        ...

    @property
    def needs_increase(self) -> int:
        """The needs_increase property."""
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value) -> None:
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")

        self.__needs_increase = value

    def apply(self, survivor: Survivor) -> None:
        survivor.needs += self.needs_increase
