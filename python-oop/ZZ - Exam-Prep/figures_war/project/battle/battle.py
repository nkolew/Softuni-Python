from abc import ABC, abstractmethod
from typing import Optional

from project import Figure


class Battle(ABC):
    @property
    @abstractmethod
    def _attr(self) -> str:
        ...
    
    def battle(self, fig_1: Figure, fig_2: Figure) -> Optional[Figure]:
        if fig_1.has_equal_attrs(fig_2, self._attr):
            return None
        
        elif fig_1.has_larger_attr_than(fig_2, self._attr):
            return fig_1
        
        else:
            return fig_2
