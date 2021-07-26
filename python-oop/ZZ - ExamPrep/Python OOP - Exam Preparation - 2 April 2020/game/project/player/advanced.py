from project.player.player import Player


class Advanced(Player):
    initial_hp = 250

    def __init__(self, username: str) -> None:
        super().__init__(username, self.initial_hp)
