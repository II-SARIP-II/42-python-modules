from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        try:
            effect_map = {
                "damage": ("Deal damage to "
                           f"{len(targets) if targets else 'target'}"),
                "heal": "Restore health to targets",
                "buff": "Increase target stats",
                "debuff": "Decrease target stats"
            }
            description = effect_map.get(self.effect_type.lower(),
                                         f"Apply {self.effect_type}")
            return {
                'card_played': self.name,
                'targets_hit': targets,
                'effect_description': description,
                'status': 'resolved'
            }
        except Exception as e:
            return {"error": f"Spell failed: {str(e)}"}
