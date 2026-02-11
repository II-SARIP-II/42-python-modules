from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int):
            raise TypeError("Attack must be integers")
        if not isinstance(health, int):
            raise TypeError("Health must be integers")
        if attack < 0 or health < 0:
            raise ValueError("Stats must be positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        try:
            target_health = getattr(target, 'health', 0)
            resolved = self.attack >= target_health
            return {
                "attacker": self.name,
                "target": getattr(target, 'name', "Unknown"),
                "damage_dealt": self.attack,
                "combat_resolved": resolved
            }
        except Exception as e:
            return {"error": f"Combat failed: {str(e)}"}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
