from player import Player
from typing import List


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str) -> str:
        for i, player in enumerate(self.players):
            if player.name == player_name:
                self.players.pop(i)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        message = []
        nl = '\n'

        message.append(f'Guild: {self.name}')
        for player in self.players:
            message.append(player.player_info())

        return nl.join(message)
