from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
from project.battle_field import BattleField


class Controller:
    def __init__(self) -> None:
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str) -> str:
        player_types = {
            'Beginner': Beginner,
            'Advanced': Advanced,
        }
        player = player_types[type](username)
        self.player_repository.players.append(player)
        return f'Successfully added player of type {type} with username: {username}'

    def add_card(self, type: str, name: str) -> str:
        card_types = {
            'Magic': MagicCard,
            'Trap': TrapCard
        }
        card = card_types[type](name)
        self.card_repository.cards.append(card)
        return f'Successfully added card of type {type}Card with name: {name}'

    def add_player_card(self, username: str, card_name: str):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)

        if player and card:
            player.add(card)
            return f'Successfully added card: {card_name} to user: {username}'

    def fight(self, attacker_name: str, enemy_name: str):
        attacker = self.player_repository.find(attacker_name)
        enemy = self.player_repository.find(enemy_name)

        if attacker and enemy:
            bf = BattleField()
            try:
                bf.fight(attacker, enemy)
            except ValueError:
                message = f'Attack user health {attacker.health} - Enemy user health {enemy.health}'
                return message

    def report(self):
        """Returns a report message in format:
        Username: {username1} - Health: {health1} - Cards {cards_count1}
        ### Card: {name1} - Damage: {card_damage1}"""

        return '\n'.join([
            str(p) for p in self.player_repository.players
        ])
