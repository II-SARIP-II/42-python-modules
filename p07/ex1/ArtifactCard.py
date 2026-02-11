from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect = effect
        if not isinstance(durability, int):
            raise TypeError("durability must be integers")
        if durability < 0:
            raise ValueError("durability must be positive")
        self.durability = durability

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {"action": "Ability activated",
                    "remaining_durability": self.durability}
        return {"error": "Artifact is broken"}
