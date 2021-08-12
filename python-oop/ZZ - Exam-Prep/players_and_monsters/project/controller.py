from typing import Optional

from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    player_repository: PlayerRepository
    card_repository: CardRepository

    def __init__(self) -> None:
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()
        self.battle_field = BattleField()

    def add_player(self, player_type: str, username: str) -> str:
        player_types = {
            'Beginner': Beginner,
            'Advanced': Advanced
        }

        player = player_types[player_type](username)
        self.player_repository.add(player)
        return f'Successfully added player of type {player_type} with username: {username}'

    def add_card(self, card_type: str, name: str) -> str:
        card_types = {
            'Magic': MagicCard,
            'Trap': TrapCard,
        }

        card = card_types[card_type](name)
        self.card_repository.add(card)
        return f'Successfully added card of type {card_type}Card with name: {name}'

    def add_player_card(self, username: str, card_name: str) -> Optional[str]:
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        if not (player and card):
            return

        player.card_repository.add(card)
        return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attack_name: str, enemy_name: str) -> Optional[str]:
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        if not (attacker and enemy):
            return

        self.battle_field.fight(attacker, enemy)
        return f'Attack user health {attacker.health} - Enemy user health {enemy.health}'

    def report(self):
        return '\n'.join([str(p) for p in self.player_repository.players])
