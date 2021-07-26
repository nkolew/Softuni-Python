from typing import List, Optional

from project.player.player import Player


class PlayerRepository:
    count: int
    players: List[Player]

    def __init__(self) -> None:
        self.count = 0
        self.players = []

    def add(self, player: Player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")

        p = self.find(player)
        if p:
            self.players.pop(self.players.index(p))
            self.count -= 1

    def find(self, username: str) -> Optional[Player]:
        for p in self.players:
            if p.username == username:
                return p

        return None
