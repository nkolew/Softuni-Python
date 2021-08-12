from typing import List, Optional

from project.player.player import Player


class PlayerRepository:
    players: List[Player]

    def __init__(self) -> None:
        self.players = []

    @property
    def count(self) -> int:
        return len(self.players)

    def add(self, player: Player) -> None:
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)

    def find(self, username: str) -> Optional[Player]:
        for p in self.players:
            if p.username == username:
                return p

        return None

    def remove(self, player_name: str):
        if player_name == '':
            raise ValueError("Player cannot be an empty string!")

        player = self.find(player_name)
        if player:
            self.players.remove(player)
