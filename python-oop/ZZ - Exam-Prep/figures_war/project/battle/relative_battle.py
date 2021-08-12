from typing import ClassVar

from project.battle.battle import Battle


class RelativeBattle(Battle):
    _attr: ClassVar[str] = 'relativity'