from typing import List, Optional

from project.card.card import Card


class CardRepository:
    count: int
    cards: List[Card]

    def __init__(self) -> None:
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")

        c = self.find(card)
        if c:
            self.cards.pop(self.cards.index(c))
            self.count -= 1

    def find(self, name: str) -> Optional[Card]:
        for c in self.cards:
            if c.name == name:
                return c

        return None
