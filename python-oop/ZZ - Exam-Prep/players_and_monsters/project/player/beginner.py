from typing import ClassVar

from project.player.player import Player


class Beginner(Player):
    _initial_health: ClassVar[int] = 50
    _additional_health_bonus: ClassVar[int] = 40
    _additional_damage_bonus: ClassVar[int] = 30

    def apply_bonus(self) -> None:
        self.health += self._additional_health_bonus
        for c in self.card_repository.cards:
            c.damage_points += self._additional_damage_bonus

        super().apply_bonus()
