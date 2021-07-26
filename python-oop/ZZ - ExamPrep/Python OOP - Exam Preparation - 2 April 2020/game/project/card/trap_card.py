from project.card.card import Card


class TrapCard(Card):
    initial_damage_points = 120
    initial_health_points = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, self.initial_damage_points, self.initial_health_points)
