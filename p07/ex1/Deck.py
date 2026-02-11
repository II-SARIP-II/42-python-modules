from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            return None
        drawn_card = self.cards.pop(0)
        return drawn_card

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        cost = 0
        for c in self.cards:
            if c.__class__.__name__ == "CreatureCard":
                creatures += 1
            if c.__class__.__name__ == "SpellCard":
                spells += 1
            if c.__class__.__name__ == "ArtifactCard":
                artifacts += 1
            cost += c.cost
        return {
            'total_cards': len(self.cards),
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': cost/len(self.cards)
        }
