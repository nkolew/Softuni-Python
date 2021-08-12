from typing import ClassVar

from project.card.card import Card


class TrapCard(Card):
    _initial_damage_points: ClassVar[int] = 120
    _initial_health_points: ClassVar[int] = 5
