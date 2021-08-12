from typing import ClassVar

from project.battle.battle import Battle


class AreaBattle(Battle):
    _attr: ClassVar[str] = 'area'
