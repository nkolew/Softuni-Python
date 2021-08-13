from abc import ABC, abstractmethod
from typing import Tuple

SEP = ', '


class Figure(ABC):
    name: str
    _attributes: Tuple[float, ...]

    @abstractmethod
    def __init__(self, name: str, *attributes: float) -> None:
        self.name = name
        self.attributes = attributes

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.name == o.name

    @staticmethod
    def _validate(value: float) -> None:
        if value < 0:
            raise ValueError("Negative number!")

        return None

    @property
    def attributes(self):
        """The attributes property."""
        return self._attributes

    @attributes.setter
    def attributes(self, values):
        for a in values:
            self._validate(a)

        self._attributes = values

    def _get_attr_values(self, o, attr) -> Tuple[float, float]:
        self_attr = getattr(self, attr)
        o_attr = getattr(o, attr)
        return self_attr, o_attr

    def has_larger_attr_than(self, o: 'Figure', attr: str) -> bool:
        self_attr, o_attr = self._get_attr_values(o, attr)
        return self_attr > o_attr

    def has_equal_attrs(self, o: 'Figure', attr: str) -> bool:
        self_attr, o_attr = self._get_attr_values(o, attr)
        return self_attr == o_attr

    @abstractmethod
    def calculate_area(self) -> float:
        ...

    @abstractmethod
    def calculate_circumference(self) -> float:
        ...

    @property
    def area(self) -> float:
        return self.calculate_area()

    @property
    def circumference(self) -> float:
        return self.calculate_circumference()

    @property
    def relativity(self) -> float:
        return self.area / self.circumference

    def __str__(self) -> str:
        return f'''Figure name: {self.name}
Parameters: {SEP.join(map(str, self.attributes))}
Area: {self.calculate_area()}
Circumference: {self.calculate_circumference()}
Relativity: {self.relativity}'''
