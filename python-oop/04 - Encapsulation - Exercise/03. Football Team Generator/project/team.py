from typing import List, Union

from project import Player


class Team:
    __name: str
    __rating: int
    __players: List[Player]

    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        """The name property."""
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f'Player {player.name} has already joined'

        self.__players.append(player)
        return f'Player {player.name} joined team {self.name}'

    def remove_player(self, player_name: str) -> Union[Player, str]:
        for i, p in enumerate(self.__players):
            if p.name == player_name:
                return self.__players.pop(i)

        return f'Player {player_name} not found'
