from typing import ClassVar, List, Optional, Tuple, Type

from project import Circle, Figure, Rectangle, Square, Triangle

SEP = ', '


class Suitcase:
    _valid_figure_types: ClassVar[Tuple[str, ...]] = (
        'Circle',
        'Rectangle',
        'Triangle',
        'Square'
    )

    repository: List[Figure]

    def __init__(self) -> None:
        self.repository = []

    def add(self, figure: Figure) -> str:
        if figure.__class__.__name__ not in self._valid_figure_types:
            raise TypeError('The type of Figure is incorrect!')

        if figure in self.repository:
            raise KeyError('Figure name already exist!')

        self.repository.append(figure)
        return f'Figure: {figure.name} added.'

    def get_figure(self, figure_name: str) -> Optional[Figure]:
        for f in self.repository:
            if f.name == figure_name:
                return f

        return None

    def remove(self, figure_name: str) -> str:
        figure = self.get_figure(figure_name)

        if not figure:
            raise KeyError("Figure: {figure_name} not exist!")

        self.repository.remove(figure)
        return f'Figure: {figure_name} removed.'

    def __repr__(self) -> str:
        return SEP.join(f.name for f in self.repository)
