from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if "dragon" in name_or_power.lower():
            return CreatureCard(name_or_power, 5, "Legendary", 6, 12)
        if "goblin" in name_or_power.lower():
            return CreatureCard(name_or_power, 2, "Common", 2, 5)
        else:
            return CreatureCard(name_or_power, 3, "Legendary", 6, 12)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if "lightning" in name_or_power.lower():
            return SpellCard(name_or_power, 3, "Common", "damage")
        if "heal" in name_or_power.lower():
            return SpellCard(name_or_power, 3, "Common", "heal")
        if "buff" in name_or_power.lower():
            return SpellCard(name_or_power, 3, "Common", "buff")
        else:
            return SpellCard(name_or_power, 3, "Common", "debuff")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if "mana" in name_or_power.lower():
            return ArtifactCard(name_or_power, 2, "Common", 5, "+1 mana")
        if "heal" in name_or_power.lower():
            return ArtifactCard(name_or_power, 2, "Common", 5, "+1 health")
        else:
            return ArtifactCard(name_or_power, 2, "Common", 5, "-1 cost")

    def create_themed_deck(self, size: int) -> dict:
        return {
            "deck_name": "Dragon's Hoard",
            "size": size
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
