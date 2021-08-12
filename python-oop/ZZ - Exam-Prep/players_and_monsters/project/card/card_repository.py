from typing import List, Optional

from project.card.card import Card


class CardRepository:
    cards: List[Card]

    def __init__(self) -> None:
        self.cards = []

    @property
    def count(self) -> int:
        return len(self.cards)

    def add(self, card: Card) -> None:
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)

    def find(self, name: str) -> Optional[Card]:
        for c in self.cards:
            if c.name == name:
                return c

        return None

    def remove(self, card_name: str):
        if card_name == '':
            raise ValueError("Card cannot be an empty string!")

        card = self.find(card_name)
        if card:
            self.cards.remove(card)
