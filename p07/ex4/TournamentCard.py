from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, defence: int, attack_value: int,
                 id: str) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.defence = defence
        self.attack_value = attack_value
        self.wins = 0
        self.losses = 0
        self.id = id

    # Card
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": "Card summoned to battlefield"
        }

    # Combatable
    def attack(self, target: Card) -> dict:
        try:
            target_health = getattr(target, 'health', 0)
            resolved = self.attack >= target_health
            if resolved is True:
                self.update_wins(1)
            return {
                "attacker": self.name,
                "target": getattr(target, 'name', "Unknown"),
                "damage_dealt": self.attack,
                "combat_resolved": resolved
            }
        except Exception as e:
            return {"error": f"Combat failed: {str(e)}"}

    # Combatable
    def defend(self, incoming_damage: int) -> dict:
        a = True if self.health > (incoming_damage - self.defence) else False
        if a is False:
            self.update_losses(1)
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - self.defence,
            "damage_blocked": self.defence,
            "still_alive": a
        }

    # Combatable
    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "hp": self.health,
            "attack_damage": self.attack_value,
            "defend": self.defence
        }

    # Rankable
    def calculate_rating(self) -> int:
        return 1200 + (self.wins * 16) - (self.losses * 16)

    # Rankable
    def update_wins(self, wins: int) -> None:
        self.wins += wins

    # Rankable
    def update_losses(self, losses: int) -> None:
        self.losses += losses

    # Rankable
    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }
