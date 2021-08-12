from typing import ClassVar

from project.card.card import Card


class MagicCard(Card):
    _initial_damage_points: ClassVar[int] = 5
    _initial_health_points: ClassVar[int] = 80
