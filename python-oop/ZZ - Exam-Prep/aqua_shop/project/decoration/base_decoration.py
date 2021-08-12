from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    comfort: int
    price: float

    def __init__(self) -> None:
        self.comfort = self._default_comfort
        self.price = self._default_price

    @property
    @abstractmethod
    def _default_comfort(self) -> int:
        ...

    @property
    @abstractmethod
    def _default_price(self) -> float:
        ...
