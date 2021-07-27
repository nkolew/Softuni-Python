from abc import ABC, abstractmethod
from project.card.card import Card
from project.card.card_repository import CardRepository


class Player(ABC):
    _username: str
    _health: int

    @abstractmethod
    def __init__(self, username: str, health: int) -> None:
        self.username = username
        self.health = health
        self.card_repository = CardRepository()

    @property
    def is_dead(self) -> bool:
        return self.health <= 0

    @property
    def username(self):
        """The username property."""
        return self._username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError("Player's username cannot be an empty string.")
        self._username = value

    @property
    def health(self):
        """The health property."""
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError(
                "Player's health bonus cannot be less than zero.")
        self._health = value

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        try:
            self.health -= damage_points
        except ValueError:
            self.health = 0

    @property
    def damage_points(self):
        return sum(
            c.damage_points
            for c in self.card_repository.cards)

    def __str__(self) -> str:
        message = []
        message.append(
            f'Username: {self.username} - Health: {self.health} - Cards {len(self.card_repository.cards)}')
        for c in self.card_repository.cards:
            message.append(str(c))
        return '\n'.join(message)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.username == o.username

    def apply_bonus(self):
        self.health += sum(c.health_points for c in self.card_repository.cards)

    def add(self, card: Card):
        self.card_repository.add(card)
