from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Magical, Combatable):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, attack_value: int,
                 defence: int, mana: int):
        super().__init__(name, cost, rarity)
        self.attack_value = attack_value
        self.defence = defence
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": game_state["name"],
            "mana_used": game_state["cost"],
            "effect": "Elite Presence"
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_value,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        a = True if self.health > (incoming_damage - self.defence) else False
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - self.defence,
            "damage_blocked": self.defence,
            "still_alive": a
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "hp": self.health,
            "attack_damage": self.attack_value,
            "defend": self.defence
        }

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        target_names = [target.name for target in targets]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana": self.mana,
        }
