from typing import List, Union

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    decorations: List[BaseDecoration]

    def __init__(self) -> None:
        self.decorations = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def find_by_type(self, decoration_type: str) -> Union[BaseDecoration, str]:
        for d in self.decorations:
            if d.__class__.__name__ == decoration_type:
                return d
        return "None"

    def remove(self, decoration: BaseDecoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False
