from typing import ClassVar

from project.player.player import Player


class Advanced(Player):
    _initial_health: ClassVar[int] = 250
