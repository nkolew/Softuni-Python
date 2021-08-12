from abc import ABC, abstractmethod

from project.card.card_repository import CardRepository


class Player(ABC):
    _username: str
    _health: int

    def __init__(self, username: str) -> None:
        self.username = username
        self.health = self._initial_health
        self.card_repository = CardRepository()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.username == o.username

    def __str__(self) -> str:
        nl = '\n'
        return nl.join([
            f'Username: {self.username} - Health: {self.health} - Cards {len(self.card_repository.cards)}',
            f'{nl.join([str(c) for c in self.card_repository.cards])}',
        ])

    @ property
    @ abstractmethod
    def _initial_health(self) -> int:
        ...

    @ property
    def username(self):
        """The username property."""
        return self._username

    @ username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Player's username cannot be an empty string.")
        self._username = value

    @ property
    def health(self):
        """The health property."""
        return self._health

    @ health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self._health = value

    @ property
    def is_dead(self) -> bool:
        return self.health <= 0

    def take_damage(self, damage_points: int) -> None:
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")

        if damage_points > self.health:
            damage_points = self.health

        self.health -= damage_points

    def apply_bonus(self) -> None:
        health_bonus = sum(c.health_points for c in self.card_repository.cards)
        self.health += health_bonus

    def attack(self, enemy: 'Player'):
        for c in self.card_repository.cards:
            enemy.take_damage(c.damage_points)
            if enemy.is_dead:
                return
