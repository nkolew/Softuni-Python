from project.player.player import Player


class Beginner(Player):
    initial_hp = 50
    beginner_hp_bonus = 40

    def __init__(self, username: str) -> None:
        super().__init__(username, self.initial_hp)

    def apply_bonus(self):
        super().apply_bonus()
        
        self.health += self.beginner_hp_bonus
        for c in self.card_repository.cards:
            c.damage_points += 30
