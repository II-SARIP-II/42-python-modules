from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    # Card
    def play(self, game_state: dict) -> dict:
        pass

    # Combatable
    def attack(self, target: Card) -> dict:
        pass

    # Combatable
    def defend(self, incoming_damage: int) -> dict:
        pass

    # Combatable
    def get_combat_stats(self) -> dict:
        pass

    # Rankable
    def calculate_rating(self) -> int:
        pass

    # Rankable
    def update_wins(self, wins: int) -> None:
        pass

    # Rankable
    def update_losses(self, losses: int) -> None:
        pass

    # Rankable
    def get_rank_info(self) -> dict:
        pass
